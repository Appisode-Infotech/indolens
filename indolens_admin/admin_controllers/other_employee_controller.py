import datetime
import json

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.other_emp_resp_model import get_other_employees

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_other_employee(other_emp, files):
    try:
        with connection.cursor() as cursor:
            insert_other_emp_query = f"""
                INSERT INTO other_employees (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, document_2_type, document_2_url, 
                    status, created_by, created_on, last_updated_by, last_updated_on
                ) VALUES (
                    '{other_emp.name}', '{other_emp.email}', '{other_emp.phone}', '{other_emp.password}',
                    '{files.profile_pic}', '{other_emp.address}', '{other_emp.document_1_type}', 
                    '{json.dumps(files.document1)}', '{other_emp.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{other_emp.created_by}', '{today}', '{other_emp.last_updated_by}', '{today}'
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
            get_sales_executive_query = f"""
            SELECT emp.*, creator.name, updater.name, os.store_name
            FROM other_employees AS emp
            LEFT JOIN own_store AS os ON emp.assigned_store_id = os.store_id
            LEFT JOIN admin AS creator ON emp.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON emp.last_updated_by = updater.admin_id
            GROUP BY emp.other_employee_id
            """
            cursor.execute(get_sales_executive_query)
            other_emp = cursor.fetchall()

            return {
                       "status": True,
                       "other_emp_list": get_other_employees(other_emp)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_other_emp_by_id(empid):
    try:
        with connection.cursor() as cursor:
            get_other_employee_query = f"""
            SELECT emp.*, creator.name, updater.name, os.store_name
            FROM other_employees AS emp
            LEFT JOIN own_store AS os ON emp.assigned_store_id = os.store_id
            LEFT JOIN admin AS creator ON emp.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON emp.last_updated_by = updater.admin_id
            WHERE emp.other_employee_id = {empid}
            """
            cursor.execute(get_other_employee_query)
            other_emp = cursor.fetchall()
            return {
                       "status": True,
                       "other_employee": get_other_employees(other_emp)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_other_employees(empid, status):
    try:
        with connection.cursor() as cursor:
            update_other_employees_query = f"""
                UPDATE other_employees
                SET
                    status = {status}
                WHERE
                    other_employee_id = {empid}
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
