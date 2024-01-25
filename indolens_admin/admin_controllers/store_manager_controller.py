import datetime
import json
import bcrypt

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_controllers import send_notification_controller, email_template_controller
from indolens_admin.admin_models.admin_resp_model.own_store_emp_resp_model import get_own_store_employees

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_store_manager(store_manager, files):
    try:
        hashed_password = bcrypt.hashpw(store_manager.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with connection.cursor() as cursor:
            insert_store_manager_query = f"""
                INSERT INTO own_store_employees (
                    name, email, phone, password, profile_pic, 
                    assigned_store_id, address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role
                ) VALUES (
                    '{store_manager.name}', '{store_manager.email}', '{store_manager.phone}', '{hashed_password}', 
                    '{files.profile_pic}', 0, '{store_manager.address}', 
                    '{store_manager.document_1_type}', '{json.dumps(files.document1)}', 
                    '{store_manager.document_2_type}', '{json.dumps(files.document2)}', 1, '{store_manager.created_by}', 
                    '{today}', '{store_manager.last_updated_by}', '{today}', 1
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_store_manager_query)
            subject = email_template_controller.get_employee_creation_email_subject()
            body = email_template_controller.get_employee_creation_email_body(store_manager.name, 'Manager',
                                                                              store_manager.email,
                                                                              store_manager.password)
            send_notification_controller.send_email(subject, body, store_manager.email)

            mid = cursor.lastrowid
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
        with connection.cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    name = '{store_manager.name}',
                    email = '{store_manager.email}',
                    phone = '{store_manager.phone}',
                    {'profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    address = '{store_manager.address}',
                    last_updated_by = '{store_manager.last_updated_by}',
                    last_updated_on = '{today}'
                WHERE employee_id = {store_manager.employee_id} 
            """
            print(update_store_manager_query)
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
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id
                                            WHERE sm.role = 1 AND sm.status {status_condition} 
                                            ORDER BY sm.employee_id DESC"""
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                "status": True,
                "store_managers": get_own_store_employees(store_managers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_store_manager_by_id(mid):
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id 
                                            WHERE sm.employee_id = {mid} """
            cursor.execute(get_store_manager_query)
            store_manager = cursor.fetchall()
            return {
                "status": True,
                "store_manager": get_own_store_employees(store_manager)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_store_manager(mid, status):
    try:
        with connection.cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    status = {status}
                WHERE
                    employee_id = {mid}
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


def assignStore(empId, storeId):
    try:
        with connection.cursor() as cursor:
            assign_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    assigned_store_id = {storeId}
                WHERE
                    employee_id = {empId}
            """
            # Execute the update query using your cursor
            cursor.execute(assign_store_manager_query)

            get_manager_query = f""" SELECT name,email,phone FROM own_store_employees WHERE employee_id = {empId}
            """

            # Execute the update query using your cursor
            cursor.execute(get_manager_query)
            manager_data = cursor.fetchone()

            get_store_query = f""" SELECT store_name, store_phone, store_address FROM own_store 
                                    WHERE store_id = {storeId}"""

            cursor.execute(get_store_query)
            store_data = cursor.fetchone()

            subject = email_template_controller.get_employee_assigned_store_email_subject(manager_data[0])
            body = email_template_controller.get_employee_assigned_store_email_body(manager_data[0], 'Manager',
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


def unAssignStore(empId, storeId):
    try:
        with connection.cursor() as cursor:
            unassign_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    assigned_store_id = 0
                WHERE
                    employee_id = {empId}
            """
            # Execute the update query using your cursor
            cursor.execute(unassign_store_manager_query)
            get_manager_query = f""" SELECT name,email,phone FROM own_store_employees WHERE employee_id = {empId}
                        """

            # Execute the update query using your cursor
            cursor.execute(get_manager_query)
            manager_data = cursor.fetchone()

            get_store_query = f""" SELECT store_name, store_phone, store_address FROM own_store 
                                                WHERE store_id = {storeId}"""

            cursor.execute(get_store_query)
            store_data = cursor.fetchone()

            subject = email_template_controller.get_employee_unassigned_store_email_subject(manager_data[0])
            body = email_template_controller.get_employee_unassigned_store_email_body(manager_data[0], 'Manager',
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
