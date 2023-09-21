import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.lab_resp_model import get_labs

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_lab(lab_obj):
    cleaned_str = lab_obj.lab_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    lab_lat, lab_lng = map(float, cleaned_str.split(', '))
    try:
        with connection.cursor() as cursor:
            create_lab_query = f"""
                                    INSERT INTO lab (
                                        lab_name, lab_display_name, lab_phone, lab_gst, lab_email,
                                        lab_city, lab_state, lab_zip, lab_lat, lab_lng, lab_address,
                                        status, created_by, created_on, last_updated_by, last_updated_on) 
                                    VALUES ('{lab_obj.lab_name}', '{lab_obj.lab_display_name}', 
                                            '{lab_obj.lab_phone}', '{lab_obj.lab_gstin}', 
                                            '{lab_obj.lab_email}', '{lab_obj.lab_city}', 
                                            '{lab_obj.lab_state}', '{lab_obj.lab_zip_code}', '{lab_lat}',
                                            '{lab_lng}', '{lab_obj.complete_address}', 1, {lab_obj.created_by}, 
                                            '{today}', {lab_obj.last_updated_by}, '{today}')"""

            cursor.execute(create_lab_query)
            return {
                "status": True,
                "message": "lab added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_labs():
    try:
        with connection.cursor() as cursor:
            get_lab_query = f""" SELECT l.*, creator.name, updater.name, lt.name FROM lab AS l
                                LEFT JOIN lab_technician AS lt ON lt.assigned_lab_id = l.lab_id
                                LEFT JOIN admin AS creator ON l.created_by = creator.admin_id
                                LEFT JOIN admin AS updater ON l.last_updated_by = updater.admin_id"""
            cursor.execute(get_lab_query)
            lab_data = cursor.fetchall()
            return {
                "status": True,
                "lab_list": get_labs(lab_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_by_id(sid):
    try:
        with connection.cursor() as cursor:
            get_lab_data_query = f""" SELECT * FROM own_store WHERE store_id = '{sid}'"""
            cursor.execute(get_lab_data_query)
            lab_data = cursor.fetchall()
            return {
                "status": True,
                "lab_data": get_labs(lab_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_own_store_by_id(lab_obj):
    cleaned_str = lab_obj.store_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    store_lat, store_lng = map(float, cleaned_str.split(', '))
    try:
        with connection.cursor() as cursor:
            update_own_store_query = f"""
                UPDATE own_store
                SET 
                    store_zip = '{lab_obj.store_zip_code}',
                    store_name = '{lab_obj.store_name}',
                    store_display_name = '{lab_obj.store_display_name}',
                    store_phone = '{lab_obj.store_phone}',
                    store_gst = '{lab_obj.store_gstin}',
                    store_email = '{lab_obj.store_email}',
                    store_city = '{lab_obj.store_city}',
                    store_state = '{lab_obj.store_state}',
                    store_lat = '{store_lat}',
                    store_lng = '{store_lng}',
                    store_address = '{lab_obj.complete_address}',
                    last_updated_on = '{today}',
                    last_updated_by = {lab_obj.last_updated_by}
                WHERE store_id = {lab_obj.store_id}
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
