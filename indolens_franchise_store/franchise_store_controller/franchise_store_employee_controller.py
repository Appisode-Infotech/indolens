import datetime
import json

import bcrypt
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_models.admin_resp_model.own_store_emp_resp_model import get_own_store_employees


def get_all_franchise_emp(store):
    try:
        with getConnection().cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, fs.fs_store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater
                                            FROM franchise_store_employees AS sm
                                            LEFT JOIN franchise_store AS fs ON sm.fse_assigned_store_id = fs.fs_store_id
                                            LEFT JOIN admin AS creator ON sm.fse_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON sm.fse_last_updated_by = updater.admin_admin_id
                                            WHERE sm.fse_assigned_store_id = '{store}' 
                                            ORDER BY sm.fse_employee_id DESC"""

            cursor.execute(get_store_employee_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "franchise_employee_list": store_employees
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_franchise_emp_by_id(store, employeeId):
    try:
        with getConnection().cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, fs.fs_store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater
                                            FROM franchise_store_employees AS sm
                                            LEFT JOIN franchise_store AS fs ON sm.fse_assigned_store_id = fs.fs_store_id
                                            LEFT JOIN admin AS creator ON sm.fse_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON sm.fse_last_updated_by = updater.admin_admin_id
                                            WHERE sm.fse_employee_id = {employeeId} """
            cursor.execute(get_store_employee_query)

            store_employees = cursor.fetchone()
            store_employees['fse_document_1_url'] = json.loads(store_employees['fse_document_1_url']) if store_employees['fse_document_1_url'] else []
            store_employees['fse_document_2_url'] = json.loads(store_employees['fse_document_2_url']) if store_employees['fse_document_2_url'] else []
            return {
                "status": True,
                "franchise_employee": store_employees
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_active_franchise_emp(store):
    try:
        with getConnection().cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, fs.fs_store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater
                                            FROM franchise_store_employees AS sm
                                            LEFT JOIN franchise_store AS fs ON sm.fse_assigned_store_id = fs.fs_store_id
                                            LEFT JOIN admin AS creator ON sm.fse_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON sm.fse_last_updated_by = updater.admin_admin_id
                                            WHERE sm.fse_assigned_store_id = '{store}' AND sm.fse_status = 1 
                                            AND sm.fse_assigned_store_id != 0
                                            AND sm.fse_role != 4
                                            ORDER BY sm.fse_employee_id DESC"""
            cursor.execute(get_store_employee_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "active_employee_list": store_employees
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_own_store_employee_by_id(employee_id):
    try:
        with getConnection().cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM own_store_employees AS sm
                                            LEFT JOIN own_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id
                                            WHERE sm.employee_id = '{employee_id}' """
            cursor.execute(get_store_employee_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "franchise_employee": store_employees
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_active_store_optometry(assigned_store):
    try:
        with getConnection().cursor() as cursor:
            get_store_employee_query = f""" SELECT sm.*, fs.fs_store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater
                                            FROM franchise_store_employees AS sm
                                            LEFT JOIN franchise_store AS fs ON sm.fse_assigned_store_id = fs.fs_store_id
                                            LEFT JOIN admin AS creator ON sm.fse_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON sm.fse_last_updated_by = updater.admin_admin_id
                                            WHERE sm.fse_assigned_store_id = '{assigned_store}' AND sm.fse_status = 1 
                                            AND sm.fse_role != 4
                                            ORDER BY sm.fse_employee_id DESC"""
            cursor.execute(get_store_employee_query)
            store_employees = cursor.fetchall()
            return {
                "status": True,
                "optometry_list": store_employees
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301