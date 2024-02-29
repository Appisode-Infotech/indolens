import datetime
import json
import random
import string

import bcrypt
import pymysql
import pytz
import requests
from django.db import connection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_controllers.admin_setting_controller import get_base_url
from indolens_own_store.own_store_model.response_model.own_store_emp_resp_model import get_own_store_employees

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
        with connection.cursor() as cursor:
            login_query = f"""SELECT ose.*, os.store_name, creator.name, updater.name FROM own_store_employees AS ose 
                                LEFT JOIN own_store AS os ON ose.assigned_store_id = os.store_id
                                LEFT JOIN admin AS creator ON ose.created_by = creator.admin_id
                                LEFT JOIN admin AS updater ON ose.last_updated_by = updater.admin_id
                                WHERE ose.email = '{store_ob.email}' AND ose.role != 4 """
            cursor.execute(login_query)
            admin_data = cursor.fetchall()

            if not admin_data:
                return {
                    "status": False,
                    "message": "Invalid user email",
                    "store": None
                }, 301
            elif admin_data[0][12] == 0:
                return {
                    "status": False,
                    "message": "Your Account is locked, please contact your Admin",
                    "store": None
                }, 301
            elif admin_data[0][6] == 0:
                return {
                    "status": False,
                    "message": "Your Account is not assigned to any store, please contact your Admin",
                    "store": None
                }, 301
            elif bcrypt.checkpw(store_ob.password.encode('utf-8'), admin_data[0][4].encode('utf-8')):
                store = get_own_store_employees(admin_data)
                get_assigned_store_status = f"""SELECT status FROM own_store
                                                 WHERE store_id = '{store[0]['assigned_store_id']}'"""
                cursor.execute(get_assigned_store_status)
                assigned_store_status = cursor.fetchone()

                if assigned_store_status[0] == 0:
                    return {
                        "status": False,
                        "message": "Your Account is assigned to an inactive store, please contact your Admin",
                        "store": store
                    }, 200
                else:
                    return {
                        "status": True,
                        "message": "user login successfull",
                        "store": store
                    }, 200


            else:
                return {
                    "status": False,
                    "message": "Invalid user password",
                    "store": None
                }, 301

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_assigned_store(employee_id):
    try:
        with connection.cursor() as cursor:
            get_assigned_store = f"""SELECT assigned_store_id FROM own_store_employees 
                                WHERE employee_id = '{employee_id}'"""
            cursor.execute(get_assigned_store)
            assigned_store = cursor.fetchone()

            if assigned_store[0] != 0:
                get_assigned_store_status = f"""SELECT status FROM own_store 
                                                WHERE store_id = '{assigned_store[0]}'"""
                cursor.execute(get_assigned_store_status)
                assigned_store_status = cursor.fetchone()
                if assigned_store_status[0] == 0:
                    return 0
                else:
                    return assigned_store[0]

            else:
                return assigned_store[0]

    except pymysql.Error as e:
        return 0
    except Exception as e:
        return 0


def forgot_password(email):
    try:
        with connection.cursor() as cursor:
            pwd_code = generate_random_string()
            reset_pwd_link = f"{get_base_url()}/own_store/reset_password/code={pwd_code}"
            print(reset_pwd_link)

            check_email_query = f"""SELECT email,status, name FROM own_store_employees WHERE email = '{email}'"""
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

                subject = email_template_controller.get_password_reset_email_subject(email)
                body = email_template_controller.get_password_reset_email_body(check_email[2], reset_pwd_link, email)
                email_response = send_notification_controller.send_email(subject, body, email)
                print(email_response.status_code)

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


def update_store_employee_password(password, email):
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with connection.cursor() as cursor:
            login_query = f"""UPDATE own_store_employees SET password = %s WHERE email = '{email}'"""
            cursor.execute(login_query, (hashed_password,))

            login_query = f"""UPDATE reset_password SET status = 1 WHERE email = '{email}'"""
            cursor.execute(login_query)

            return {
                "status": True,
                "message": "Password changed successfully. Please login using new credentials"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
