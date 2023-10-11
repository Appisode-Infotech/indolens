import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.master_color_resp_model import get_product_colors

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def add_master_color(color_obj):
    try:
        with connection.cursor() as cursor:
            create_color_query = f"""
                INSERT INTO product_colors (
                    color_id, color_code, color_name,  color_description, 
                    status, created_on, created_by, last_updated_on, last_updated_by
                ) 
                VALUES (
                    '{color_obj.color_id}','{color_obj.color_code}', '{color_obj.color_name}',
                    '{color_obj.color_description}',
                    '{color_obj.status}', '{today}',
                    '{color_obj.created_by}', '{today}',
                    '{color_obj.last_updated_by}'
                )
            """

            cursor.execute(create_color_query)
            return {
                "status": True,
                "message": "Frame Color added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_central_inventory_color():
    try:
        with connection.cursor() as cursor:
            get_frame_color_query = f""" SELECT pc.* , creator.name, updater.name
            FROM product_colors AS pc
            LEFT JOIN admin AS creator ON pc.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON pc.last_updated_by = updater.admin_id
            """
            cursor.execute(get_frame_color_query)
            frame_color_data = cursor.fetchall()
            print(frame_color_data)

            return {
                "status": True,
                "frame_color": get_product_colors(frame_color_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_master_color(mcid, status):
    try:
        with connection.cursor() as cursor:
            set_color_query = f"""
            UPDATE product_colors SET status = '{status}' WHERE color_id = '{mcid}';
            """
            cursor.execute(set_color_query)

            return {
                "status": True,
                "message": "Updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301