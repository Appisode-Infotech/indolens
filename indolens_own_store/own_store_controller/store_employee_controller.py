import datetime
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.area_head_resp_model import get_area_heads
from indolens_own_store.own_store_model.response_model.own_store_emp_resp_model import get_own_store_employees

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_all_store_employee(store_id):
    try:
        with connection.cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id
                                            WHERE sm.assigned_store_id = '{store_id}' ORDER BY sm.employee_id DESC"""
            cursor.execute(get_store_employee_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "store_employee_list": get_own_store_employees(store_employees)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
def get_all_active_store_employee(store_id):
    try:
        with connection.cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id
                                            WHERE sm.assigned_store_id = '{store_id}' AND sm.status = 1 
                                            ORDER BY sm.employee_id DESC"""
            cursor.execute(get_store_employee_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "active_employee_list": get_own_store_employees(store_employees)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_store_employee_by_id(employee_id):
    try:
        with connection.cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id
                                            WHERE sm.employee_id = '{employee_id}' """
            cursor.execute(get_store_employee_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "store_employee": get_own_store_employees(store_employees)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_franchise_employee_by_id(employee_id):
    try:
        with connection.cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM franchise_store_employees AS sm
                                            LEFT JOIN franchise_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id
                                            WHERE sm.employee_id = '{employee_id}' """
            cursor.execute(get_store_employee_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "store_employee": get_own_store_employees(store_employees)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301