import datetime
import json

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.own_store_emp_resp_model import get_own_store_employees

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_store_manager(sub_admin, files):
    try:
        with connection.cursor() as cursor:
            insert_store_manager_query = f"""
                INSERT INTO own_store_employees (
                    name, email, phone, password, profile_pic, 
                    assigned_store_id, address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role
                ) VALUES (
                    '{sub_admin.name}', '{sub_admin.email}', '{sub_admin.phone}', '{sub_admin.password}', '{files.profile_pic}', 
                    '{sub_admin.assigned_store_id}', '{sub_admin.address}', '{sub_admin.document_1_type}', '{json.dumps(files.document1)}', 
                    '{sub_admin.document_2_type}', '{json.dumps(files.document2)}', 1, '{sub_admin.created_by}', '{today}', 
                    '{sub_admin.last_updated_by}', '{today}', 1
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_store_manager_query)

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


def get_all_store_manager():
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id
                                            WHERE sm.role = 1 """
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
                                            WHERE sm.employee_id = '{mid}'"""
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
