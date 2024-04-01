import datetime

import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_models.admin_resp_model.own_store_resp_model import get_own_store

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def create_own_store(store_obj):
    cleaned_str = store_obj.store_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    store_lat, store_lng = map(float, cleaned_str.split(', '))
    try:
        with getConnection().cursor() as cursor:
            create_own_store_query = """
                INSERT INTO own_store (
                    os_store_zip, os_store_name, os_store_display_name, os_store_phone, 
                    os_store_gst, os_store_email, os_store_city, os_store_state, os_store_lat, 
                    os_store_lng, os_store_address, os_status, os_created_by, os_created_on, 
                    os_last_updated_by, os_last_updated_on
                ) 
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
            """

            cursor.execute(create_own_store_query, (
                store_obj.store_zip_code, store_obj.store_name, store_obj.store_display_name,
                store_obj.store_phone, store_obj.store_gstin, store_obj.store_email,
                store_obj.store_city, store_obj.store_state, store_lat, store_lng,
                store_obj.complete_address, 1, store_obj.created_by, getIndianTime(),
                store_obj.last_updated_by, getIndianTime()
            ))
            storeId = cursor.lastrowid
            return {
                       "status": True,
                       "message": "own store added",
                       "storeId": storeId
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_own_stores(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_own_stores_query = f"""
                                    SELECT own_store.*, own_store_employees.ose_name, own_store_employees.ose_employee_id,
                                    creator.admin_name, updater.admin_name
                                    FROM own_store
                                    LEFT JOIN admin AS creator ON own_store.os_created_by = creator.admin_admin_id
                                    LEFT JOIN admin AS updater ON own_store.os_last_updated_by = updater.admin_admin_id
                                    LEFT JOIN own_store_employees ON own_store.os_store_id = own_store_employees.ose_assigned_store_id AND own_store_employees.ose_role = 1
                                    WHERE own_store.os_status {status_condition} 
                                    GROUP BY own_store.os_store_id
                                    ORDER BY own_store.os_store_id DESC
                                    """
            cursor.execute(get_own_stores_query)
            stores_data = cursor.fetchall()
            return {
                       "status": True,
                       "own_stores": stores_data
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_own_store_count():
    try:
        with getConnection().cursor() as cursor:
            get_own_stores_query = f"""
                                    SELECT count(*)
                                    FROM own_store
                                    """
            cursor.execute(get_own_stores_query)
            stores_data = cursor.fetchone()
            return {
                       "status": True,
                       "own_stores": stores_data['count(*)']
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_unassigned_active_own_store_for_manager():
    try:
        with getConnection().cursor() as cursor:
            unassigned_stores = []
            # get_unassigned_active_own_store_for_manager_query = f"""SELECT o.store_id, o.store_name FROM own_store AS o
            # LEFT JOIN own_store_employees e ON o.store_id = e.assigned_store_id WHERE (e.employee_id IS NULL OR e.role
            #  <> 1 OR e.assigned_store_id = 0) AND o.status = 1 GROUP BY o.store_id"""

            get_unassigned_active_own_store_for_manager_query = f"""SELECT os.store_id, os.store_name
                    FROM own_store os
                    LEFT JOIN own_store_employees ose ON os.store_id = ose.assigned_store_id AND ose.role = 1
                    WHERE ose.assigned_store_id IS NULL AND os.status = 1 """

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


def get_active_own_stores():
    try:
        with getConnection().cursor() as cursor:
            unassigned_stores = []
            get_unassigned_active_own_store_for_manager_query = f"""SELECT o.store_id, o.store_name FROM own_store o 
            WHERE o.status = 1;"""
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


def get_own_store_by_id(sid):
    try:
        with getConnection().cursor() as cursor:
            get_own_stores_query = f""" SELECT own_store.*, own_store_employees.ose_name, own_store_employees.ose_employee_id,
                                    creator.admin_name, updater.admin_name
                                    FROM own_store
                                    LEFT JOIN admin AS creator ON own_store.os_created_by = creator.admin_admin_id
                                    LEFT JOIN admin AS updater ON own_store.os_last_updated_by = updater.admin_admin_id
                                    LEFT JOIN own_store_employees ON own_store.os_store_id = own_store_employees.ose_assigned_store_id AND own_store_employees.ose_role = 1 
                                    WHERE own_store.os_store_id = '{sid}' GROUP BY own_store.os_store_id """
            cursor.execute(get_own_stores_query)
            stores_data = cursor.fetchall()
            return {
                       "status": True,
                       "own_stores": stores_data
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_own_store_by_id(store_obj):
    cleaned_str = store_obj.store_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    store_lat, store_lng = map(float, cleaned_str.split(', '))
    try:
        with getConnection().cursor() as cursor:
            update_own_store_query = f"""
                UPDATE own_store
                SET 
                    store_zip = '{store_obj.store_zip_code}',
                    store_name = '{store_obj.store_name}',
                    store_display_name = '{store_obj.store_display_name}',
                    store_phone = '{store_obj.store_phone}',
                    store_gst = '{store_obj.store_gstin}',
                    store_email = '{store_obj.store_email}',
                    store_city = '{store_obj.store_city}',
                    store_state = '{store_obj.store_state}',
                    store_lat = '{store_lat}',
                    store_lng = '{store_lng}',
                    store_address = '{store_obj.complete_address}',
                    last_updated_on = '{getIndianTime()}',
                    last_updated_by = {store_obj.last_updated_by}
                WHERE store_id = {store_obj.store_id}
            """

            cursor.execute(update_own_store_query)
            connection.commit()  # Commit the transaction after executing the update query

            return {
                       "status": True,
                       "message": "Own store updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_own_store(sid, status):
    try:
        with getConnection().cursor() as cursor:
            update_sub_admin_query = f"""
                UPDATE own_store
                SET
                    os_status = {status}
                WHERE
                    os_store_id = {sid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_sub_admin_query)

            return {
                       "status": True,
                       "message": "Own Store updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_own_storestore_stats(ownStoreId):
    try:
        with getConnection().cursor() as cursor:
            employee_count_sql_query = f"""SELECT COUNT(*) FROM own_store_employees 
                                            WHERE ose_assigned_store_id = {ownStoreId} AND ose_status = 1"""
            cursor.execute(employee_count_sql_query)
            total_employee_count = cursor.fetchone()
            employee_count = total_employee_count['COUNT(*)'] if total_employee_count['COUNT(*)'] is not None else 0

            customer_count_sql_query = f"""SELECT COUNT(*) FROM customers WHERE customer_created_by_store_id = {ownStoreId} 
                                        AND customer_created_by_store_type = 1 """
            cursor.execute(customer_count_sql_query)
            total_customer_count = cursor.fetchone()
            customer_count = total_customer_count['COUNT(*)'] if total_customer_count['COUNT(*)'] is not None else 0

            return {
                       "status": True,
                       "total_employee_count": employee_count,
                       "total_customer_count": customer_count
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
