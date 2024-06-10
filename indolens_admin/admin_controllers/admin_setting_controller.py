import datetime
import json
import pymysql
from indolens.db_connection import getConnection

import pytz

from indolens_admin.admin_models.admin_resp_model.admin_setting_resp_model import admin_setting_response

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def admin_setting(data):
    try:
        with getConnection().cursor() as cursor:
            admin_setting_check = f""" SELECT COUNT(*) FROM admin_setting """
            cursor.execute(admin_setting_check)
            admin_check = cursor.fetchone()

            emailjs_attributes = {
                'emailjs_url': data.get('emailjs_url', ''),
                'emailjs_service_id': data.get('emailjs_service_id', ''),
                'emailjs_template_id': data.get('emailjs_template_id', ''),
                'emailjs_user_id': data.get('emailjs_user_id', ''),
            }

            support_attributes = {
                'support_email': data.get('support_email', ''),
                'support_phone': data.get('support_phone', ''),
                'support_hour': data.get('support_hours', ''),
            }

            central_inventory_details = {
                'ci_gst': data.get('ci_gst', ''),
                'ci_phone': data.get('ci_phone', ''),
                'ci_address': data.get('ci_address', ''),
                'ci_email': data.get('ci_email', ''),
                'ci_name': data.get('ci_name', ''),
            }

            if admin_check['COUNT(*)'] == 0:
                admin_setting_query = f"""INSERT INTO admin_setting (emailjs_attribute, base_url, created_on,
                created_by, updated_on, updated_by, support_attributes, central_inventory_details ) 
                VALUES('{json.dumps(emailjs_attributes)}', '{data.get('base_url')}', '{getIndianTime()}', 1, 
                '{getIndianTime()}', 1, '{json.dumps(support_attributes)}', '{json.dumps(central_inventory_details)}') """
                cursor.execute(admin_setting_query)
                return {"status": True, "message": "Insert Success"}, 200
            else:
                admin_setting_query = f"""
                    UPDATE admin_setting 
                    SET 
                        emailjs_attribute = '{json.dumps(emailjs_attributes)}', 
                        base_url = '{data.get('base_url')}',
                        updated_on = '{getIndianTime()}',
                        updated_by = 1,
                        support_attributes = '{json.dumps(support_attributes)}',
                        central_inventory_details = '{json.dumps(central_inventory_details)}'
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
        with getConnection().cursor() as cursor:
            admin_setting_check = f""" SELECT * FROM admin_setting """
            cursor.execute(admin_setting_check)
            admin_settings = cursor.fetchone()

            admin_settings['emailjs_attribute'] = json.loads(admin_settings['emailjs_attribute']) if admin_settings['emailjs_attribute'] else []
            admin_settings['support_attributes'] = json.loads(admin_settings['support_attributes']) if admin_settings['support_attributes'] else []
            admin_settings['central_inventory_details'] = json.loads(admin_settings['central_inventory_details']) if admin_settings['central_inventory_details'] else []
            return {"status": True,
                    "message": "fetch Success",
                    "admin_setting": admin_settings if admin_settings is not None else {},
                    }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_emailjs_attribute():
    try:
        with getConnection().cursor() as cursor:
            admin_setting_check = f""" SELECT emailjs_attribute FROM admin_setting """
            cursor.execute(admin_setting_check)
            admin_check = cursor.fetchone()
            return json.loads(admin_check['emailjs_attribute']) if admin_check is not None else {}

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_base_url():
    try:
        with getConnection().cursor() as cursor:
            admin_setting_check = f""" SELECT base_url FROM admin_setting """
            cursor.execute(admin_setting_check)
            admin_check = cursor.fetchone()
            return admin_check['base_url'] if admin_check is not None else ''

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_support_data():
    try:
        with getConnection().cursor() as cursor:
            admin_setting_check = f""" SELECT support_attributes FROM admin_setting """
            cursor.execute(admin_setting_check)
            admin_check = cursor.fetchone()
            return json.loads(admin_check['support_attributes']) if admin_check is not None else {}

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
