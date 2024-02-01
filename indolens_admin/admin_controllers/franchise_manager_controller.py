import datetime
import json

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_models.admin_resp_model.franchise_owner_resp_model import get_franchise_owners

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def create_franchise_owner(franchise_owner, files):
    try:
        hashed_password = bcrypt.hashpw(franchise_owner.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with connection.cursor() as cursor:
            insert_franchise_owner_query = f"""
                INSERT INTO franchise_store_employees (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, document_2_type, document_2_url, 
                    status, created_by, created_on, last_updated_by, last_updated_on, role,assigned_store_id
                ) VALUES (  
                    '{franchise_owner.name}', '{franchise_owner.email}', '{franchise_owner.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{franchise_owner.address}', '{franchise_owner.document_1_type}', 
                    '{json.dumps(files.document1)}', '{franchise_owner.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{franchise_owner.created_by}', '{getIndianTime()}', '{franchise_owner.last_updated_by}', 
                    '{getIndianTime()}', 1,0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_franchise_owner_query)

            subject = email_template_controller.get_employee_creation_email_subject(franchise_owner.name)
            body = email_template_controller.get_employee_creation_email_body(franchise_owner.name, 'Franchise Owner',
                                                                              franchise_owner.email,
                                                                              franchise_owner.password)
            send_notification_controller.send_email(subject, body, franchise_owner.email)

            foid = cursor.lastrowid

            return {
                "status": True,
                "message": "franchise owner added",
                "franchiseOwnersId": foid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_franchise_owner(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with connection.cursor() as cursor:
            get_all_franchise_owner_query = f""" SELECT a.*, os.store_name, creator.name, updater.name 
                                            FROM franchise_store_employees AS a
                                            LEFT JOIN franchise_store AS os ON a.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON a.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON a.last_updated_by = updater.admin_id 
                                            WHERE a.role = 1 AND a.status {status_condition}
                                            ORDER BY a.employee_id DESC"""
            cursor.execute(get_all_franchise_owner_query)
            franchise_owners = cursor.fetchall()
            return {
                "status": True,
                "franchise_owners": get_franchise_owners(franchise_owners)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_owner_by_id(foid):
    try:
        with connection.cursor() as cursor:
            get_all_franchise_owner_query = f""" SELECT a.*, os.store_name, creator.name, updater.name 
                                            FROM franchise_store_employees AS a
                                            LEFT JOIN franchise_store AS os ON a.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON a.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON a.last_updated_by = updater.admin_id
                                             WHERE a.employee_id = '{foid}'"""
            cursor.execute(get_all_franchise_owner_query)
            franchise_owners = cursor.fetchall()
            return {
                "status": True,
                "franchise_owner": get_franchise_owners(franchise_owners)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_franchise_owner(foid, status):
    try:
        with connection.cursor() as cursor:
            update_franchise_owners_query = f"""
                UPDATE franchise_store_employees
                SET
                    status = {status}
                WHERE
                    employee_id = {foid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_franchise_owners_query)

            return {
                "status": True,
                "message": "franchise owner updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_franchise_owner(franchise_owner, files):
    try:
        with connection.cursor() as cursor:
            update_franchise_owners_query = f"""
                UPDATE franchise_store_employees
                SET 
                    name = '{franchise_owner.name}',
                    email = '{franchise_owner.email}',
                    phone = '{franchise_owner.phone}',
                    {'profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                    address = '{franchise_owner.address}',
                    last_updated_by = '{franchise_owner.last_updated_by}',
                    last_updated_on = '{getIndianTime()}'
                WHERE employee_id = {franchise_owner.employee_id}
            """

            # Execute the update query using your cursor
            cursor.execute(update_franchise_owners_query)

            return {
                "status": True,
                "message": "franchise owner updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def assign_store_franchise_owner(empId, storeId):
    try:
        with connection.cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE franchise_store_employees
                SET
                    assigned_store_id = {storeId}
                WHERE
                    employee_id = {empId}
            """
            # Execute the update query using your cursor
            cursor.execute(update_store_manager_query)

            return {
                "status": True,
                "message": "Store assigned"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def unassign_store_franchise_owner(FranchiseOwnerId, storeId):
    try:
        with connection.cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE franchise_store_employees
                SET
                    assigned_store_id = 0
                WHERE
                    employee_id = {FranchiseOwnerId}
            """
            # Execute the update query using your cursor
            cursor.execute(update_store_manager_query)

            return {
                       "status": True,
                       "message": "Store un assigned"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_active_own_stores():
    try:
        with connection.cursor() as cursor:
            unassigned_stores = []
            get_unassigned_active_own_store_for_manager_query = f"""SELECT f.store_id, f.store_name FROM franchise_store f 
            WHERE f.status = 1;"""
            cursor.execute(get_unassigned_active_own_store_for_manager_query)
            stores_data = cursor.fetchall()
            for store in stores_data:
                unassigned_stores.append({
                    "store_id": store[0],
                    "store_name": store[1]
                })
            return {
                       "status": True,
                       "available_stores": unassigned_stores
                   }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301