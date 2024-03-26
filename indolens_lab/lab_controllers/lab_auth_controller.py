import datetime
import json
import random
import string

import bcrypt
import pymysql
import pytz
import requests
from indolens.db_connection import connection

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
        with connection.cursor() as cursor:
            login_query = f"""SELECT lt.*, creator.name, updater.name, l.lab_name
                        FROM lab_technician AS lt
                        LEFT JOIN lab AS l ON lt.assigned_lab_id = l.lab_id
                        LEFT JOIN admin AS creator ON lt.created_by = creator.admin_id
                        LEFT JOIN admin AS updater ON lt.last_updated_by = updater.admin_id
                        WHERE lt.email = '{lab_obj.email}'
                        """
            cursor.execute(login_query)
            lab_tech_data = cursor.fetchall()
            if not lab_tech_data:
                return {
                    "status": False,
                    "message": "Invalid user email",
                    "lab_tech": None
                }, 301
            elif lab_tech_data[0][12] == 0:
                return {
                    "status": False,
                    "message": "Your Account is locked, please contact your Admin",
                    "lab_tech": None
                }, 301
            elif lab_tech_data[0][6] == 0:
                return {
                    "status": False,
                    "message": "Your Account is not assigned to any Lab, please contact your Admin",
                    "lab_tech": None
                }, 301
            elif bcrypt.checkpw(lab_obj.password.encode('utf-8'), lab_tech_data[0][4].encode('utf-8')):
                lab = get_lab_tech(lab_tech_data)
                get_lab_query = f""" SELECT status FROM lab WHERE lab_id = '{lab[0]['assigned_lab_id']}'"""
                cursor.execute(get_lab_query)
                assigned_lab_status = cursor.fetchone()
                if assigned_lab_status[0] == 0:
                    return {
                        "status": False,
                        "message": "Your Account is assigned to an inactive lab, please contact your Admin",
                        "store": lab
                    }, 200
                else:
                    return {
                        "status": True,
                        "message": "user login successfull",
                        "lab_tech": lab
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
        with connection.cursor() as cursor:
            get_assigned_lab = f"""SELECT assigned_lab_id FROM lab_technician 
                                WHERE lab_technician_id = '{lab_tech_id}'"""
            cursor.execute(get_assigned_lab)
            assigned_lab = cursor.fetchone()
            return assigned_lab[0]
    except pymysql.Error as e:
        return 0
    except Exception as e:
        return 0


def forgot_password(email):
    try:
        with connection.cursor() as cursor:
            pwd_code = generate_random_string()
            reset_pwd_link = f"{get_base_url()}/lab/lab_reset_password/code={pwd_code}"
            print(reset_pwd_link)

            check_email_query = f"""SELECT email,status, name FROM lab_technician WHERE email = '{email}'"""
            cursor.execute(check_email_query)
            check_email = cursor.fetchone()

            if check_email is None:
                return {
                    "status": False,
                    "message": "Please enter the valid email to reset the password"
                }, 200

            elif check_email is not None and check_email[1] != 0:
                update_pwd_code_query = f"""INSERT INTO reset_password (email, code, status, created_on) 
                                            VALUES (%s, %s, %s, %s)"""
                cursor.execute(update_pwd_code_query, (email, pwd_code, 0, getIndianTime()))

                subject = email_template_controller.get_password_reset_email_subject(check_email[1])
                body = email_template_controller.get_password_reset_email_body(check_email[1], reset_pwd_link, email)
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
            elif check_email is not None and check_email[1] == 0:
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
        with connection.cursor() as cursor:
            check_link_validity_query = f""" SELECT status, created_on, email FROM reset_password WHERE code = '{code}'
                                                ORDER BY reset_password_id DESC LIMIT 1"""
            cursor.execute(check_link_validity_query)
            link_validity = cursor.fetchone()

            if link_validity is None:
                return {
                    "status": True,
                    "message": "Invalid link to reset Password",
                    "email": ""
                }, 200

            else:
                email = link_validity[2]
                query_datetime = ist.localize(link_validity[1])
                current_datetime = datetime.datetime.now(ist)
                time_difference = current_datetime - query_datetime
                time_difference_mins = time_difference.total_seconds() / 60

                if link_validity is not None and (link_validity[0] == 1 or time_difference_mins > 15):
                    return {
                        "status": True,
                        "message": "Password reset link has been expired",
                        "email": ""
                    }, 200
                elif link_validity is not None and link_validity[0] == 0 and time_difference_mins < 15:
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
        with connection.cursor() as cursor:
            login_query = f"""UPDATE lab_technician SET password = %s WHERE email = '{email}'"""
            cursor.execute(login_query, (hashed_password,))

            login_query = f"""UPDATE reset_password SET status = 1 WHERE email = '{email}'"""
            cursor.execute(login_query)

            return {
                "status": True,
                "message": "Password changed successfully. Please login using new credentials",
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
