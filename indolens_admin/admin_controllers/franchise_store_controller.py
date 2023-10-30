import datetime

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.franchise_store_resp_model import get_franchise_store

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_franchise_store(franchise_obj):
    cleaned_str = franchise_obj.store_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    store_lat, store_lng = map(float, cleaned_str.split(', '))
    try:
        with connection.cursor() as cursor:
            create_franchise_store_query = f"""
                                        INSERT INTO franchise_store (
                                            store_zip, store_name, store_display_name, store_phone, store_gst, store_email,
                                            store_city, store_state, store_lat, store_lng, store_address,
                                            status, created_by, created_on, last_updated_by, last_updated_on ) 
                                        VALUES ('{franchise_obj.store_zip_code}', '{franchise_obj.store_name}', 
                                                '{franchise_obj.store_display_name}', '{franchise_obj.store_phone}', 
                                                '{franchise_obj.store_gstin}', '{franchise_obj.store_email}', 
                                                '{franchise_obj.store_city}', '{franchise_obj.store_state}', '{store_lat}',
                                                '{store_lng}', '{franchise_obj.complete_address}', 1, {franchise_obj.created_by}, 
                                                '{today}', {franchise_obj.last_updated_by}, '{today}')"""

            cursor.execute(create_franchise_store_query)
            return {
                       "status": True,
                       "message": "franchise store added"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_franchise_stores():
    try:
        with connection.cursor() as cursor:
            get_own_stores_query = f""" SELECT franchise_store.*, franchise_store_employees.name, 
                                        franchise_store_employees.employee_id FROM franchise_store
                                        LEFT JOIN franchise_store_employees ON 
                                        franchise_store.store_id = franchise_store_employees.assigned_store_id AND 
                                        franchise_store_employees.role = 1"""
            cursor.execute(get_own_stores_query)
            stores_data = cursor.fetchall()
            return {
                       "status": True,
                       "franchise_store": get_franchise_store(stores_data)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_store_by_id(fid):
    try:
        with connection.cursor() as cursor:
            get_own_stores_query = f""" SELECT * FROM franchise_store WHERE store_id = '{fid}'"""
            cursor.execute(get_own_stores_query)
            stores_data = cursor.fetchall()
            return {
                       "status": True,
                       "franchise_store": get_franchise_store(stores_data)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_franchise_store_by_id(franchise_obj):
    cleaned_str = franchise_obj.store_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    store_lat, store_lng = map(float, cleaned_str.split(', '))
    try:
        with connection.cursor() as cursor:
            update_own_store_query = f"""
                    UPDATE franchise_store
                    SET 
                        store_zip = '{franchise_obj.store_zip_code}',
                        store_name = '{franchise_obj.store_name}',
                        store_display_name = '{franchise_obj.store_display_name}',
                        store_phone = '{franchise_obj.store_phone}',
                        store_gst = '{franchise_obj.store_gstin}',
                        store_email = '{franchise_obj.store_email}',
                        store_city = '{franchise_obj.store_city}',
                        store_state = '{franchise_obj.store_state}',
                        store_lat = '{store_lat}',
                        store_lng = '{store_lng}',
                        store_address = '{franchise_obj.complete_address}',
                        last_updated_on = '{today}',
                        last_updated_by = {franchise_obj.last_updated_by}
                    WHERE store_id = {franchise_obj.store_id}
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


def enable_disable_franchise_store(fid, status):
    try:
        with connection.cursor() as cursor:
            update_franchise_store_query = f"""
                UPDATE franchise_store
                SET
                    status = {status}
                WHERE
                    store_id = {fid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_franchise_store_query)

            return {
                       "status": True,
                       "message": "Franchise Store updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
