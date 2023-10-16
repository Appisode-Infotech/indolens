import datetime
import json

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.own_store_emp_resp_model import get_own_store_employees

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_optimetry(optimetry_obj, files):
    try:
        with connection.cursor() as cursor:
            insert_optimetry_obj_query = f"""
                INSERT INTO own_store_employees (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role, certificates
                ) VALUES (
                    '{optimetry_obj.name}', '{optimetry_obj.email}', '{optimetry_obj.phone}', '{optimetry_obj.password}',
                    '{files.profile_pic}', '{optimetry_obj.address}', '{optimetry_obj.document_1_type}', 
                    '{json.dumps(files.document1)}', '{optimetry_obj.document_2_type}', '{json.dumps(files.document2)}', 
                    0, '{optimetry_obj.created_by}', '{today}', '{optimetry_obj.last_updated_by}', '{today}', 2, '{json.dumps(files.certificates)}
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_optimetry_obj_query)
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


def create_franchise_optimetry(optimetry_obj, files):
    print(optimetry_obj.certificates)
    try:
        with connection.cursor() as cursor:
            insert_optimetry_obj_query = f"""
                INSERT INTO franchise_store_employees (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role, certificates
                ) VALUES (
                    '{optimetry_obj.name}', '{optimetry_obj.email}', '{optimetry_obj.phone}', '{optimetry_obj.password}',
                    '{files.profile_pic}', '{optimetry_obj.address}', '{optimetry_obj.document_1_type}', 
                    '{json.dumps(files.document1)}', '{optimetry_obj.document_2_type}', '{json.dumps(files.document2)}', 
                    0, '{optimetry_obj.created_by}', '{today}', '{optimetry_obj.last_updated_by}', '{today}', 2, '{json.dumps(files.certificates)}'
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_optimetry_obj_query)
            opid = cursor.lastrowid

            return {
                "status": True,
                "message": "Employee added",
                "opid": opid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_optimetry():
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT op.*, os.store_name, creator.name, updater.name FROM own_store_employees AS op
                                            LEFT JOIN own_store AS os ON op.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON op.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON op.last_updated_by = updater.admin_id
                                            WHERE op.role = 2 """
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                       "status": True,
                       "optimetry_list": get_own_store_employees(store_managers)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_franchise_optimetry():
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT op.*, os.store_name, creator.name, updater.name 
                                            FROM franchise_store_employees AS op
                                            LEFT JOIN own_store AS os ON op.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON op.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON op.last_updated_by = updater.admin_id
                                            WHERE op.role = 2 """
            cursor.execute(get_store_manager_query)
            franchise_optimetry = cursor.fetchall()
            print(get_own_store_employees(franchise_optimetry))
            return {
                       "status": True,
                       "optimetry_list": get_own_store_employees(franchise_optimetry)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_optimetry_by_id(opid):
    try:
        with connection.cursor() as cursor:
            get_optimetry_query = f""" SELECT op.*, os.store_name, creator.name, updater.name FROM own_store_employees AS op
                                            LEFT JOIN own_store AS os ON op.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON op.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON op.last_updated_by = updater.admin_id 
                                            WHERE op.employee_id = '{opid}'"""
            cursor.execute(get_optimetry_query)
            optimetry = cursor.fetchall()
            return {
                       "status": True,
                       "optimetry": get_own_store_employees(optimetry)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_optimetry_by_id(opid):
    try:
        with connection.cursor() as cursor:
            get_optimetry_query = f""" SELECT op.*, os.store_name, creator.name, updater.name FROM franchise_store_employees AS op
                                            LEFT JOIN own_store AS os ON op.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON op.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON op.last_updated_by = updater.admin_id 
                                            WHERE op.employee_id = '{opid}'"""
            cursor.execute(get_optimetry_query)
            optimetry = cursor.fetchall()
            return {
                       "status": True,
                       "optimetry": get_own_store_employees(optimetry)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_optimetry(opid, status):
    try:
        with connection.cursor() as cursor:
            update_optimetry_query = f"""
                UPDATE own_store_employees
                SET
                    status = {status}
                WHERE
                    employee_id = {opid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_optimetry_query)

            return {
                       "status": True,
                       "message": "Optimetry updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

