import datetime
import json

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.own_store_emp_resp_model import get_own_store_employees


def get_all_franchise_emp(store):
    try:
        with connection.cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM franchise_store_employees AS sm
                                            LEFT JOIN franchise_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id
                                            WHERE sm.assigned_store_id = '{store}' """
            cursor.execute(get_store_employee_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "franchise_employee_list": get_own_store_employees(store_employees)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_franchise_emp_by_id(store, employeeId):
    try:
        with connection.cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM franchise_store_employees AS sm
                                            LEFT JOIN franchise_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id
                                            WHERE sm.assigned_store_id = '{store}' AND sm.employee_id = {employeeId}"""
            cursor.execute(get_store_employee_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "franchise_employee": get_own_store_employees(store_employees)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301