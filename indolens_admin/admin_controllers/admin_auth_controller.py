import datetime
import string
import random

import bcrypt
import pymysql
from indolens.db_connection import getConnection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_controllers.admin_setting_controller import get_base_url
from indolens_admin.admin_models.admin_req_model import admin_auth_model
from indolens_admin.admin_models.admin_resp_model.admin_auth_resp_model import get_admin_user

import pytz

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def login(admin_obj):
    try:
        with getConnection().cursor() as cursor:
            login_query = f"""SELECT * FROM admin WHERE admin_email = '{admin_obj.email}'"""
            cursor.execute(login_query)
            admin_data = cursor.fetchone()
            print(admin_data)
            if admin_data is None:
                return {
                    "status": False,
                    "message": "Invalid admin email",
                    "admin": None
                }, 301

            elif admin_obj is not None and admin_data['admin_status'] != 0:
                if bcrypt.checkpw(admin_obj.password.encode('utf-8'), admin_data['admin_password'].encode('utf-8')):
                    return {
                        "status": True,
                        "message": "admin login successfull",
                        "admin": admin_data
                    }, 200
                else:
                    return {
                        "status": False,
                        "message": "Invalid admin password",
                        "admin": None
                    }, 301
            elif admin_obj is not None and admin_data['admin_status'] == 0:
                return {
                    "status": False,
                    "message": "The id has been blocked, please contact super admin",
                    "admin": None
                }, 301

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def forgot_password(email):
    try:
        with getConnection().cursor() as cursor:
            pwd_code = generate_random_string()
            reset_pwd_link = f"{get_base_url()}/admin/reset_password/code={pwd_code}"
            print("++++++++++++++reset_pwd_link++++++++++++++++++")
            print(reset_pwd_link)

            check_email_query = f"""SELECT admin_email, admin_status, admin_name FROM admin WHERE admin_email = '{email}'"""
            cursor.execute(check_email_query)
            check_email = cursor.fetchone()

            if check_email is None:
                return {
                    "status": False,
                    "message": "Please enter the valid email to reset the password"
                }, 200

            elif check_email is not None and check_email['admin_status'] != 0:
                update_pwd_code_query = f"""INSERT INTO reset_password (rpwd_email, rpwd_code, rpwd_status, rpwd_created_on) 
                                            VALUES (%s, %s, %s, %s)"""
                cursor.execute(update_pwd_code_query, (email, pwd_code, 0, getIndianTime()))

                subject = email_template_controller.get_password_reset_email_subject(email)
                body = email_template_controller.get_password_reset_email_body(check_email['admin_name'], reset_pwd_link, email)
                email_response = send_notification_controller.send_email(subject, body, email)

                if email_response.status_code == 200:
                    return {
                        "status": True,
                        "message": f"Password reset link sent successfully. Please check you email: {email} for password reset link."
                    }, 200
                else:
                    return {
                        "status": False,
                        "message": f"Failed to send password reset link to {email}. Please try again or contact your "
                                   f"admin. "
                    }, 200
            elif check_email is not None and check_email['admin_status'] == 0:
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


def update_admin_password(password, email):
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with getConnection().cursor() as cursor:
            login_query = f"""UPDATE admin SET admin_password = %s WHERE admin_email = '{email}'"""
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
