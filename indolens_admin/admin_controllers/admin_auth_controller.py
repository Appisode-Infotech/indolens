import string
import random
import pymysql
from django.contrib.sites import requests
from django.db import connection

from indolens_admin.admin_models.admin_req_model import admin_auth_model
from indolens_admin.admin_models.admin_resp_model.admin_auth_resp_model import get_admin_user

def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def login(admin_obj):
    try:
        with connection.cursor() as cursor:
            login_query = f"""SELECT * FROM admin WHERE email = '{admin_obj.email}';"""
            cursor.execute(login_query)
            admin_data = cursor.fetchone()
            if admin_data is None:
                return {
                           "status": False,
                           "message": "Invalid admin email",
                           "admin": None
                       }, 301
            elif admin_data[4] != admin_obj.password:
                return {
                           "status": False,
                           "message": "Invalid admin password",
                           "admin": None
                       }, 301
            else:
                return {
                           "status": True,
                           "message": "admin login successfull",
                           "admin": admin_auth_model.admin_auth_model_from_dict(get_admin_user(admin_data))
                       }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def forgot_password(email):
    try:
        with connection.cursor() as cursor:
            pwd_code = generate_random_string()
            reset_pwd_link = f"http://127.0.0.1:8000/admin/reset_password/code={pwd_code}"
            update_pwd_code_query = f"""INSERT INTO reset_password (email, code, status, created_on, created_by) 
                                        VALUES (%s, %s, %s, %s, %s, %s)"""

            # # Execute the query with the data
            # cursor.execute(sql, (email, code, status, created_on, created_by))

            cursor.execute(update_pwd_code_query)

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
                sql_query = f"""UPDATE printer SET printer_password = '{hashed_password}' WHERE email = '{email}' """
                cursor.execute(sql_query)
                return {
                    "status": True,
                    "message": f"Password reset successful. We have sent an email to {email} with new password."
                }, 200
            else:
                return {
                    "status": False,
                    "message": f"Failed to send the new password to {email}. Please try again or contact your admin if you are facing the issue continiously"
                }, 200


    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301