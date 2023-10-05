import datetime

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.own_store_resp_model import get_own_store

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_own_store(store_obj):
    cleaned_str = store_obj.store_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    store_lat, store_lng = map(float, cleaned_str.split(', '))
    try:
        with connection.cursor() as cursor:
            create_own_store_query = f"""
                                    INSERT INTO own_store (
                                        store_zip, store_name, store_display_name, store_phone, store_gst, store_email,
                                        store_city, store_state, store_lat, store_lng, store_address,
                                        status, created_by, created_on, last_updated_by, last_updated_on ) 
                                    VALUES ('{store_obj.store_zip_code}', '{store_obj.store_name}', 
                                            '{store_obj.store_display_name}', '{store_obj.store_phone}', 
                                            '{store_obj.store_gstin}', '{store_obj.store_email}', 
                                            '{store_obj.store_city}', '{store_obj.store_state}', '{store_lat}',
                                            '{store_lng}', '{store_obj.complete_address}', 1, {store_obj.created_by}, 
                                            '{today}', {store_obj.last_updated_by}, '{today}')"""

            cursor.execute(create_own_store_query)
            return {
                       "status": True,
                       "message": "own store added"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_own_stores():
    try:
        with connection.cursor() as cursor:
            get_own_stores_query = f""" SELECT * FROM own_store """
            cursor.execute(get_own_stores_query)
            stores_data = cursor.fetchall()
            return {
                       "status": True,
                       "own_stores": get_own_store(stores_data)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_own_store_by_id(sid):
    try:
        with connection.cursor() as cursor:
            get_own_stores_query = f""" SELECT * FROM own_store WHERE store_id = '{sid}'"""
            cursor.execute(get_own_stores_query)
            stores_data = cursor.fetchall()
            return {
                       "status": True,
                       "own_stores": get_own_store(stores_data)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_own_store_by_id(store_obj):
    cleaned_str = store_obj.store_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    store_lat, store_lng = map(float, cleaned_str.split(', '))
    try:
        with connection.cursor() as cursor:
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
                    last_updated_on = '{today}',
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
        with connection.cursor() as cursor:
            update_sub_admin_query = f"""
                UPDATE own_store
                SET
                    status = {status}
                WHERE
                    store_id = {sid}
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
