import datetime
import json
import string
import random

import bcrypt
import pymysql
import pytz
import requests
from django.db import connection

from indolens_admin.admin_models.admin_req_model import admin_auth_model
from indolens_admin.admin_models.admin_resp_model.admin_auth_resp_model import get_admin_user
from migrate_db import cursor

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def login(admin_obj):
    try:
        with connection.cursor() as cursor:
            login_query = f"""SELECT * FROM admin WHERE email = '{admin_obj.email}'"""
            cursor.execute(login_query)
            admin_data = cursor.fetchone()
            if admin_data is None:
                return {
                    "status": False,
                    "message": "Invalid admin email",
                    "admin": None
                }, 301

            elif admin_obj is not None and admin_data[12] != 0:
                if bcrypt.checkpw(admin_obj.password.encode('utf-8'), admin_data[4].encode('utf-8')):
                    return {
                        "status": True,
                        "message": "admin login successfull",
                        "admin": admin_auth_model.admin_auth_model_from_dict(get_admin_user(admin_data))
                    }, 200
                else:
                    return {
                        "status": False,
                        "message": "Invalid admin password",
                        "admin": None
                    }, 301
            elif admin_obj is not None and admin_data[12] == 0:
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
        with connection.cursor() as cursor:
            pwd_code = generate_random_string()
            reset_pwd_link = f"http://127.0.0.1:8000/admin/reset_password/code={pwd_code}"
            print(reset_pwd_link)

            check_email_query = f"""SELECT email,status FROM admin WHERE email = '{email}'"""
            cursor.execute(check_email_query)
            check_email = cursor.fetchone()
            print(check_email)

            if check_email is None:
                return {
                    "status": False,
                    "message": "Please enter the valid email to reset the password"
                }, 200

            elif check_email is not None and check_email[1] != 0:
                update_pwd_code_query = f"""INSERT INTO reset_password (email, code, status, created_on) 
                                            VALUES (%s, %s, %s, %s)"""
                cursor.execute(update_pwd_code_query, (email, pwd_code, 0, today))

                url = 'https://api.emailjs.com/api/v1.0/email/send'
                data = {
                    'service_id': 'default_service',
                    'template_id': 'template_ycnjmqh',
                    'user_id': 'qbWAgwqHOFbcgoJRF',
                    'template_params': {
                        'to_email': email,
                        'new_password': reset_pwd_link,
                        'g-recaptcha-response': '03AHJ_ASjnLA214KSNKFJAK12sfKASfehbmfd...'
                    }
                }

                headers = {'Content-Type': 'application/json'}

                email_response = requests.post(url, data=json.dumps(data), headers=headers)
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


def update_admin_password(password, email):
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with connection.cursor() as cursor:
            login_query = f"""UPDATE admin SET password = %s WHERE email = '{email}'"""
            cursor.execute(login_query, (hashed_password,))
            admin_data = cursor.fetchone()

            login_query = f"""UPDATE reset_password SET status = 1 WHERE email = '{email}'"""
            cursor.execute(login_query)

            return {
                "status": True,
                "message": "Password change was successfully. Please login in now",
                "admin": admin_auth_model.admin_auth_model_from_dict(get_admin_user(admin_data))
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
