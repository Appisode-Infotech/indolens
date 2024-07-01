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

def create_other_employee(other_emp, files):
    try:
        hashed_password = bcrypt.hashpw(other_emp.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with getConnection().cursor() as cursor:
            insert_other_emp_query = f"""
                INSERT INTO own_store_employees (
                    ose_name, ose_email, ose_phone, ose_password, ose_profile_pic, 
                    ose_address, ose_document_1_type, ose_document_1_url, 
                    ose_document_2_type, ose_document_2_url, ose_status, ose_created_by, ose_created_on, 
                    ose_last_updated_by, ose_last_updated_on, ose_role, ose_assigned_store_id
                ) VALUES (
                    '{other_emp.name}', '{other_emp.email}', '{other_emp.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{other_emp.address}', '{other_emp.document_1_type}', 
                    '{json.dumps(files.document1)}', '{other_emp.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{other_emp.created_by}', '{getIndianTime()}', '{other_emp.last_updated_by}', '{getIndianTime()}', 4,0
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
        with getConnection().cursor() as cursor:
            update_other_emp_query = f"""
                UPDATE own_store_employees
                SET 
                    ose_name = '{other_emp.name}',
                    ose_email = '{other_emp.email}',
                    ose_phone = '{other_emp.phone}',
                    {'ose_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    ose_address = '{other_emp.address}',
                    ose_last_updated_by = '{other_emp.last_updated_by}',
                    ose_last_updated_on = '{getIndianTime()}'
                WHERE ose_employee_id = {other_emp.employee_id}
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
        with getConnection().cursor() as cursor:
            update_other_emp_query = f"""
                UPDATE franchise_store_employees
                SET 
                    fse_name = '{other_emp.name}',
                    fse_email = '{other_emp.email}',
                    fse_phone = '{other_emp.phone}',
                    {'fse_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    fse_address = '{other_emp.address}',
                    fse_last_updated_by = '{other_emp.last_updated_by}',
                    fse_last_updated_on = '{getIndianTime()}'
                WHERE fse_employee_id = {other_emp.employee_id}
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
        with getConnection().cursor() as cursor:
            insert_other_emp_query = f"""
                INSERT INTO franchise_store_employees (
                    fse_name, fse_email, fse_phone, fse_password, fse_profile_pic, 
                    fse_address, fse_document_1_type, fse_document_1_url, 
                    fse_document_2_type, fse_document_2_url, fse_status, fse_created_by, fse_created_on, 
                    fse_last_updated_by, fse_last_updated_on, fse_role, fse_assigned_store_id
                ) VALUES (
                    '{other_emp.name}', '{other_emp.email}', '{other_emp.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{other_emp.address}', '{other_emp.document_1_type}', 
                    '{json.dumps(files.document1)}', '{other_emp.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{other_emp.created_by}', '{getIndianTime()}', '{other_emp.last_updated_by}', '{getIndianTime()}', 4,0
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
        with getConnection().cursor() as cursor:
            get_other_employee_query = f""" SELECT sm.*, os.os_store_name AS store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.ose_assigned_store_id = os.os_store_id
                                            LEFT JOIN admin AS creator ON sm.ose_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON sm.ose_last_updated_by = updater.admin_admin_id
                                            WHERE sm.ose_role = 4 AND sm.ose_status {status_condition} 
                                            ORDER BY sm.ose_employee_id DESC"""
            cursor.execute(get_other_employee_query)
            other_employees = cursor.fetchall()
            return {
                "status": True,
                "other_emp_list": other_employees
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
        with getConnection().cursor() as cursor:
            get_other_employee_query = f""" SELECT fse.*, fs.fs_store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater
                                            FROM franchise_store_employees AS fse
                                            LEFT JOIN franchise_store AS fs ON fse.fse_assigned_store_id = fs.fs_store_id
                                            LEFT JOIN admin AS creator ON fse.fse_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON fse.fse_last_updated_by = updater.admin_admin_id
                                            WHERE fse.fse_role = 4 AND fse.fse_status {status_condition} 
                                            ORDER BY fse.fse_employee_id DESC"""
            cursor.execute(get_other_employee_query)
            other_employees = cursor.fetchall()
            return {
                "status": True,
                "other_emp_list": other_employees
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_other_emp_by_id(empid):
    try:
        with getConnection().cursor() as cursor:
            get_other_employee_query = f""" SELECT sm.*, os.os_store_name AS store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.ose_assigned_store_id = os.os_store_id
                                            LEFT JOIN admin AS creator ON sm.ose_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON sm.ose_last_updated_by = updater.admin_admin_id
                                            WHERE sm.ose_employee_id = '{empid}'"""
            cursor.execute(get_other_employee_query)
            other_employee = cursor.fetchone()

            other_employee['ose_document_1_url'] = json.loads(other_employee['ose_document_1_url']) if other_employee[
                'ose_document_1_url'] else []
            other_employee['ose_document_2_url'] = json.loads(other_employee['ose_document_2_url']) if other_employee[
                'ose_document_2_url'] else []
            return {
                "status": True,
                "other_employee": other_employee
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_other_emp_by_id(empid):
    try:
        with getConnection().cursor() as cursor:
            get_other_employee_query = f""" SELECT fse.*, fs.fs_store_name, creator.admin_name AS creator, 
                                                        updater.admin_name AS updater
                                                        FROM franchise_store_employees AS fse
                                                        LEFT JOIN franchise_store AS fs ON fse.fse_assigned_store_id = fs.fs_store_id
                                                        LEFT JOIN admin AS creator ON fse.fse_created_by = creator.admin_admin_id
                                                        LEFT JOIN admin AS updater ON fse.fse_last_updated_by = updater.admin_admin_id
                                                        WHERE fse.fse_employee_id = '{empid}' 
                                                        ORDER BY fse.fse_employee_id DESC"""
            cursor.execute(get_other_employee_query)
            other_employee = cursor.fetchone()
            other_employee['fse_document_1_url'] = json.loads(other_employee['fse_document_1_url']) if other_employee[
                'fse_document_1_url'] else []
            other_employee['fse_document_2_url'] = json.loads(other_employee['fse_document_2_url']) if other_employee[
                'fse_document_2_url'] else []
            return {
                "status": True,
                "other_employee": other_employee
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_other_employees(empid, status):
    try:
        with getConnection().cursor() as cursor:
            update_other_employees_query = f"""
                UPDATE own_store_employees
                SET
                    ose_status = {status}
                WHERE
                    ose_employee_id = {empid}
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
        with getConnection().cursor() as cursor:
            update_other_employees_query = f"""
                UPDATE franchise_store_employees
                SET
                    fse_status = {status}
                WHERE
                    fse_employee_id = {empid}
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
            body = email_template_controller.get_employee_assigned_store_email_body(manager_data['ose_name'], 'Store Employee',
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


def unassign_store_own_store_other_employee(empId, storeId):
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
            body = email_template_controller.get_employee_unassigned_store_email_body(manager_data['ose_name'], 'Store Employee',
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
