import datetime
import json

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_models.admin_resp_model.own_store_emp_resp_model import get_own_store_employees

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def create_other_employee(other_emp, files):
    try:
        hashed_password = bcrypt.hashpw(other_emp.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with connection.cursor() as cursor:
            insert_other_emp_query = f"""
                INSERT INTO own_store_employees (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role,assigned_store_id
                ) VALUES (
                    '{other_emp.name}', '{other_emp.email}', '{other_emp.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{other_emp.address}', '{other_emp.document_1_type}', 
                    '{json.dumps(files.document1)}', '{other_emp.document_2_type}', '{json.dumps(files.document2)}', 
                    0, '{other_emp.created_by}', '{getIndianTime()}', '{other_emp.last_updated_by}', '{getIndianTime()}', 4,0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_other_emp_query)
            empid = cursor.lastrowid

            subject = email_template_controller.get_employee_creation_email_subject(other_emp.name)
            body = email_template_controller.get_store_employee_creation_email_body(other_emp.name, 'Store Employee',
                                                                              other_emp.email)
            send_notification_controller.send_email(subject, body, other_emp.email)

            return {
                "status": True,
                "message": "Employee added",
                "empid": empid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def update_other_employee(other_emp, files):
    try:
        with connection.cursor() as cursor:
            update_other_emp_query = f"""
                UPDATE own_store_employees
                SET 
                    name = '{other_emp.name}',
                    email = '{other_emp.email}',
                    phone = '{other_emp.phone}',
                    {'profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    address = '{other_emp.address}',
                    last_updated_by = '{other_emp.last_updated_by}',
                    last_updated_on = '{getIndianTime()}'
                WHERE employee_id = {other_emp.employee_id}
            """

            # Execute the update query using your cursor
            cursor.execute(update_other_emp_query)

            return {
                "status": True,
                "message": "Employee updated",
                "empid": other_emp.id
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def update_franchise_other_employee(other_emp, files):
    try:
        with connection.cursor() as cursor:
            update_other_emp_query = f"""
                UPDATE franchise_store_employees
                SET 
                    name = '{other_emp.name}',
                    email = '{other_emp.email}',
                    phone = '{other_emp.phone}',
                    {'profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    address = '{other_emp.address}',
                    last_updated_by = '{other_emp.last_updated_by}',
                    last_updated_on = '{getIndianTime()}'
                WHERE employee_id = {other_emp.employee_id}
            """
            # Execute the update query using your cursor
            cursor.execute(update_other_emp_query)

            return {
                "status": True,
                "message": "Employee updated",
                "empid": other_emp.id
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def create_franchise_other_employee(other_emp, files):
    try:
        hashed_password = bcrypt.hashpw(other_emp.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with connection.cursor() as cursor:
            insert_other_emp_query = f"""
                INSERT INTO franchise_store_employees (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role, assigned_store_id
                ) VALUES (
                    '{other_emp.name}', '{other_emp.email}', '{other_emp.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{other_emp.address}', '{other_emp.document_1_type}', 
                    '{json.dumps(files.document1)}', '{other_emp.document_2_type}', '{json.dumps(files.document2)}', 
                    0, '{other_emp.created_by}', '{getIndianTime()}', '{other_emp.last_updated_by}', '{getIndianTime()}', 4,0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_other_emp_query)
            empid = cursor.lastrowid

            subject = email_template_controller.get_lab_tech_creation_email_subject(other_emp.name)
            body = email_template_controller.get_store_employee_creation_email_body(other_emp.name, 'Lab Technician',
                                                                              other_emp.email)
            send_notification_controller.send_email(subject, body, other_emp.email)

            return {
                "status": True,
                "message": "Employee added",
                "empid": empid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_other_emp(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT op.*, os.store_name, creator.name, updater.name 
                                            FROM own_store_employees AS op
                                            LEFT JOIN own_store AS os ON op.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON op.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON op.last_updated_by = updater.admin_id
                                            WHERE op.role = 4 AND op.status {status_condition} 
                                            ORDER BY op.employee_id DESC"""
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                "status": True,
                "other_emp_list": get_own_store_employees(store_managers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_franchise_other_emp(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT op.*, os.store_name, creator.name, updater.name 
                                            FROM franchise_store_employees AS op
                                            LEFT JOIN franchise_store AS os ON op.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON op.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON op.last_updated_by = updater.admin_id
                                            WHERE op.role = 4 AND op.status {status_condition} 
                                            ORDER BY op.employee_id DESC"""
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                "status": True,
                "other_emp_list": get_own_store_employees(store_managers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_other_emp_by_id(empid):
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT foe.*, os.store_name, creator.name, updater.name 
                                            FROM own_store_employees AS foe
                                            LEFT JOIN own_store AS os ON foe.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON foe.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON foe.last_updated_by = updater.admin_id 
                                            WHERE foe.employee_id = '{empid}'"""
            cursor.execute(get_store_manager_query)
            store_manager = cursor.fetchall()
            return {
                "status": True,
                "other_employee": get_own_store_employees(store_manager)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_other_emp_by_id(empid):
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT foe.*, os.store_name, creator.name, updater.name 
                                            FROM franchise_store_employees AS foe
                                            LEFT JOIN franchise_store AS os ON foe.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON foe.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON foe.last_updated_by = updater.admin_id 
                                            WHERE foe.employee_id = '{empid}'"""
            cursor.execute(get_store_manager_query)
            store_manager = cursor.fetchall()
            return {
                "status": True,
                "other_employee": get_own_store_employees(store_manager)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_other_employees(empid, status):
    try:
        with connection.cursor() as cursor:
            update_other_employees_query = f"""
                UPDATE own_store_employees
                SET
                    status = {status}
                WHERE
                    employee_id = {empid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_other_employees_query)

            return {
                "status": True,
                "message": "Employee updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_franchise_other_employees(empid, status):
    try:
        with connection.cursor() as cursor:
            update_other_employees_query = f"""
                UPDATE franchise_store_employees
                SET
                    status = {status}
                WHERE
                    employee_id = {empid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_other_employees_query)

            return {
                "status": True,
                "message": "Employee updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def assign_store_own_store_other_employee(empId, storeId):
    try:
        with connection.cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    assigned_store_id = {storeId}
                WHERE
                    employee_id = {empId}
            """
            cursor.execute(update_store_manager_query)

            get_employee_query = f""" SELECT name,email,phone FROM own_store_employees WHERE employee_id = {empId}
                                                """
            # Execute the update query using your cursor
            cursor.execute(get_employee_query)
            manager_data = cursor.fetchone()

            get_store_query = f""" SELECT store_name, store_phone, store_address FROM own_store 
                                                                        WHERE store_id = {storeId}"""

            cursor.execute(get_store_query)
            store_data = cursor.fetchone()

            subject = email_template_controller.get_employee_assigned_store_email_subject(manager_data[0])
            body = email_template_controller.get_employee_assigned_store_email_body(manager_data[0], 'Store Employee',
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


def unassign_store_own_store_other_employee(empId, storeId):
    try:
        with connection.cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    assigned_store_id = 0
                WHERE
                    employee_id = {empId}
            """
            # Execute the update query using your cursor
            cursor.execute(update_store_manager_query)

            get_employee_query = f""" SELECT name,email,phone FROM own_store_employees WHERE employee_id = {empId}
                                                """
            # Execute the update query using your cursor
            cursor.execute(get_employee_query)
            manager_data = cursor.fetchone()

            get_store_query = f""" SELECT store_name, store_phone, store_address FROM own_store 
                                                                        WHERE store_id = {storeId}"""

            cursor.execute(get_store_query)
            store_data = cursor.fetchone()

            subject = email_template_controller.get_employee_unassigned_store_email_subject(manager_data[0])
            body = email_template_controller.get_employee_unassigned_store_email_body(manager_data[0], 'Store Employee',
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
