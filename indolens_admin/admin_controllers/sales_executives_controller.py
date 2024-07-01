import datetime
import json

import bcrypt
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_models.admin_resp_model.own_store_emp_resp_model import get_own_store_employees

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def create_own_sales_executives(sales_executives, files):
    try:
        hashed_password = bcrypt.hashpw(sales_executives.password.encode('utf-8'), bcrypt.gensalt()).decode('utf_8')
        with getConnection().cursor() as cursor:
            insert_sales_executives_query = f"""
                INSERT INTO own_store_employees (
                    ose_name, ose_email, ose_phone, ose_password, ose_profile_pic, 
                    ose_address, ose_document_1_type, ose_document_1_url, 
                    ose_document_2_type, ose_document_2_url, ose_status, ose_created_by, ose_created_on, 
                    ose_last_updated_by, ose_last_updated_on, ose_role, ose_assigned_store_id
                ) VALUES (
                    '{sales_executives.name}', '{sales_executives.email}', '{sales_executives.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{sales_executives.address}', '{sales_executives.document_1_type}', 
                    '{json.dumps(files.document1)}', '{sales_executives.document_2_type}', '{json.dumps(files.document2)}', 1,
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
        with getConnection().cursor() as cursor:
            update_sales_executives_query = f"""
                UPDATE own_store_employees
                SET 
                    ose_name = '{sales_executives.name}',
                    ose_email = '{sales_executives.email}',
                    ose_phone = '{sales_executives.phone}',
                    {'ose_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    ose_address = '{sales_executives.address}',
                    ose_last_updated_by = '{sales_executives.last_updated_by}',
                    ose_last_updated_on = '{getIndianTime()}'
                WHERE ose_employee_id = {sales_executives.employee_id}
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
        with getConnection().cursor() as cursor:
            update_sales_executives_query = f"""
                UPDATE franchise_store_employees
                SET 
                    fse_name = '{sales_executives.name}',
                    fse_email = '{sales_executives.email}',
                    fse_phone = '{sales_executives.phone}',
                    {'fse_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    fse_address = '{sales_executives.address}',
                    fse_last_updated_by = '{sales_executives.last_updated_by}',
                    fse_last_updated_on = '{getIndianTime()}'
                WHERE fse_employee_id = {sales_executives.employee_id}
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
        with getConnection().cursor() as cursor:
            insert_sales_executives_query = f"""
                INSERT INTO franchise_store_employees (
                   fse_name, fse_email, fse_phone, fse_password, fse_profile_pic, 
                    fse_address, fse_document_1_type, fse_document_1_url, 
                    fse_document_2_type, fse_document_2_url, fse_status, fse_created_by, fse_created_on, 
                    fse_last_updated_by, fse_last_updated_on, fse_role,fse_assigned_store_id
                ) VALUES (
                    '{sales_executives.name}', '{sales_executives.email}', '{sales_executives.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{sales_executives.address}', '{sales_executives.document_1_type}', 
                    '{json.dumps(files.document1)}', '{sales_executives.document_2_type}', '{json.dumps(files.document2)}', 1,
                    '{sales_executives.created_by}', '{getIndianTime()}', '{sales_executives.last_updated_by}', '{getIndianTime()}', 3,0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_sales_executives_query)

            subject = email_template_controller.get_franchise_employee_creation_email_subject(sales_executives.name)
            body = email_template_controller.get_franchise_employee_creation_email_body(sales_executives.name, 'Sales Executive',
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
        with getConnection().cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.os_store_name AS store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.ose_assigned_store_id = os.os_store_id
                                            LEFT JOIN admin AS creator ON sm.ose_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON sm.ose_last_updated_by = updater.admin_admin_id
                                            WHERE sm.ose_role = 3 AND sm.ose_status {status_condition}
                                            ORDER BY sm.ose_employee_id DESC"""
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                "status": True,
                "sales_executive_list": store_managers
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
        with getConnection().cursor() as cursor:
            get_store_manager_query = f""" SELECT fse.*, fs.fs_store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater
                                            FROM franchise_store_employees AS fse
                                            LEFT JOIN franchise_store AS fs ON fse.fse_assigned_store_id = fs.fs_store_id
                                            LEFT JOIN admin AS creator ON fse.fse_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON fse.fse_last_updated_by = updater.admin_admin_id
                                            WHERE fse.fse_role = 3 AND fse.fse_status {status_condition}
                                            ORDER BY fse.fse_employee_id DESC"""
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                "status": True,
                "franchise_sales_executive_list": store_managers
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_own_sales_executive_by_id(seId):
    try:
        with getConnection().cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.os_store_name AS store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.ose_assigned_store_id = os.os_store_id
                                            LEFT JOIN admin AS creator ON sm.ose_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON sm.ose_last_updated_by = updater.admin_admin_id
                                            WHERE sm.ose_employee_id = '{seId}'"""
            cursor.execute(get_store_manager_query)
            store_manager = cursor.fetchone()
            store_manager['ose_document_1_url'] = json.loads(store_manager['ose_document_1_url']) if store_manager[
                'ose_document_1_url'] else []
            store_manager['ose_document_2_url'] = json.loads(store_manager['ose_document_2_url']) if store_manager[
                'ose_document_2_url'] else []
            return {
                "status": True,
                "sales_executive": store_manager
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_sales_executive_by_id(seId):
    try:
        with getConnection().cursor() as cursor:
            get_sales_executive_query = f""" SELECT fse.*, fs.fs_store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater
                                            FROM franchise_store_employees AS fse
                                            LEFT JOIN franchise_store AS fs ON fse.fse_assigned_store_id = fs.fs_store_id
                                            LEFT JOIN admin AS creator ON fse.fse_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON fse.fse_last_updated_by = updater.admin_admin_id 
                                            WHERE fse.fse_employee_id = '{seId}'"""
            cursor.execute(get_sales_executive_query)
            sales_executive = cursor.fetchone()
            sales_executive['fse_document_1_url'] = json.loads(sales_executive['fse_document_1_url']) if \
            sales_executive['fse_document_1_url'] else []
            sales_executive['fse_document_2_url'] = json.loads(sales_executive['fse_document_2_url']) if \
            sales_executive['fse_document_2_url'] else []

            return {
                "status": True,
                "franchise_sales_executive": sales_executive
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_sales_executive(seId, status):
    try:
        with getConnection().cursor() as cursor:
            update_sales_executive_query = f"""
                UPDATE own_store_employees
                SET
                    ose_status = {status}
                WHERE
                    ose_employee_id = {seId}
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
        with getConnection().cursor() as cursor:
            update_sales_executive_query = f"""
                UPDATE franchise_store_employees
                SET 
                    fse_status = {status}
                WHERE
                    fse_employee_id = {seId}
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

            subject = email_template_controller.get_employee_assigned_store_email_subject(manager_data['ose_name'])
            body = email_template_controller.get_employee_assigned_store_email_body(manager_data['ose_name'], 'Sales Executive',
                                                                                    manager_data['ose_email'],
                                                                                    store_data['os_store_name'],
                                                                                    store_data['os_store_phone'],
                                                                                    store_data['os_store_address'])

            send_notification_controller.send_email(subject, body, manager_data['ose_email'])

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

            subject = email_template_controller.get_employee_unassigned_store_email_subject(manager_data['ose_name'])
            body = email_template_controller.get_employee_unassigned_store_email_body(manager_data['ose_name'], 'Sales Executive',
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


