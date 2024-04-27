import datetime
import json
import string
import random

import bcrypt
import pymysql
import pytz
import requests
from indolens.db_connection import getConnection
from indolens_admin.admin_controllers import email_template_controller, send_notification_controller

from indolens_admin.admin_controllers.admin_setting_controller import get_base_url
from indolens_area_head.area_head_model.area_head_resp_models.area_head_resp_model import get_area_heads

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def generate_random_string(length=16):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def login(area_head):
    try:
        with getConnection().cursor() as cursor:
            login_query = f""" SELECT * 
                                FROM area_head                                
                                WHERE ah_email = '{area_head.email}'"""
            cursor.execute(login_query)
            area_head_data = cursor.fetchone()

            if not area_head_data:
                return {
                    "status": False,
                    "message": "Invalid user email",
                    "area_head": None
                }, 301
            elif area_head_data['ah_status'] == 0:
                return {
                    "status": False,
                    "message": "Your Account is locked, please contact your Admin",
                    "area_head": None
                }, 301
            elif area_head_data['ah_assigned_stores'] == "0":
                return {
                    "status": False,
                    "message": "Your Account is not assigned to any store, please contact your Admin",
                    "area_head": None
                }, 301
            elif bcrypt.checkpw(area_head.password.encode('utf-8'), area_head_data['ah_password'].encode('utf-8')):
                return {
                    "status": True,
                    "message": "user login successfull",
                    "area_head": area_head_data
                }, 200
            else:
                return {
                    "status": False,
                    "message": "Invalid user password",
                    "area_head": None
                }, 301

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def forgot_password(email):
    try:
        with getConnection().cursor() as cursor:
            pwd_code = generate_random_string()
            reset_pwd_link = f"{get_base_url()}/area_head/reset_password/code={pwd_code}"
            print(reset_pwd_link)

            check_email_query = f"""SELECT ah_email,ah_status, ah_name FROM area_head WHERE ah_email = '{email}'"""
            cursor.execute(check_email_query)
            check_email = cursor.fetchone()
            print(check_email)

            if check_email is None:
                return {
                    "status": False,
                    "message": "Please enter the valid email to reset the password"
                }, 200

            elif check_email is not None and check_email['ah_status'] != 0:
                update_pwd_code_query = f"""INSERT INTO reset_password (rpwd_email, rpwd_code, rpwd_status, rpwd_created_on) 
                                            VALUES (%s, %s, %s, %s)"""
                cursor.execute(update_pwd_code_query, (email, pwd_code, 0, getIndianTime()))

                subject = email_template_controller.get_password_reset_email_subject(check_email['ah_name'])
                body = email_template_controller.get_password_reset_email_body(check_email['ah_name'], reset_pwd_link,
                                                                               email)
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


def update_area_head_password(password, email):
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with getConnection().cursor() as cursor:
            login_query = f"""UPDATE area_head SET ah_password = %s WHERE ah_email = '{email}'"""
            cursor.execute(login_query, (hashed_password,))
            admin_data = cursor.fetchone()

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


def get_area_head_assigned_store(aread_head_id):
    try:
        with getConnection().cursor() as cursor:
            get_assigned_store = f"""SELECT ah_assigned_stores FROM area_head 
                                WHERE ah_area_head_id = '{aread_head_id}'"""
            cursor.execute(get_assigned_store)
            assigned_store = cursor.fetchone()
            return assigned_store['ah_assigned_stores']

    except pymysql.Error as e:
        return 0
    except Exception as e:
        return 0
