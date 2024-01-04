import datetime
import json

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.area_head_resp_model import get_area_heads

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_area_head(area_head, files):
    try:
        hashed_password = bcrypt.hashpw(area_head.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with connection.cursor() as cursor:
            insert_area_head_query = f"""
                INSERT INTO area_head (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, document_2_type, document_2_url, 
                    status, created_by, created_on, last_updated_by, last_updated_on,assigned_stores
                ) VALUES (
                    '{area_head.full_name}', '{area_head.email}', '{area_head.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{area_head.complete_address}', '{area_head.document1_type}', 
                    '{json.dumps(files.document1)}', '{area_head.document2_type}', '{json.dumps(files.document2)}', 
                    1, '{area_head.created_by}', '{today}', '{area_head.last_updated_by}', '{today}',0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_area_head_query)
            ahid = cursor.lastrowid

            return {
                       "status": True,
                       "message": "Area Head added",
                       "areaHeadId": ahid
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_area_head(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with connection.cursor() as cursor:
            get_area_head_query = f"""
            SELECT ah.*, GROUP_CONCAT(os.store_name SEPARATOR ', ') AS assigned_stores_names, creator.name, updater.name
            FROM area_head AS ah
            LEFT JOIN own_store AS os
            ON FIND_IN_SET(os.store_id, ah.assigned_stores)
            LEFT JOIN admin AS creator ON ah.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON ah.last_updated_by = updater.admin_id
            WHERE ah.status {status_condition} GROUP BY ah.area_head_id ORDER BY ah.area_head_id DESC"""
            cursor.execute(get_area_head_query)
            area_heads = cursor.fetchall()

            return {
                       "status": True,
                       "area_heads_list": get_area_heads(area_heads)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_area_head_by_id(ahid):
    try:
        with connection.cursor() as cursor:
            get_area_head_query = f"""
            SELECT ah.*, GROUP_CONCAT(os.store_name SEPARATOR ', ') AS assigned_stores_names, creator.name, updater.name
            FROM area_head AS ah
            LEFT JOIN own_store AS os
            ON FIND_IN_SET(os.store_id, ah.assigned_stores)
            LEFT JOIN admin AS creator ON ah.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON ah.last_updated_by = updater.admin_id
            WHERE area_head_id = '{ahid}'
            GROUP BY ah.area_head_id
            """
            cursor.execute(get_area_head_query)
            area_heads = cursor.fetchall()

            return {
                       "status": True,
                       "area_head": get_area_heads(area_heads)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def edit_area_head(area_head, files):
    try:
        with connection.cursor() as cursor:
            update_area_head_query = f"""
                                UPDATE area_head
                                SET 
                                    name = '{area_head.full_name}',
                                    email = '{area_head.email}',
                                    phone = '{area_head.phone}',
                                    {'profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                                    address = '{area_head.complete_address}',
                                    last_updated_by = '{area_head.last_updated_by}',
                                    last_updated_on = '{today}'
                                WHERE area_head_id = {area_head.area_head_id}
                            """
            cursor.execute(update_area_head_query)

            return {
                "status": True,
                "message": "Area Head updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_area_head(ahId, status):
    # update table set status= '{status}' where area_head_id = '{ahid}'
    try:
        with connection.cursor() as cursor:
            set_area_head_query = f"""
            UPDATE area_head SET status = '{status}' WHERE area_head_id = '{ahId}';
            """
            cursor.execute(set_area_head_query)

            return {
                       "status": True,
                       "message": "Updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def assignStore(empId, storeId):
    print(storeId)
    try:
        with connection.cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE area_head
                SET
                    assigned_stores = '{storeId}'
                WHERE
                    area_head_id = {empId}
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


def unAssignStore(empId, storeId):
    try:
        with connection.cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE area_head
                SET
                    assigned_stores = 0
                WHERE
                    area_head_id = {empId}
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