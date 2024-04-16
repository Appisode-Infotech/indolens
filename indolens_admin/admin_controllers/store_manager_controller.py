import datetime
import json
import bcrypt

import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_controllers import send_notification_controller, email_template_controller
from indolens_admin.admin_models.admin_resp_model.own_store_emp_resp_model import get_own_store_employees

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def create_store_manager(store_manager, files):
    try:
        hashed_password = bcrypt.hashpw(store_manager.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with getConnection().cursor() as cursor:
            insert_store_manager_query = f"""
                INSERT INTO own_store_employees (
                    ose_name, ose_email, ose_phone, ose_password, ose_profile_pic, 
                    ose_assigned_store_id, ose_address, ose_document_1_type, ose_document_1_url, 
                    ose_document_2_type, ose_document_2_url, ose_status, ose_created_by, ose_created_on, 
                    ose_last_updated_by, ose_last_updated_on, ose_role
                ) VALUES (
                    '{store_manager.name}', '{store_manager.email}', '{store_manager.phone}', '{hashed_password}', 
                    '{files.profile_pic}', 0, '{store_manager.address}', 
                    '{store_manager.document_1_type}', '{json.dumps(files.document1)}', 
                    '{store_manager.document_2_type}', '{json.dumps(files.document2)}', 1, '{store_manager.created_by}', 
                    '{getIndianTime()}', '{store_manager.last_updated_by}', '{getIndianTime()}', 1
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_store_manager_query)
            mid = cursor.lastrowid

            subject = email_template_controller.get_employee_creation_email_subject(store_manager.name)
            body = email_template_controller.get_employee_creation_email_body(store_manager.name, 'Manager',
                                                                              store_manager.email,
                                                                              store_manager.password)
            send_notification_controller.send_email(subject, body, store_manager.email)

            return {
                "status": True,
                "message": "sub admin added",
                "mid": mid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def update_store_manager(store_manager, files):
    try:
        with getConnection().cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    ose_name = '{store_manager.name}',
                    ose_email = '{store_manager.email}',
                    ose_phone = '{store_manager.phone}',
                    {'ose_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    ose_address = '{store_manager.address}',
                    ose_last_updated_by = '{store_manager.last_updated_by}',
                    ose_last_updated_on = '{getIndianTime()}'
                WHERE ose_employee_id = {store_manager.employee_id} 
            """
            cursor.execute(update_store_manager_query)

            subject = email_template_controller.get_employee_update_email_subject(store_manager.name)
            body = email_template_controller.get_employee_update_email_body(store_manager.name, 'Manager',
                                                                            store_manager.email, store_manager.phone,
                                                                            store_manager.address)
            send_notification_controller.send_email(subject, body, store_manager.email)

            return {
                "status": True,
                "message": "store manager updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_store_manager(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.os_store_name AS store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.ose_assigned_store_id = os.os_store_id
                                            LEFT JOIN admin AS creator ON sm.ose_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON sm.ose_last_updated_by = updater.admin_admin_id
                                            WHERE sm.ose_role = 1 AND sm.ose_status {status_condition} 
                                            ORDER BY sm.ose_employee_id DESC"""
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                "status": True,
                "store_managers": store_managers
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_store_manager_by_id(mid):
    try:
        with getConnection().cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.os_store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.ose_assigned_store_id = os.os_store_id
                                            LEFT JOIN admin AS creator ON sm.ose_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON sm.ose_last_updated_by = updater.admin_admin_id 
                                            WHERE sm.ose_employee_id = {mid} """
            cursor.execute(get_store_manager_query)
            store_manager = cursor.fetchone()

            store_manager['ose_document_1_url'] = json.loads(store_manager['ose_document_1_url']) if store_manager['ose_document_1_url'] else []
            store_manager['ose_document_2_url'] = json.loads(store_manager['ose_document_2_url']) if store_manager['ose_document_2_url'] else []
            return {
                "status": True,
                "store_manager": store_manager
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_store_manager(mid, status):
    try:
        with getConnection().cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    ose_status = {status}
                WHERE
                    ose_employee_id = {mid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_store_manager_query)

            return {
                "status": True,
                "message": "Store Manager updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def assignStore(empId, storeId, role):
    try:
        with getConnection().cursor() as cursor:
            assign_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    ose_assigned_store_id = {storeId}
                WHERE
                    ose_employee_id = {empId}
            """
            # Execute the update query using your cursor
            cursor.execute(assign_store_manager_query)

            get_employee_query = f""" SELECT ose_name, ose_email, ose_phone 
                                    FROM own_store_employees WHERE ose_employee_id = {empId} """

            # Execute the update query using your cursor
            cursor.execute(get_employee_query)
            manager_data = cursor.fetchone()

            get_store_query = f""" SELECT os_store_name, os_store_phone, os_store_address FROM own_store 
                                    WHERE os_store_id = {storeId}"""

            cursor.execute(get_store_query)
            store_data = cursor.fetchone()

            subject = email_template_controller.get_employee_assigned_store_email_subject(manager_data[0])
            body = email_template_controller.get_employee_assigned_store_email_body(manager_data['ose_name'], role,
                                                                                    manager_data['ose_email'],
                                                                                    store_data['os_store_name'],
                                                                                    store_data['os_store_phone'],
                                                                                    store_data['os_store_address'])

            send_notification_controller.send_email(subject, body, manager_data[1])

            return {
                "status": True,
                "message": "Store assigned"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def unAssignStore(empId, storeId, role):
    try:
        with getConnection().cursor() as cursor:
            unassign_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    ose_assigned_store_id = 0
                WHERE
                    ose_employee_id = {empId}
            """
            # Execute the update query using your cursor
            cursor.execute(unassign_store_manager_query)
            get_employee_query = f""" SELECT ose_name,ose_email,ose_phone 
            FROM own_store_employees WHERE ose_employee_id = {empId}
                        """
            # Execute the update query using your cursor
            cursor.execute(get_employee_query)
            manager_data = cursor.fetchone()

            get_store_query = f""" SELECT os_store_name, os_store_phone, os_store_address FROM own_store 
                                                WHERE os_store_id = {storeId}"""

            cursor.execute(get_store_query)
            store_data = cursor.fetchone()

            subject = email_template_controller.get_employee_unassigned_store_email_subject(manager_data[0])
            body = email_template_controller.get_employee_unassigned_store_email_body(manager_data['ose_name'], role,
                                                                                    manager_data['ose_email'],
                                                                                    store_data['os_store_name'],
                                                                                    store_data['os_store_phone'],
                                                                                    store_data['os_store_address'])

            send_notification_controller.send_email(subject, body, manager_data['ose_email'])

            return {
                "status": True,
                "message": "Store un assigned"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
