import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.master_frame_type_resp_model import get_frame_types

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def add_frame_type(frame_obj):
    try:
        with connection.cursor() as cursor:
            create_shape_query = f"""
                INSERT INTO frame_types (
                    frame_type_name,  frame_type_description, 
                    status, created_on, created_by, last_updated_on, last_updated_by
                ) 
                VALUES (
                    '{frame_obj.frame_type_name}',
                    '{frame_obj.frame_type_description}',
                    0, '{today}',
                    '{frame_obj.created_by}', '{today}',
                    '{frame_obj.last_updated_by}'
                )
            """

            cursor.execute(create_shape_query)
            return {
                "status": True,
                "message": "Frame Type added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def edit_frame_type(frame_obj):
    try:
        with connection.cursor() as cursor:
            update_shape_query = f"""
                UPDATE  frame_types SET
                    frame_type_name = '{frame_obj.frame_type_name}',  
                    frame_type_description = '{frame_obj.frame_type_description}', 
                    last_updated_on = '{today}', last_updated_by = '{frame_obj.last_updated_by}'
                    WHERE frame_id = {frame_obj.frame_id}
            """

            cursor.execute(update_shape_query)
            return {
                "status": True,
                "message": "Frame Type updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_central_inventory_frame_types():
    try:
        with connection.cursor() as cursor:
            get_frame_types_query = f""" SELECT ft.* , creator.name, updater.name
            FROM frame_types AS ft
            LEFT JOIN admin AS creator ON ft.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON ft.last_updated_by = updater.admin_id
            ORDER BY ft.frame_id ASC
            """
            cursor.execute(get_frame_types_query)
            frame_type_data = cursor.fetchall()

            return {
                "status": True,
                "frame_type": get_frame_types(frame_type_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_frame_type(tid, status):
    try:
        with connection.cursor() as cursor:
            set_frame_type_query = f"""
            UPDATE frame_types SET status = '{status}' WHERE frame_id = '{tid}';
            """
            cursor.execute(set_frame_type_query)

            return {
                "status": True,
                "message": "Updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_central_inventory_frame_types_by_id(frameId):
    try:
        with connection.cursor() as cursor:
            get_frame_types_query = f""" SELECT ft.* , creator.name, updater.name
            FROM frame_types AS ft
            LEFT JOIN admin AS creator ON ft.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON ft.last_updated_by = updater.admin_id
            WHERE ft.frame_id = {frameId}
            """
            cursor.execute(get_frame_types_query)
            frame_type_data = cursor.fetchall()

            return {
                "status": True,
                "frame_type": get_frame_types(frame_type_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301