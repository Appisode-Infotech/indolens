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

def create_optimetry(optimetry_obj, files):
    try:
        hashed_password = bcrypt.hashpw(optimetry_obj.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with getConnection().cursor() as cursor:
            insert_optimetry_obj_query = f"""
                INSERT INTO own_store_employees (
                    ose_name, ose_email, ose_phone, ose_password, ose_profile_pic, 
                    ose_address, ose_document_1_type, ose_document_1_url, 
                    ose_document_2_type, ose_document_2_url, ose_status, ose_created_by, ose_created_on, 
                    ose_last_updated_by, ose_last_updated_on, ose_role, ose_certificates, ose_assigned_store_id
                ) VALUES (
                    '{optimetry_obj.name}', '{optimetry_obj.email}', '{optimetry_obj.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{optimetry_obj.address}', '{optimetry_obj.document_1_type}', 
                    '{json.dumps(files.document1)}', '{optimetry_obj.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{optimetry_obj.created_by}', '{getIndianTime()}', '{optimetry_obj.last_updated_by}', '{getIndianTime()}', 2, 
                    '{json.dumps(files.certificates)}', 0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_optimetry_obj_query)
            empid = cursor.lastrowid

            subject = email_template_controller.get_employee_creation_email_subject(optimetry_obj.name)
            body = email_template_controller.get_employee_creation_email_body(optimetry_obj.name, 'Optometry',
                                                                              optimetry_obj.email,
                                                                              optimetry_obj.password)
            send_notification_controller.send_email(subject, body, optimetry_obj.email)

            return {
                "status": True,
                "message": "Employee added",
                "empid": empid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def update_optimetry(optimetry_obj, files):
    try:
        with getConnection().cursor() as cursor:
            update_optimetry_obj_query = f"""
                                UPDATE own_store_employees
                                SET 
                                    ose_name = '{optimetry_obj.name}',
                                    ose_email = '{optimetry_obj.email}',
                                    ose_phone = '{optimetry_obj.phone}',
                                    {'ose_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                                    ose_address = '{optimetry_obj.address}',
                                    ose_last_updated_by = '{optimetry_obj.last_updated_by}',
                                    ose_last_updated_on = '{getIndianTime()}'
                                WHERE ose_employee_id = {optimetry_obj.employee_id}
                            """
            cursor.execute(update_optimetry_obj_query)

            return {
                "status": True,
                "message": "Employee updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_optimetry(opid, status):
    try:
        with getConnection().cursor() as cursor:
            update_optimetry_query = f"""
                UPDATE own_store_employees
                SET
                    ose_status = {status}
                WHERE
                    ose_employee_id = {opid}
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


def create_franchise_optimetry(optimetry_obj, files):
    try:
        hashed_password = bcrypt.hashpw(optimetry_obj.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with getConnection().cursor() as cursor:
            insert_optimetry_obj_query = f"""
                INSERT INTO franchise_store_employees (
                    fse_name, fse_email, fse_phone, fse_password, fse_profile_pic, 
                    fse_address, fse_document_1_type, fse_document_1_url, 
                    fse_document_2_type, fse_document_2_url, fse_status, fse_created_by, fse_created_on, 
                    fse_last_updated_by, fse_last_updated_on, fse_role, fse_certificates,fse_assigned_store_id
                ) VALUES (
                    '{optimetry_obj.name}', '{optimetry_obj.email}', '{optimetry_obj.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{optimetry_obj.address}', '{optimetry_obj.document_1_type}', 
                    '{json.dumps(files.document1)}', '{optimetry_obj.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{optimetry_obj.created_by}', '{getIndianTime()}', '{optimetry_obj.last_updated_by}', '{getIndianTime()}', 2, '{json.dumps(files.certificates)}',0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_optimetry_obj_query)

            subject = email_template_controller.get_franchise_employee_creation_email_subject(optimetry_obj.name)
            body = email_template_controller.get_franchise_employee_creation_email_body(optimetry_obj.name, 'Optometry',
                                                                              optimetry_obj.email,
                                                                              optimetry_obj.password)
            send_notification_controller.send_email(subject, body, optimetry_obj.email)

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


def get_all_optimetry(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_store_manager_query = f""" SELECT op.*, os.os_store_name AS store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater FROM own_store_employees AS op
                                            LEFT JOIN own_store AS os ON op.ose_assigned_store_id = os.os_store_id
                                            LEFT JOIN admin AS creator ON op.ose_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON op.ose_last_updated_by = updater.admin_admin_id
                                            WHERE op.ose_role = 2 AND op.ose_status {status_condition}
                                            ORDER BY op.ose_employee_id DESC"""
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                "status": True,
                "optimetry_list": store_managers
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_franchise_optimetry(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_all_franchise_optometry_query = f""" SELECT fse.*, fs.fs_store_name, creator.admin_name, updater.admin_name 
                                                        FROM franchise_store_employees AS fse
                                                        LEFT JOIN franchise_store AS fs ON fse.fse_assigned_store_id = fs.fs_store_id
                                                        LEFT JOIN admin AS creator ON fse.fse_created_by = creator.admin_admin_id
                                                        LEFT JOIN admin AS updater ON fse.fse_last_updated_by = updater.admin_admin_id 
                                                        WHERE fse.fse_role = 2 AND fse.fse_status {status_condition}
                                                        ORDER BY fse.fse_employee_id DESC"""

            cursor.execute(get_all_franchise_optometry_query)
            franchise_optimetry = cursor.fetchall()
            return {
                "status": True,
                "optimetry_list": franchise_optimetry
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_optimetry_by_id(opid):
    try:
        with getConnection().cursor() as cursor:
            get_optimetry_query = f""" SELECT op.*, os.os_store_name AS store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater FROM own_store_employees AS op
                                            LEFT JOIN own_store AS os ON op.ose_assigned_store_id = os.os_store_id
                                            LEFT JOIN admin AS creator ON op.ose_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON op.ose_last_updated_by = updater.admin_admin_id 
                                            WHERE op.ose_employee_id = '{opid}'"""
            cursor.execute(get_optimetry_query)
            optimetry = cursor.fetchone()

            optimetry['ose_document_1_url'] = json.loads(optimetry['ose_document_1_url']) if optimetry[
                'ose_document_1_url'] else []
            optimetry['ose_document_2_url'] = json.loads(optimetry['ose_document_2_url']) if optimetry[
                'ose_document_2_url'] else []
            optimetry['ose_certificates'] = json.loads(optimetry['ose_certificates']) if optimetry[
                'ose_certificates'] else []

            return {
                "status": True,
                "optimetry": optimetry
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_optimetry_by_id(opid):
    try:
        with getConnection().cursor() as cursor:
            get_optimetry_query = f""" SELECT fse.*, fs.fs_store_name, creator.admin_name AS creator, 
                                            updater.admin_name AS updater
                                            FROM franchise_store_employees AS fse
                                            LEFT JOIN franchise_store AS fs ON fse.fse_assigned_store_id = fs.fs_store_id
                                            LEFT JOIN admin AS creator ON fse.fse_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON fse.fse_last_updated_by = updater.admin_admin_id 
                                            WHERE fse.fse_employee_id = '{opid}'"""
            cursor.execute(get_optimetry_query)
            optimetry = cursor.fetchone()

            optimetry['fse_document_1_url'] = json.loads(optimetry['fse_document_1_url']) if optimetry['fse_document_1_url'] else []
            optimetry['fse_document_2_url'] = json.loads(optimetry['fse_document_2_url']) if optimetry['fse_document_2_url'] else []
            optimetry['fse_certificates'] = json.loads(optimetry['fse_certificates']) if optimetry['fse_certificates'] else []

            return {
                "status": True,
                "optimetry": optimetry
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_franchise_optimetry(optimetry_obj, files):
    try:
        with getConnection().cursor() as cursor:
            update_optimetry_obj_query = f"""
                                UPDATE franchise_store_employees
                                SET 
                                    fse_name = '{optimetry_obj.name}',
                                    fse_email = '{optimetry_obj.email}',
                                    fse_phone = '{optimetry_obj.phone}',
                                    {'fse_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                                    fse_address = '{optimetry_obj.address}',
                                    fse_last_updated_by = '{optimetry_obj.last_updated_by}',
                                    fse_last_updated_on = '{getIndianTime()}'
                                WHERE fse_employee_id = {optimetry_obj.employee_id}
                            """
            cursor.execute(update_optimetry_obj_query)

            return {
                "status": True,
                "message": "Franchise Optimetry updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_franchise_optimetry(franchiseOptimetryId, status):
    try:
        with getConnection().cursor() as cursor:
            update_optimetry_query = f"""
                UPDATE franchise_store_employees
                SET
                    status = {status}
                WHERE
                    employee_id = {franchiseOptimetryId}
            """

            # Execute the update query using your cursor
            cursor.execute(update_optimetry_query)

            return {
                "status": True,
                "message": "Franchise Optimetry updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
