import datetime
import json

import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_models.admin_resp_model.area_head_resp_model import get_area_heads
from indolens_own_store.own_store_model.response_model.own_store_emp_resp_model import get_own_store_employees

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def get_all_store_employee(store_id):
    try:
        with getConnection().cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.os_store_name AS store_name, creator.admin_name AS creator, 
                                                        updater.admin_name AS updater FROM own_store_employees AS sm
                                                        LEFT JOIN own_store AS os ON sm.ose_assigned_store_id = os.os_store_id
                                                        LEFT JOIN admin AS creator ON sm.ose_created_by = creator.admin_admin_id
                                                        LEFT JOIN admin AS updater ON sm.ose_last_updated_by = updater.admin_admin_id
                                                        WHERE sm.ose_assigned_store_id IN {store_id}
                                                        ORDER BY sm.ose_employee_id DESC"""
            cursor.execute(get_store_manager_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "store_employees": store_employees
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_store_employee_by_id(employee_id):
    try:
        with getConnection().cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.os_store_name AS store_name, creator.admin_name AS creator, 
                                                        updater.admin_name AS updater FROM own_store_employees AS sm
                                                        LEFT JOIN own_store AS os ON sm.ose_assigned_store_id = os.os_store_id
                                                        LEFT JOIN admin AS creator ON sm.ose_created_by = creator.admin_admin_id
                                                        LEFT JOIN admin AS updater ON sm.ose_last_updated_by = updater.admin_admin_id 
                                                        WHERE sm.ose_employee_id = {employee_id} """
            cursor.execute(get_store_manager_query)
            store_employees = cursor.fetchone()
            store_employees['ose_document_1_url'] = json.loads(store_employees['ose_document_1_url']) if store_employees[
                'ose_document_1_url'] else []
            store_employees['ose_document_2_url'] = json.loads(store_employees['ose_document_2_url']) if store_employees[
                'ose_document_2_url'] else []
            return {
                "status": True,
                "store_employee": store_employees
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301