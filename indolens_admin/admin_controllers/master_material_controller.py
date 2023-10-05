import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.master_material_resp_model import get_product_materials

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def add_master_material(material_obj):
    try:
        with connection.cursor() as cursor:
            create_material_query = f"""
                INSERT INTO product_materials (
                    material_id, material_name,  material_description, 
                    status, created_on, created_by, last_updated_on, last_updated_by
                ) 
                VALUES (
                    '{material_obj.material_id}', '{material_obj.material_name}',
                    '{material_obj.material_description}',
                    '{material_obj.status}', '{today}',
                    '{material_obj.created_by}', '{today}',
                    '{material_obj.last_updated_by}'
                )
            """

            cursor.execute(create_material_query)
            return {
                "status": True,
                "message": "Frame Material added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_all_central_inventory_materials():
    try:
        with connection.cursor() as cursor:
            get_material_query = f""" SELECT pm.* , creator.name, updater.name
            FROM product_materials AS pm
            LEFT JOIN admin AS creator ON pm.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON pm.last_updated_by = updater.admin_id
            """
            cursor.execute(get_material_query)
            material_data = cursor.fetchall()
            print(material_data)

            return {
                "status": True,
                "frame_material": get_product_materials(material_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_master_material(mid, status):
    try:
        with connection.cursor() as cursor:
            set_material_query = f"""
            UPDATE product_materials SET status = '{status}' WHERE material_id = '{mid}';
            """
            cursor.execute(set_material_query)

            return {
                "status": True,
                "message": "Updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
