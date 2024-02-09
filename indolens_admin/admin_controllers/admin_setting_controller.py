import datetime
import json
import string
import random

import bcrypt
import pymysql
from django.db import connection

import pytz

from indolens_admin.admin_models.admin_resp_model.admin_setting_resp_model import admin_setting_response

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def admin_setting(data):
    try:
        with connection.cursor() as cursor:
            admin_setting_check = f""" SELECT COUNT(*) FROM admin_setting """
            cursor.execute(admin_setting_check)
            admin_check = cursor.fetchone()
            print(admin_check)

            emailjs_attributes = {
                'emailjs_url': data.get('emailjs_url', ''),
                'emailjs_service_id': data.get('emailjs_service_id', ''),
                'emailjs_template_id': data.get('emailjs_template_id', ''),
                'emailjs_user_id': data.get('emailjs_user_id', ''),
                'emailjs_recaptcha': data.get('emailjs_recaptcha', ''),
            }

            if admin_check[0] == 0:
                admin_setting_query = f"""INSERT INTO admin_setting (emailjs_attribute, base_url, created_on,
                created_by, updated_on, updated_by ) VALUES('{json.dumps(emailjs_attributes)}', '{data.get('base_url')}',
                '{getIndianTime()}', 1, '{getIndianTime()}', 1) """
                cursor.execute(admin_setting_query)
                return {"status": True, "message": "Insert Success"}, 200
            else:
                admin_setting_query = f"""
                    UPDATE admin_setting 
                    SET 
                        emailjs_attribute = '{json.dumps(emailjs_attributes)}', 
                        base_url = '{data.get('base_url')}',
                        updated_on = '{getIndianTime()}',
                        updated_by = 1
                    WHERE setting_id = 1
                """
                cursor.execute(admin_setting_query)

                return {"status": True, "message": "Update Success"}, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_admin_setting():
    try:
        with connection.cursor() as cursor:
            admin_setting_check = f""" SELECT * FROM admin_setting """
            cursor.execute(admin_setting_check)
            admin_check = cursor.fetchone()
            return {"status": True,
                    "message": "Update Success",
                    "admin_setting": admin_setting_response(admin_check)
                    }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
