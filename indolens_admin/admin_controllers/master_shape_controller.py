import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.master_shapes_resp_model import get_frame_shapes

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def add_frame_shape(shape_obj):
    try:
        with connection.cursor() as cursor:
            create_shape_query = f"""
                INSERT INTO frame_shapes (
                    shape_id, shape_name,  shape_description, 
                    status, created_on, created_by, last_updated_on, last_updated_by
                ) 
                VALUES (
                    '{shape_obj.shape_id}', '{shape_obj.shape_name}',
                    '{shape_obj.shape_description}',
                    '{shape_obj.status}', '{today}',
                    '{shape_obj.created_by}', '{today}',
                    '{shape_obj.last_updated_by}'
                )
            """

            cursor.execute(create_shape_query)
            return {
                "status": True,
                "message": "Frame Shape added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_central_inventory_shapes():
    try:
        with connection.cursor() as cursor:
            get_product_shape_query = f""" SELECT fs.* , creator.name, updater.name
            FROM frame_shapes AS fs 
            LEFT JOIN admin AS creator ON fs.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON fs.last_updated_by = updater.admin_id
            """
            cursor.execute(get_product_shape_query)
            shapes_data = cursor.fetchall()
            print(shapes_data)

            return {
                "status": True,
                "product_shape": get_frame_shapes(shapes_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301