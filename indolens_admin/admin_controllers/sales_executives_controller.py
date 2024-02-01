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

def create_own_sales_executives(sales_executives, files):
    try:
        hashed_password = bcrypt.hashpw(sales_executives.password.encode('utf-8'), bcrypt.gensalt()).decode('utf_8')
        with connection.cursor() as cursor:
            insert_sales_executives_query = f"""
                INSERT INTO own_store_employees (
                   name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role,assigned_store_id
                ) VALUES (
                    '{sales_executives.name}', '{sales_executives.email}', '{sales_executives.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{sales_executives.address}', '{sales_executives.document_1_type}', 
                    '{json.dumps(files.document1)}', '{sales_executives.document_2_type}', '{json.dumps(files.document2)}', 0,
                    '{sales_executives.created_by}', '{getIndianTime()}', '{sales_executives.last_updated_by}', '{getIndianTime()}', 3, 0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_sales_executives_query)

            subject = email_template_controller.get_employee_creation_email_subject(sales_executives.name)
            body = email_template_controller.get_employee_creation_email_body(sales_executives.name, 'Sales Executive',
                                                                              sales_executives.email,
                                                                              sales_executives.password)
            send_notification_controller.send_email(subject, body, sales_executives.email)

            seId = cursor.lastrowid

            return {
                "status": True,
                "message": "Sales Executives added",
                "seId": seId
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def update_own_sales_executives(sales_executives, files):
    try:
        with connection.cursor() as cursor:
            update_sales_executives_query = f"""
                UPDATE own_store_employees
                SET 
                    name = '{sales_executives.name}',
                    email = '{sales_executives.email}',
                    phone = '{sales_executives.phone}',
                    {'profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    address = '{sales_executives.address}',
                    last_updated_by = '{sales_executives.last_updated_by}',
                    last_updated_on = '{getIndianTime()}'
                WHERE employee_id = {sales_executives.employee_id}
            """

            # Execute the update query using your cursor
            cursor.execute(update_sales_executives_query)

            return {
                "status": True,
                "message": "Sales Executives updated",
                "seId": sales_executives.id
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def update_franchise_sales_executives(sales_executives, files):
    try:
        with connection.cursor() as cursor:
            update_sales_executives_query = f"""
                UPDATE franchise_store_employees
                SET 
                    name = '{sales_executives.name}',
                    email = '{sales_executives.email}',
                    phone = '{sales_executives.phone}',
                    {'profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    address = '{sales_executives.address}',
                    last_updated_by = '{sales_executives.last_updated_by}',
                    last_updated_on = '{getIndianTime()}'
                WHERE employee_id = {sales_executives.employee_id}
            """

            # Execute the update query using your cursor
            cursor.execute(update_sales_executives_query)

            return {
                "status": True,
                "message": "Sales Executives updated",
                "seId": sales_executives.id
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def create_franchise_sales_executives(sales_executives, files):
    try:
        hashed_password = bcrypt.hashpw(sales_executives.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with connection.cursor() as cursor:
            insert_sales_executives_query = f"""
                INSERT INTO franchise_store_employees (
                   name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role,assigned_store_id
                ) VALUES (
                    '{sales_executives.name}', '{sales_executives.email}', '{sales_executives.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{sales_executives.address}', '{sales_executives.document_1_type}', 
                    '{json.dumps(files.document1)}', '{sales_executives.document_2_type}', '{json.dumps(files.document2)}', 0,
                    '{sales_executives.created_by}', '{getIndianTime()}', '{sales_executives.last_updated_by}', '{getIndianTime()}', 3,0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_sales_executives_query)

            subject = email_template_controller.get_employee_creation_email_subject(sales_executives.name)
            body = email_template_controller.get_employee_creation_email_body(sales_executives.name, 'Sales Executive',
                                                                              sales_executives.email,
                                                                              sales_executives.password)
            send_notification_controller.send_email(subject, body, sales_executives.email)

            seId = cursor.lastrowid

            return {
                "status": True,
                "message": "Sales Executives added",
                "franchiseSaleExecutivesId": seId
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_own_sales_executive(status):
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
                                            WHERE sm.role = 3 AND sm.status {status_condition}
                                            ORDER BY sm.employee_id DESC"""
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                "status": True,
                "sales_executive_list": get_own_store_employees(store_managers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_franchise_sales_executive(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name 
                                            FROM franchise_store_employees AS sm
                                            LEFT JOIN franchise_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id
                                            WHERE sm.role = 3 AND sm.status {status_condition}
                                            ORDER BY sm.employee_id DESC"""
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                "status": True,
                "franchise_sales_executive_list": get_own_store_employees(store_managers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_own_sales_executive_by_id(seId):
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id 
                                            WHERE sm.employee_id = '{seId}'"""
            cursor.execute(get_store_manager_query)
            store_manager = cursor.fetchall()
            return {
                "status": True,
                "sales_executive": get_own_store_employees(store_manager)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_sales_executive_by_id(seId):
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name 
                                            FROM franchise_store_employees AS sm
                                            LEFT JOIN franchise_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id 
                                            WHERE sm.employee_id = '{seId}'"""
            cursor.execute(get_store_manager_query)
            store_manager = cursor.fetchall()
            return {
                "status": True,
                "franchise_sales_executive": get_own_store_employees(store_manager)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_sales_executive(seId, status):
    try:
        with connection.cursor() as cursor:
            update_sales_executive_query = f"""
                UPDATE own_store_employees
                SET
                    status = {status}
                WHERE
                    employee_id = {seId}
            """

            # Execute the update query using your cursor
            cursor.execute(update_sales_executive_query)

            return {
                "status": True,
                "message": "Sales Executive updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_franchise_sales_executive(seId, status):
    try:
        with connection.cursor() as cursor:
            update_sales_executive_query = f"""
                UPDATE franchise_store_employees
                SET 
                    status = {status}
                WHERE
                    employee_id = {seId}
            """

            # Execute the update query using your cursor
            cursor.execute(update_sales_executive_query)

            return {
                "status": True,
                "message": "Sales Executive updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def assign_store_own_store_sales_executive(empId, storeId):
    try:
        with connection.cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE own_store_employees
                SET
                    assigned_store_id = {storeId}
                WHERE
                    employee_id = {empId}
            """
            # Execute the update query using your cursor
            cursor.execute(update_store_manager_query)

            return {
                       "status": True,
                       "message": "Store assigned"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def unassign_store_own_store_sales_executive(empId, storeId):
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

            return {
                       "status": True,
                       "message": "Store un assigned"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


