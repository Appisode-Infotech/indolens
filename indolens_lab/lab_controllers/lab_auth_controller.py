import datetime
import json
import random
import string

import bcrypt
import pymysql
import pytz
import requests
from indolens.db_connection import getConnection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_controllers.admin_setting_controller import get_base_url
from indolens_franchise_store.franchise_store_model.franchise_store_resp_model.franchise_store_emp_resp_model import \
    get_franchise_store_employees
from indolens_lab.lab_models.response_model.lab_tech_resp_model import get_lab_tech

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def lab_login(lab_obj):
    try:
        with getConnection().cursor() as cursor:
            login_query = f"""SELECT lt.*, l.lab_name AS lab_name
                        FROM lab_technician AS lt
                        LEFT JOIN lab AS l ON lt.lt_assigned_lab_id = l.lab_lab_id
                        WHERE lt.lt_email = '{lab_obj.email}'
                        """
            cursor.execute(login_query)
            lab_tech_data = cursor.fetchone()
            if not lab_tech_data:
                return {
                    "status": False,
                    "message": "Invalid user email",
                    "lab_tech": None
                }, 301
            elif lab_tech_data['lt_status'] == 0:
                return {
                    "status": False,
                    "message": "Your Account is locked, please contact your Admin",
                    "lab_tech": None
                }, 301
            elif lab_tech_data['lt_assigned_lab_id'] == 0:
                return {
                    "status": False,
                    "message": "Your Account is not assigned to any Lab, please contact your Admin",
                    "lab_tech": None
                }, 301
            elif bcrypt.checkpw(lab_obj.password.encode('utf-8'), lab_tech_data['lt_password'].encode('utf-8')):

                get_lab_query = f""" SELECT lab_status FROM lab WHERE lab_lab_id = '{lab_tech_data['lt_assigned_lab_id']}'"""
                cursor.execute(get_lab_query)
                assigned_lab_status = cursor.fetchone()
                if assigned_lab_status['lab_status'] == 0:
                    return {
                        "status": False,
                        "message": "Your Account is assigned to an inactive lab, please contact your Admin",
                        "store": lab_tech_data
                    }, 200
                else:
                    return {
                        "status": True,
                        "message": "user login successfull",
                        "lab_tech": lab_tech_data
                    }, 200
            else:
                return {
                    "status": False,
                    "message": "Invalid user password",
                    "lab_tech": None
                }, 301

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_assigned_lab(lab_tech_id):
    try:
        with getConnection().cursor() as cursor:
            get_assigned_lab = f"""SELECT lt_assigned_lab_id FROM lab_technician 
                                WHERE lt_lab_technician_id = '{lab_tech_id}'"""
            cursor.execute(get_assigned_lab)
            assigned_lab = cursor.fetchone()
            return assigned_lab['lt_assigned_lab_id']
    except pymysql.Error as e:
        return 0
    except Exception as e:
        return 0


def forgot_password(email):
    try:
        with getConnection().cursor() as cursor:
            pwd_code = generate_random_string()
            reset_pwd_link = f"{get_base_url()}/lab/lab_reset_password/code={pwd_code}"
            print(reset_pwd_link)

            check_email_query = f"""SELECT lt_email, lt_status, lt_name FROM lab_technician WHERE lt_email = '{email}'"""
            cursor.execute(check_email_query)
            check_email = cursor.fetchone()

            if check_email is None:
                return {
                    "status": False,
                    "message": "Please enter the valid email to reset the password"
                }, 200

            elif check_email is not None and check_email['lt_status'] != 0:
                update_pwd_code_query = f"""INSERT INTO reset_password (rpwd_email, rpwd_code, rpwd_status, rpwd_created_on) 
                                            VALUES (%s, %s, %s, %s)"""
                cursor.execute(update_pwd_code_query, (email, pwd_code, 0, getIndianTime()))

                subject = email_template_controller.get_password_reset_email_subject(check_email['lt_name'])
                body = email_template_controller.get_password_reset_email_body(check_email['lt_name'], reset_pwd_link, email)
                email_response = send_notification_controller.send_email(subject, body, email)

                if email_response.status_code == 200:
                    return {
                        "status": True,
                        "message": f"Password reset link sent successfully. Please check you email: {email} for password reset link."
                    }, 200
                else:
                    return {
                        "status": False,
                        "message": f"Failed to send password reset link to {email}. Please try again or contact your admin."
                    }, 200
            elif check_email is not None and check_email['lt_status'] == 0:
                return {
                    "status": False,
                    "message": "Password reset Failed due to Inactive Account. Please contact your Admin"
                }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def check_link_validity(code):
    try:
        with getConnection().cursor() as cursor:
            check_link_validity_query = f""" SELECT rpwd_status, rpwd_created_on, rpwd_email FROM reset_password 
                                                WHERE rpwd_code = '{code}'
                                                ORDER BY rpwd_reset_password_id DESC LIMIT 1"""
            cursor.execute(check_link_validity_query)
            link_validity = cursor.fetchone()

            if link_validity is None:
                return {
                    "status": True,
                    "message": "Invalid link to reset Password",
                    "email": ""
                }, 200

            else:
                email = link_validity['rpwd_email']
                query_datetime = ist.localize(link_validity['rpwd_created_on'])
                current_datetime = datetime.datetime.now(ist)
                time_difference = current_datetime - query_datetime
                time_difference_mins = time_difference.total_seconds() / 60

                if link_validity is not None and (link_validity['rpwd_status'] == 1 or time_difference_mins > 15):
                    return {
                        "status": True,
                        "message": "Password reset link has been expired",
                        "email": ""
                    }, 200
                elif link_validity is not None and link_validity['rpwd_status'] == 0 and time_difference_mins < 15:
                    return {
                        "status": True,
                        "message": "",
                        "email": email
                    }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e), "email": ""}, 301
    except Exception as e:
        return {"status": False, "message": str(e), "email": ""}, 301


def update_lab_tech_password(password, email):
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with getConnection().cursor() as cursor:
            login_query = f"""UPDATE lab_technician SET lt_password = %s WHERE lt_email = '{email}'"""
            cursor.execute(login_query, (hashed_password,))

            login_query = f"""UPDATE reset_password SET rpwd_status = 1 WHERE rpwd_email = '{email}'"""
            cursor.execute(login_query)

            return {
                "status": True,
                "message": "Password changed successfully. Please login using new credentials",
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
