import datetime
import json

import bcrypt
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_models.admin_resp_model.franchise_owner_resp_model import get_franchise_owners

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def create_franchise_owner(franchise_owner, files):
    try:
        hashed_password = bcrypt.hashpw(franchise_owner.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with getConnection().cursor() as cursor:
            insert_franchise_owner_query = f"""
                INSERT INTO franchise_store_employees (
                    fse_name, fse_email, fse_phone, fse_password, fse_profile_pic, 
                    fse_address, fse_document_1_type, fse_document_1_url, fse_document_2_type, fse_document_2_url, 
                    fse_status, fse_created_by, fse_created_on, fse_last_updated_by, fse_last_updated_on, fse_role, fse_assigned_store_id
                ) VALUES (  
                     '{franchise_owner.name}', '{franchise_owner.email}', '{franchise_owner.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{franchise_owner.address}', '{franchise_owner.document_1_type}', 
                    '{json.dumps(files.document1)}', '{franchise_owner.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{franchise_owner.created_by}', '{getIndianTime()}', '{franchise_owner.last_updated_by}', 
                    '{getIndianTime()}', 1,0
                )
            """

            cursor.execute(insert_franchise_owner_query)

            subject = email_template_controller.get_franchise_employee_creation_email_subject(franchise_owner.name)
            body = email_template_controller.get_franchise_employee_creation_email_body(franchise_owner.name, 'Franchise Owner',
                                                                              franchise_owner.email,
                                                                              franchise_owner.password)
            send_notification_controller.send_email(subject, body, franchise_owner.email)

            foid = cursor.lastrowid

            return {
                "status": True,
                "message": "franchise owner added",
                "franchiseOwnersId": foid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_franchise_owner(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_all_franchise_owner_query = f""" SELECT fse.*, fs.fs_store_name, creator.admin_name, updater.admin_name 
                                            FROM franchise_store_employees AS fse
                                            LEFT JOIN franchise_store AS fs ON fse.fse_assigned_store_id = fs.fs_store_id
                                            LEFT JOIN admin AS creator ON fse.fse_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON fse.fse_last_updated_by = updater.admin_admin_id 
                                            WHERE fse.fse_role = 1 AND fse.fse_status {status_condition}
                                            ORDER BY fse.fse_employee_id DESC"""
            cursor.execute(get_all_franchise_owner_query)
            franchise_owners = cursor.fetchall()
            return {
                "status": True,
                "franchise_owners": franchise_owners
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_owner_by_id(foid):
    try:
        with getConnection().cursor() as cursor:
            get_all_franchise_owner_query = f""" SELECT fse.*, fs.fs_store_name, creator.admin_name AS creator,
                                            updater.admin_name AS updater
                                            FROM franchise_store_employees AS fse
                                            LEFT JOIN franchise_store AS fs ON fse.fse_assigned_store_id = fs.fs_store_id
                                            LEFT JOIN admin AS creator ON fse.fse_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON fse.fse_last_updated_by = updater.admin_admin_id
                                             WHERE fse.fse_employee_id = '{foid}'"""
            cursor.execute(get_all_franchise_owner_query)
            franchise_owners = cursor.fetchone()

            franchise_owners['fse_document_1_url'] = json.loads(franchise_owners['fse_document_1_url']) if franchise_owners[
                'fse_document_1_url'] else []
            franchise_owners['fse_document_2_url'] = json.loads(franchise_owners['fse_document_2_url']) if franchise_owners[
                'fse_document_2_url'] else []

            return {
                "status": True,
                "franchise_owner": franchise_owners
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_franchise_owner(foid, status):
    try:
        with getConnection().cursor() as cursor:
            update_franchise_owners_query = f"""
                UPDATE franchise_store_employees
                SET
                    fse_status = {status}
                WHERE
                    fse_employee_id = {foid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_franchise_owners_query)

            return {
                "status": True,
                "message": "franchise owner updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_franchise_owner(franchise_owner, files):
    try:
        with getConnection().cursor() as cursor:
            update_franchise_owners_query = f"""
                UPDATE franchise_store_employees
                SET 
                    fse_name = '{franchise_owner.name}',
                    fse_email = '{franchise_owner.email}',
                    fse_phone = '{franchise_owner.phone}',
                    {'fse_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    fse_address = '{franchise_owner.address}',
                    fse_last_updated_by = '{franchise_owner.last_updated_by}',
                    fse_last_updated_on = '{getIndianTime()}'
                WHERE fse_employee_id = {franchise_owner.employee_id}
            """

            # Execute the update query using your cursor
            cursor.execute(update_franchise_owners_query)

            return {
                "status": True,
                "message": "franchise owner updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def assign_store_franchise_owner(empId, storeId, role):
    try:
        with getConnection().cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE franchise_store_employees
                SET
                    assigned_store_id = {storeId}
                WHERE
                    employee_id = {empId}
            """
            # Execute the update query using your cursor
            cursor.execute(update_store_manager_query)

            get_employee_query = f""" SELECT name,email,phone FROM franchise_store_employees WHERE employee_id = {empId}
                                                """
            # Execute the update query using your cursor
            cursor.execute(get_employee_query)
            manager_data = cursor.fetchone()

            get_store_query = f""" SELECT store_name, store_phone, store_address FROM franchise_store 
                                                                        WHERE store_id = {storeId}"""

            cursor.execute(get_store_query)
            store_data = cursor.fetchone()

            subject = email_template_controller.get_employee_assigned_store_email_subject(manager_data[0])
            body = email_template_controller.get_employee_assigned_store_email_body(manager_data[0], 'Franchise Owner',
                                                                                    manager_data[1],
                                                                                    store_data[0],
                                                                                    store_data[1], store_data[2])

            send_notification_controller.send_email(subject, body, manager_data[1])

            return {
                "status": True,
                "message": "Store assigned"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def unassign_store_franchise_owner(FranchiseOwnerId, storeId, role):
    try:
        with getConnection().cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE franchise_store_employees
                SET
                    assigned_store_id = 0
                WHERE
                    employee_id = {FranchiseOwnerId}
            """
            # Execute the update query using your cursor
            cursor.execute(update_store_manager_query)

            get_employee_query = f""" SELECT name,email,phone FROM franchise_store_employees WHERE employee_id = {FranchiseOwnerId}
                                                            """
            # Execute the update query using your cursor
            cursor.execute(get_employee_query)
            manager_data = cursor.fetchone()

            get_store_query = f""" SELECT store_name, store_phone, store_address FROM franchise_store 
                                                                                    WHERE store_id = {storeId}"""

            cursor.execute(get_store_query)
            store_data = cursor.fetchone()

            subject = email_template_controller.get_employee_unassigned_store_email_subject(manager_data[0])
            body = email_template_controller.get_employee_unassigned_store_email_body(manager_data[0],
                                                                                      'Sales Executive',
                                                                                      manager_data[1], store_data[0],
                                                                                      store_data[1], store_data[2])

            send_notification_controller.send_email(subject, body, manager_data[1])

            return {
                       "status": True,
                       "message": "Store un assigned"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_active_franchise_stores():
    try:
        with getConnection().cursor() as cursor:
            get_unassigned_active_own_store_for_manager_query = f"""SELECT fs.fs_store_id AS store_id, 
            fs.fs_store_name AS store_name FROM franchise_store fs 
            WHERE fs.fs_status = 1;"""
            cursor.execute(get_unassigned_active_own_store_for_manager_query)
            unassigned_stores = cursor.fetchall()

            return {
                       "status": True,
                       "available_stores": unassigned_stores
                   }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_active_unassigned_franchise_stores():
    try:
        with getConnection().cursor() as cursor:
            unassigned_stores = []
            get_unassigned_active_own_store_for_manager_query = f"""SELECT f.fs_store_id AS store_id, 
                    f.fs_store_name AS store_name FROM franchise_store f 
                    LEFT JOIN franchise_store_employees fse ON f.fs_store_id = fse.fse_assigned_store_id AND fse.fse_role = 1
                    WHERE fse.fse_assigned_store_id IS NULL AND f.fs_status = 1 """
            cursor.execute(get_unassigned_active_own_store_for_manager_query)
            unassigned_stores = cursor.fetchall()
            return {
                       "status": True,
                       "available_stores": unassigned_stores
                   }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301