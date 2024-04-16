import datetime
import json

import bcrypt
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_models.admin_resp_model.accountant_resp_model import get_accountants

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def create_accountant(accountant, files):
    try:
        hashed_password = bcrypt.hashpw(accountant.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with getConnection().cursor() as cursor:
            insert_accountant_query = f"""
                INSERT INTO accountant (
                    ac_name, ac_email, ac_phone, ac_password, ac_profile_pic, 
                    ac_address, ac_document_1_type, ac_document_1_url, ac_document_2_type, ac_document_2_url, 
                    ac_status, ac_created_by, ac_created_on, ac_last_updated_by, ac_last_updated_on
                ) VALUES (
                    '{accountant.name}', '{accountant.email}', '{accountant.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{accountant.address}', '{accountant.document_1_type}', 
                    '{json.dumps(files.document1)}', '{accountant.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{accountant.created_by}', '{getIndianTime()}', '{accountant.last_updated_by}', '{getIndianTime()}'
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_accountant_query)

            subject = email_template_controller.get_employee_creation_email_subject(accountant.name)
            body = email_template_controller.get_employee_creation_email_body(accountant.name, 'Accountant',
                                                                              accountant.email,
                                                                              accountant.password)
            send_notification_controller.send_email(subject, body, accountant.email)

            aid = cursor.lastrowid

            return {
                       "status": True,
                       "message": "Accountant Added",
                       "aid": aid
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_accountant(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_accountant_query = f"""
            SELECT ac.*, creator.admin_name AS creator_name, updater.admin_name AS updater_name
            FROM accountant AS ac
            LEFT JOIN admin AS creator ON ac.ac_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON ac.ac_last_updated_by = updater.admin_admin_id
            WHERE ac.ac_status {status_condition}
            GROUP BY ac.ac_accountant_id ORDER BY ac.ac_accountant_id DESC
            """
            cursor.execute(get_accountant_query)
            accountant = cursor.fetchall()

            return {
                       "status": True,
                       "accountant_list": accountant
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_accountant_by_id(aid):
    try:
        with getConnection().cursor() as cursor:
            get_accountant_query = f"""
                        SELECT ac.*, creator.admin_name AS creator_name, updater.admin_name AS updater_name
                        FROM accountant AS ac
                        LEFT JOIN admin AS creator ON ac.ac_created_by = creator.admin_admin_id
                        LEFT JOIN admin AS updater ON ac.ac_last_updated_by = updater.admin_admin_id
                        WHERE ac.ac_accountant_id = '{aid}'
                        GROUP BY ac.ac_accountant_id
                        """
            cursor.execute(get_accountant_query)
            accountant = cursor.fetchone()

            accountant['ac_document_1_url'] = json.loads(accountant['ac_document_1_url']) if accountant[
                'ac_document_1_url'] else []
            accountant['ac_document_2_url'] = json.loads(accountant['ac_document_2_url']) if accountant[
                'ac_document_2_url'] else []

            return {
                       "status": True,
                       "accountant": accountant
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_accountant(accountant_obj, files):
    try:
        with getConnection().cursor() as cursor:
            update_accountant_obj_query = f"""
                                UPDATE accountant
                                SET 
                                    ac_name = '{accountant_obj.name}',
                                    ac_email = '{accountant_obj.email}',
                                    ac_phone = '{accountant_obj.phone}',
                                    {'ac_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                                    ac_address = '{accountant_obj.address}',
                                    ac_last_updated_by = '{accountant_obj.last_updated_by}',
                                    ac_last_updated_on = '{getIndianTime()}'
                                WHERE ac_accountant_id = {accountant_obj.accountant_id}
                            """
            cursor.execute(update_accountant_obj_query)

            return {
                       "status": True,
                       "message": "Accountant updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_accountant(aid, status):
    try:
        with getConnection().cursor() as cursor:
            update_accountant_query = f"""
                UPDATE accountant
                SET
                    ac_status = {status}
                WHERE
                    ac_accountant_id = {aid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_accountant_query)

            return {
                       "status": True,
                       "message": "Accountant updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
