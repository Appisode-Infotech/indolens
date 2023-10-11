import datetime
import json

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.other_emp_resp_model import get_other_employees
from indolens_admin.admin_models.admin_resp_model.own_store_emp_resp_model import get_own_store_employees

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_other_employee(other_emp, files):
    try:
        with connection.cursor() as cursor:
            insert_other_emp_query = f"""
                INSERT INTO own_store_employees (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role
                ) VALUES (
                    '{other_emp.name}', '{other_emp.email}', '{other_emp.phone}', '{other_emp.password}',
                    '{files.profile_pic}', '{other_emp.address}', '{other_emp.document_1_type}', 
                    '{json.dumps(files.document1)}', '{other_emp.document_2_type}', '{json.dumps(files.document2)}', 
                    0, '{other_emp.created_by}', '{today}', '{other_emp.last_updated_by}', '{today}', 4
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_other_emp_query)
            empid = cursor.lastrowid

            return {
                "status": True,
                "message": "Employee added",
                "empid": empid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def create_franchise_other_employee(other_emp, files):
    try:
        with connection.cursor() as cursor:
            insert_other_emp_query = f"""
                INSERT INTO franchise_store_employees (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role
                ) VALUES (
                    '{other_emp.name}', '{other_emp.email}', '{other_emp.phone}', '{other_emp.password}',
                    '{files.profile_pic}', '{other_emp.address}', '{other_emp.document_1_type}', 
                    '{json.dumps(files.document1)}', '{other_emp.document_2_type}', '{json.dumps(files.document2)}', 
                    0, '{other_emp.created_by}', '{today}', '{other_emp.last_updated_by}', '{today}', 4
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_other_emp_query)
            empid = cursor.lastrowid

            return {
                "status": True,
                "message": "Employee added",
                "seid": empid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_other_emp():
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT op.*, os.store_name, creator.name, updater.name 
                                            FROM own_store_employees AS op
                                            LEFT JOIN own_store AS os ON op.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON op.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON op.last_updated_by = updater.admin_id
                                            WHERE op.role = 4 """
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


def get_all_franchise_other_emp():
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT op.*, os.store_name, creator.name, updater.name 
                                            FROM franchise_store_employees AS op
                                            LEFT JOIN own_store AS os ON op.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON op.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON op.last_updated_by = updater.admin_id
                                            WHERE op.role = 4 """
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
