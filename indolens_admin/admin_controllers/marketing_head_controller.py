import datetime
import json

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_models.admin_resp_model.marketing_head_resp_model import get_marketing_heads

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def create_marketing_head(marketing_head, files):
    try:
        hashed_password = bcrypt.hashpw(marketing_head.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with connection.cursor() as cursor:
            insert_marketing_head_query = f"""
                INSERT INTO marketing_head (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, document_2_type, document_2_url, 
                    status, created_by, created_on, last_updated_by, last_updated_on, assigned_area_head	
                ) VALUES (
                    '{marketing_head.fullName}', '{marketing_head.email}', '{marketing_head.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{marketing_head.completeAddress}', '{marketing_head.document_1_type}', 
                    '{json.dumps(files.document1)}', '{marketing_head.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{marketing_head.created_by}', '{getIndianTime()}', '{marketing_head.last_updated_by}', '{getIndianTime()}', 0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_marketing_head_query)

            subject = email_template_controller.get_employee_creation_email_subject(marketing_head.fullName)
            body = email_template_controller.get_employee_creation_email_body(marketing_head.fullName, 'Marketing Head',
                                                                              marketing_head.email,
                                                                              marketing_head.password)
            send_notification_controller.send_email(subject, body, marketing_head.email)

            mhid = cursor.lastrowid

            return {
                       "status": True,
                       "message": "Marketing Head added",
                       "marketingHeadId": mhid
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_marketing_head(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with connection.cursor() as cursor:
            get_marketing_head_query = f"""
            SELECT mh.*, creator.name, updater.name, ah.name
            FROM marketing_head AS mh
            LEFT JOIN area_head AS ah ON mh.assigned_area_head = ah.area_head_id
            LEFT JOIN admin AS creator ON mh.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON mh.last_updated_by = updater.admin_id
            WHERE mh.status {status_condition}
            GROUP BY mh.marketing_head_id ORDER BY mh.marketing_head_id DESC
            """
            cursor.execute(get_marketing_head_query)
            marketing_head = cursor.fetchall()

            return {
                       "status": True,
                       "marketing_heads_list": get_marketing_heads(marketing_head)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_marketing_head_by_id(mhid):
    try:
        with connection.cursor() as cursor:
            get_marketing_head_query = f"""
            SELECT mh.*, creator.name, updater.name, ah.name
            FROM marketing_head AS mh
            LEFT JOIN area_head AS ah ON mh.assigned_area_head = ah.area_head_id
            LEFT JOIN admin AS creator ON mh.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON mh.last_updated_by = updater.admin_id
            WHERE marketing_head_id = '{mhid}'
            GROUP BY mh.marketing_head_id
            """
            cursor.execute(get_marketing_head_query)
            marketing_head = cursor.fetchall()

            return {
                       "status": True,
                       "marketing_head": get_marketing_heads(marketing_head)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def edit_marketing_head(marketing_head_obj, files):
    try:
        with connection.cursor() as cursor:
            update_marketing_head_obj_query = f"""
                                UPDATE marketing_head
                                SET 
                                    name = '{marketing_head_obj.fullName}',
                                    email = '{marketing_head_obj.email}',
                                    phone = '{marketing_head_obj.phone}',
                                    {'profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                                    address = '{marketing_head_obj.completeAddress}',
                                    last_updated_by = '{marketing_head_obj.last_updated_by}',
                                    last_updated_on = '{getIndianTime()}'
                                WHERE marketing_head_id = {marketing_head_obj.marketing_head_id}
                            """
            cursor.execute(update_marketing_head_obj_query)

            return {
                "status": True,
                "message": "Marketing Head updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_marketing_head(mhid, status):
    try:
        with connection.cursor() as cursor:
            update_marketing_head_query = f"""
                UPDATE marketing_head
                SET
                    status = {status}
                WHERE
                    marketing_head_id = {mhid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_marketing_head_query)

            return {
                       "status": True,
                       "message": "Marketing  Head updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
