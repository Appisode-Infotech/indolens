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

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def login(store_ob):
    try:
        with getConnection().cursor() as cursor:
            login_query = f"""SELECT fse.*, fs.fs_store_name AS store_name FROM franchise_store_employees AS fse 
                                LEFT JOIN franchise_store AS fs ON fse.fse_assigned_store_id = fs.fs_store_id
                                WHERE fse.fse_email = '{store_ob.email}' AND fse.fse_role != 4 """
            cursor.execute(login_query)
            fse_data = cursor.fetchone()
            print(fse_data)
            if not fse_data:
                return {
                    "status": False,
                    "message": "Invalid user email",
                    "fse": None
                }, 301
            elif fse_data['fse_status'] == 0:
                return {
                    "status": False,
                    "message": "Your Account is locked, please contact your Admin",
                    "fse": None
                }, 301
            elif fse_data['fse_assigned_store_id'] == 0:
                return {
                    "status": False,
                    "message": "Your Account is not assigned to any store, please contact your Admin",
                    "fse": None
                }, 301
            elif bcrypt.checkpw(store_ob.password.encode('utf-8'), fse_data['fse_password'].encode('utf-8')):
                get_assigned_store_status = f"""SELECT fs_status FROM franchise_store
                                                WHERE fs_store_id = {fse_data['fse_assigned_store_id']} """
                cursor.execute(get_assigned_store_status)
                assigned_store_status = cursor.fetchone()

                if assigned_store_status['fs_status'] == 0:
                    return {
                        "status": False,
                        "message": "Your Account is assigned to an inactive store, please contact your Admin",
                        "fse": fse_data
                    }, 200
                else:
                    return {
                        "status": True,
                        "message": "user login successfull",
                        "fse": fse_data
                    }, 200
            else:
                return {
                    "status": False,
                    "message": "Invalid user password",
                    "fse": None
                }, 301

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_assigned_store(employee_id):
    try:
        with getConnection().cursor() as cursor:
            get_assigned_store = f"""SELECT fse_assigned_store_id FROM franchise_store_employees 
                                WHERE fse_employee_id = '{employee_id}'"""
            cursor.execute(get_assigned_store)
            assigned_store = cursor.fetchone()

            if assigned_store['fse_assigned_store_id'] != 0:
                get_assigned_store_status = f"""SELECT fs_status FROM franchise_store 
                                                WHERE fs_store_id = '{assigned_store['fse_assigned_store_id']}'"""
                cursor.execute(get_assigned_store_status)
                assigned_store_status = cursor.fetchone()
                if assigned_store_status['fs_status'] == 0:
                    return 0
                else:
                    return assigned_store['fse_assigned_store_id']

            else:
                return assigned_store['fse_assigned_store_id']
    except pymysql.Error as e:
        return 0
    except Exception as e:
        return 0


def forgot_password(email):
    try:
        with getConnection().cursor() as cursor:
            pwd_code = generate_random_string()
            reset_pwd_link = f"{get_base_url()}/franchise_store/franchise_store_reset_password/code={pwd_code}"

            check_email_query = f"""SELECT fse_email,fse_status, fse_name FROM franchise_store_employees 
                                    WHERE fse_email = '{email}'"""
            cursor.execute(check_email_query)
            check_email = cursor.fetchone()

            if check_email is None:
                return {
                    "status": False,
                    "message": "Please enter the valid email to reset the password"
                }, 200

            elif check_email is not None and check_email['fse_status'] != 0:
                update_pwd_code_query = f"""INSERT INTO reset_password (rpwd_email, rpwd_code, rpwd_status, rpwd_created_on) 
                                            VALUES (%s, %s, %s, %s)"""
                cursor.execute(update_pwd_code_query, (email, pwd_code, 0, getIndianTime()))

                subject = email_template_controller.get_password_reset_email_subject(check_email['fse_name'])
                body = email_template_controller.get_password_reset_email_body(check_email['fse_name'], reset_pwd_link, email)
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
            elif check_email is not None and check_email['fse_status'] == 0:
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
                    "status": False,
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
                        "status": False,
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


def update_store_employee_password(password, email):
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with getConnection().cursor() as cursor:
            login_query = f"""UPDATE franchise_store_employees SET fse_password = %s WHERE fse_email = '{email}'"""
            cursor.execute(login_query, (hashed_password,))

            login_query = f"""UPDATE reset_password SET rpwd_status = 1 WHERE rpwd_email = '{email}'"""
            cursor.execute(login_query)

            return {
                "status": True,
                "message": "Password changed successfully. Please login using new credentials"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
