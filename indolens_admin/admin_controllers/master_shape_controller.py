import pymysql
from indolens.db_connection import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.master_shapes_resp_model import get_frame_shapes

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def add_frame_shape(shape_obj):
    try:
        with connection.cursor() as cursor:
            create_shape_query = f"""
                INSERT INTO frame_shapes (
                    fshape_name,  fshape_description, 
                    fshape_status, fshape_created_on, fshape_created_by, fshape_last_updated_on, fshape_last_updated_by
                ) 
                VALUES (
                    '{shape_obj.shape_name}',
                    '{shape_obj.shape_description}',
                    0, '{getIndianTime()}',
                    '{shape_obj.created_by}', '{getIndianTime()}',
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

def edit_frame_shape(shape_obj):
    print(vars(shape_obj))
    try:
        with connection.cursor() as cursor:
            update_shape_query = f"""
                UPDATE  frame_shapes SET
                    fshape_name = '{shape_obj.shape_name}',  
                    fshape_description = '{shape_obj.shape_description}', 
                    fshape_last_updated_on = '{getIndianTime()}', fshape_last_updated_by = '{shape_obj.last_updated_by}'
                    WHERE fshape_shape_id = {shape_obj.shape_id}
                
            """

            cursor.execute(update_shape_query)
            return {
                "status": True,
                "message": "Frame Shape updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_central_inventory_shapes():
    try:
        with connection.cursor() as cursor:
            get_product_shape_query = f""" SELECT fs.* , creator.admin_name, updater.admin_name
            FROM frame_shapes AS fs 
            LEFT JOIN admin AS creator ON fs.fshape_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON fs.fshape_last_updated_by = updater.admin_admin_id
            ORDER BY fs.fshape_shape_id ASC
            """
            cursor.execute(get_product_shape_query)
            shapes_data = cursor.fetchall()

            return {
                "status": True,
                "product_shape": shapes_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_frame_shape(sid, status):
    try:
        with connection.cursor() as cursor:
            set_frame_shape_query = f"""
            UPDATE frame_shapes SET fshape_status = '{status}' WHERE fshape_shape_id = '{sid}';
            """
            cursor.execute(set_frame_shape_query)

            return {
                "status": True,
                "message": "Updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_central_inventory_shapes_by_id(shapeId):
    try:
        with connection.cursor() as cursor:
            get_product_shape_query = f""" SELECT fs.* , creator.admin_name, updater.admin_name
            FROM frame_shapes AS fs 
            LEFT JOIN admin AS creator ON fs.fshape_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON fs.fshape_last_updated_by = updater.admin_admin_id
            WHERE fs.fshape_shape_id = {shapeId}
            """
            cursor.execute(get_product_shape_query)
            shapes_data = cursor.fetchall()

            return {
                "status": True,
                "product_shape": shapes_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301