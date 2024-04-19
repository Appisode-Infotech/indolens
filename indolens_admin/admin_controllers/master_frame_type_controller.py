import pymysql
from indolens.db_connection import getConnection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.master_frame_type_resp_model import get_frame_types

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def add_frame_type(frame_obj):
    try:
        with getConnection().cursor() as cursor:
            create_shape_query = f"""
                INSERT INTO frame_types (
                    ftype_name,  ftype_description, 
                    ftype_status, ftype_created_on, ftype_created_by, ftype_last_updated_on, ftype_last_updated_by
                ) 
                VALUES (
                    '{frame_obj.frame_type_name}',
                    '{frame_obj.frame_type_description}',
                    0, '{getIndianTime()}',
                    '{frame_obj.created_by}', '{getIndianTime()}',
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
        with getConnection().cursor() as cursor:
            update_shape_query = f"""
                UPDATE  frame_types SET
                    ftype_name = '{frame_obj.frame_type_name}',  
                    ftype_description = '{frame_obj.frame_type_description}', 
                    ftype_last_updated_on = '{getIndianTime()}', ftype_last_updated_by = '{frame_obj.last_updated_by}'
                    WHERE ftype_frame_id = {frame_obj.frame_id}
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
        with getConnection().cursor() as cursor:
            get_frame_types_query = f""" SELECT  
            ft.ftype_frame_id, 
            ft.ftype_name, 
            ft.ftype_description, 
            ft.ftype_status, 
            CASE 
                WHEN ft.ftype_status = 1 THEN 'Active'
                ELSE 'Inactive'
            END AS Status,
            DATE_FORMAT(ft.ftype_created_on, '%d/%m/%Y %h:%i %p') AS ftype_created_on, 
            DATE_FORMAT(ft.ftype_last_updated_on, '%d/%m/%Y %h:%i %p') AS ftype_last_updated_on, 
            creator.admin_name AS creator, updater.admin_name AS updater
            FROM frame_types AS ft
            LEFT JOIN admin AS creator ON ft.ftype_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON ft.ftype_last_updated_by = updater.admin_admin_id
            ORDER BY ft.ftype_frame_id ASC
            """
            cursor.execute(get_frame_types_query)
            frame_type_data = cursor.fetchall()

            return {
                "status": True,
                "frame_type": frame_type_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_frame_type(tid, status):
    try:
        with getConnection().cursor() as cursor:
            set_frame_type_query = f"""
            UPDATE frame_types SET ftype_status = '{status}' WHERE ftype_frame_id = '{tid}';
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
        with getConnection().cursor() as cursor:
            get_frame_types_query = f""" SELECT ft.* , creator.admin_name, updater.admin_name
            FROM frame_types AS ft
            LEFT JOIN admin AS creator ON ft.ftype_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON ft.ftype_last_updated_by = updater.admin_admin_id
            WHERE ft.ftype_frame_id = {frameId}
            """
            cursor.execute(get_frame_types_query)
            frame_type_data = cursor.fetchall()

            return {
                "status": True,
                "frame_type": frame_type_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301