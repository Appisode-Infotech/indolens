import datetime
import json

import bcrypt
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_models.admin_resp_model.sub_admin_resp_model import get_sub_admin

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def create_sub_admin(sub_admin, files):
    try:
        hashed_password = bcrypt.hashpw(sub_admin.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with getConnection().cursor() as cursor:
            insert_admin_query = f"""
                INSERT INTO admin (
                    admin_name, admin_email, admin_phone, admin_password, admin_role, admin_profile_pic, 
                    admin_address, admin_document_1_type, admin_document_1_url, admin_document_2_type, 
                    admin_document_2_url,  admin_status, admin_created_by, admin_created_on, admin_last_updated_by, 
                    admin_last_updated_on
                ) VALUES (
                    '{sub_admin.full_name}', '{sub_admin.email}', '{sub_admin.phone}', '{hashed_password}', 2, 
                    '{files.profile_pic}', '{sub_admin.complete_address}', '{sub_admin.document_1_type}', 
                    '{json.dumps(files.document1)}', '{sub_admin.document_2_type}', '{json.dumps(files.document2)}', 
                    1, {int(sub_admin.created_by)}, '{getIndianTime()}', {int(sub_admin.last_updated_by)}, '{getIndianTime()}'
                )
            """

            cursor.execute(insert_admin_query)

            subject = email_template_controller.get_employee_creation_email_subject(sub_admin.full_name)
            body = email_template_controller.get_employee_creation_email_body(sub_admin.full_name, 'Sub-Admin',
                                                                              sub_admin.email,
                                                                              sub_admin.password)
            send_notification_controller.send_email(subject, body, sub_admin.email)

            said = cursor.lastrowid

            return {
                       "status": True,
                       "message": "sub admin added",
                       "said": said
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_sub_admin(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_all_sub_admin_query = f""" SELECT a.*, creator.admin_name AS creator, updater.admin_name AS updater 
                                            FROM admin AS a
                                            LEFT JOIN admin AS creator ON a.admin_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON a.admin_last_updated_by = updater.admin_admin_id
                                            WHERE a.admin_role = 2 AND a.admin_status {status_condition}
                                            ORDER BY a.admin_admin_id DESC"""
            cursor.execute(get_all_sub_admin_query)
            sub_admins = cursor.fetchall()
            return {
                       "status": True,
                       "sub_admins": sub_admins
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_sub_admin_by_id(said):
    try:
        with getConnection().cursor() as cursor:
            get_sub_admin_query = f""" SELECT a.*, creator.admin_name AS creator, updater.admin_name AS updater 
                                                        FROM admin AS a
                                                        LEFT JOIN admin AS creator ON a.admin_created_by = creator.admin_admin_id
                                                        LEFT JOIN admin AS updater ON a.admin_last_updated_by = updater.admin_admin_id
                                                        WHERE a.admin_admin_id = {said} """
            cursor.execute(get_sub_admin_query)
            sub_admin = cursor.fetchone()
            sub_admin['admin_document_1_url'] = json.loads(sub_admin['admin_document_1_url']) if sub_admin[
                'admin_document_1_url'] else []
            sub_admin['admin_document_2_url'] = json.loads(sub_admin['admin_document_2_url']) if sub_admin[
                'admin_document_2_url'] else []

            return {
                       "status": True,
                       "sub_admin": sub_admin
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_sub_admin(sub_admin, files):
    try:
        with getConnection().cursor() as cursor:
            update_admin_query = f"""
                UPDATE admin
                SET
                    admin_name = '{sub_admin.full_name}',
                    admin_email = '{sub_admin.email}',
                    admin_phone = '{sub_admin.phone}',
                    {'admin_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    admin_address = '{sub_admin.complete_address}',
                    admin_last_updated_by = '{sub_admin.last_updated_by}',
                    admin_last_updated_on = '{getIndianTime()}'
                WHERE
                    admin_admin_id = {sub_admin.admin_id}
            """

            # Execute the update query using your cursor
            cursor.execute(update_admin_query)

            return {
                       "status": True,
                       "message": "sub admin updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_sub_admin(said, status):
    try:
        with getConnection().cursor() as cursor:
            update_sub_admin_query = f"""
                UPDATE admin
                SET
                    admin_status = {status}
                WHERE
                    admin_admin_id = {said}
            """

            # Execute the update query using your cursor
            cursor.execute(update_sub_admin_query)

            return {
                       "status": True,
                       "message": "Sub Admin updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
