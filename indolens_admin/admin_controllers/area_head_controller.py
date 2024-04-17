import datetime
import json

import bcrypt
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_models.admin_resp_model.area_head_resp_model import get_area_heads

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def create_area_head(area_head, files):
    try:
        hashed_password = bcrypt.hashpw(area_head.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with getConnection().cursor() as cursor:
            insert_area_head_query = f"""
                INSERT INTO area_head (
                    ah_name, ah_email, ah_phone, ah_password, ah_profile_pic, 
                    ah_address, ah_document_1_type, ah_document_1_url, ah_document_2_type, ah_document_2_url, 
                    ah_status, ah_created_by, ah_created_on, ah_last_updated_by, ah_last_updated_on,ah_assigned_stores
                ) VALUES (
                    '{area_head.full_name}', '{area_head.email}', '{area_head.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{area_head.complete_address}', '{area_head.document1_type}', 
                    '{json.dumps(files.document1)}', '{area_head.document2_type}', '{json.dumps(files.document2)}', 
                    1, '{area_head.created_by}', '{getIndianTime()}', '{area_head.last_updated_by}', '{getIndianTime()}',0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_area_head_query)
            ahid = cursor.lastrowid

            subject = email_template_controller.get_employee_creation_email_subject(area_head.full_name)
            body = email_template_controller.get_employee_creation_email_body(area_head.full_name, 'Area Head',
                                                                              area_head.email,
                                                                              area_head.password)
            send_notification_controller.send_email(subject, body, area_head.email)

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
        with getConnection().cursor() as cursor:
            get_area_head_query = f"""
            SELECT ah.*, GROUP_CONCAT(os.os_store_name SEPARATOR ', ') AS assigned_stores_names, creator.admin_name,
            updater.admin_name
            FROM area_head AS ah
            LEFT JOIN own_store AS os ON FIND_IN_SET(os.os_store_id, ah.ah_assigned_stores)
            LEFT JOIN admin AS creator ON ah.ah_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON ah.ah_last_updated_by = updater.admin_admin_id
            WHERE ah.ah_status {status_condition} GROUP BY ah.ah_area_head_id ORDER BY ah.ah_area_head_id DESC"""
            cursor.execute(get_area_head_query)
            area_heads = cursor.fetchall()

            for area_head in area_heads:
                area_head['ah_assigned_stores'] = [int(store_id) for store_id in
                                                   area_head['ah_assigned_stores'].split(',')] if area_head[
                    'ah_assigned_stores'] else []

                area_head['assigned_stores_names'] = [store.strip() for store in
                                                      area_head['assigned_stores_names'].split(',')] if area_head[
                    'assigned_stores_names'] else []

                area_head['id_name_pair'] = list(
                    zip(area_head['ah_assigned_stores'], area_head['assigned_stores_names']))

            return {
                "status": True,
                "area_heads_list": area_heads
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_area_head_by_id(ahid):
    try:
        with getConnection().cursor() as cursor:
            get_area_head_query = f"""
                        SELECT ah.*, GROUP_CONCAT(os.os_store_name SEPARATOR ', ') AS assigned_stores_names, creator.admin_name,
                        updater.admin_name
                        FROM area_head AS ah
                        LEFT JOIN own_store AS os ON FIND_IN_SET(os.os_store_id, ah.ah_assigned_stores)
                        LEFT JOIN admin AS creator ON ah.ah_created_by = creator.admin_admin_id
                        LEFT JOIN admin AS updater ON ah.ah_last_updated_by = updater.admin_admin_id
                        WHERE ah_area_head_id = '{ahid}' """
            cursor.execute(get_area_head_query)
            area_head = cursor.fetchone()

            area_head['ah_assigned_stores'] = [int(store_id) for store_id in
                                               area_head['ah_assigned_stores'].split(',')] if area_head[
                'ah_assigned_stores'] else []

            area_head['assigned_stores_names'] = [store.strip() for store in
                                                  area_head['assigned_stores_names'].split(',')] if area_head[
                'assigned_stores_names'] else []

            area_head['id_name_pair'] = list(
                zip(area_head['ah_assigned_stores'], area_head['assigned_stores_names']))

            # get_area_head_query = f"""
            #             SELECT ah.*, GROUP_CONCAT(os.os_store_name SEPARATOR ', ') AS assigned_stores_names,
            #             creator.admin_name AS creator,
            #             updater.admin_name AS updater
            #             FROM area_head AS ah
            #             LEFT JOIN own_store AS os ON FIND_IN_SET(os.os_store_id, ah.ah_assigned_stores)
            #             LEFT JOIN admin AS creator ON ah.ah_created_by = creator.admin_admin_id
            #             LEFT JOIN admin AS updater ON ah.ah_last_updated_by = updater.admin_admin_id
            #             WHERE ah_area_head_id = '{ahid}'"""
            # cursor.execute(get_area_head_query)
            # area_heads = cursor.fetchone()

            area_head['ah_document_1_url'] = json.loads(area_head['ah_document_1_url']) if area_head[
                'ah_document_1_url'] else []
            area_head['ah_document_2_url'] = json.loads(area_head['ah_document_2_url']) if area_head[
                'ah_document_2_url'] else []

            return {
                "status": True,
                "area_head": area_head
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_area_head(area_head, files):
    try:
        with getConnection().cursor() as cursor:
            update_area_head_query = f"""
                                UPDATE area_head
                                SET 
                                    ah_name = '{area_head.full_name}',
                                    ah_email = '{area_head.email}',
                                    ah_phone = '{area_head.phone}',
                                    {'ah_profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                                    ah_address = '{area_head.complete_address}',
                                    ah_last_updated_by = '{area_head.last_updated_by}',
                                    ah_last_updated_on = '{getIndianTime()}'
                                WHERE ah_area_head_id = {area_head.area_head_id}
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
        with getConnection().cursor() as cursor:
            set_area_head_query = f"""
            UPDATE area_head SET ah_status = '{status}' WHERE ah_area_head_id = '{ahId}';
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
    try:
        with getConnection().cursor() as cursor:
            update_store_manager_query = f"""
                UPDATE area_head
                SET
                    assigned_stores = '{storeId}'
                WHERE
                    area_head_id = {empId}
            """
            # Execute the update query using your cursor
            cursor.execute(update_store_manager_query)

            get_employee_query = f""" SELECT name,email,phone FROM area_head WHERE area_head_id = {empId}
                                                            """
            # Execute the update query using your cursor
            cursor.execute(get_employee_query)
            manager_data = cursor.fetchone()
            if len(storeId) == 1:
                storeId = f"""({storeId})"""

            get_store_query = f""" SELECT store_name, store_phone, store_address FROM own_store 
                                                                                    WHERE store_id IN {tuple(storeId)}"""

            cursor.execute(get_store_query)
            store_data = cursor.fetchall()

            subject = email_template_controller.get_area_head_assigned_store_email_subject(manager_data[0])
            body = email_template_controller.get_area_head_assigned_store_email_body(manager_data[0], 'Area Head',
                                                                                     manager_data[1],
                                                                                     store_data)

            response = send_notification_controller.send_email(subject, body, manager_data[1])

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
        with getConnection().cursor() as cursor:
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
