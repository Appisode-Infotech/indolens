import pymysql
from indolens.db_connection import getConnection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.master_material_resp_model import get_product_materials

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def add_master_material(material_obj):
    try:
        with getConnection().cursor() as cursor:
            create_material_query = f"""
                INSERT INTO product_materials (
                    pm_material_name, pm_material_description, 
        pm_status, pm_created_on, pm_created_by, pm_last_updated_on, pm_last_updated_by
                ) 
                VALUES (
                    '{material_obj.material_name}',
                    '{material_obj.material_description}',
                    0, '{getIndianTime()}',
                    '{material_obj.created_by}', '{getIndianTime()}',
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

def edit_master_material(material_obj):
    print(vars(material_obj))
    try:
        with getConnection().cursor() as cursor:
            update_material_query = f"""
                UPDATE product_materials SET
                    pm_material_name = '{material_obj.material_name}',  
                    pm_material_description = '{material_obj.material_description}', 
                    pm_last_updated_on = '{getIndianTime()}', 
                    pm_last_updated_by = '{material_obj.last_updated_by}'
                WHERE pm_material_id = {material_obj.material_id}
            """

            cursor.execute(update_material_query)
            return {
                "status": True,
                "message": "Frame Material updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_all_central_inventory_materials():
    try:
        with getConnection().cursor() as cursor:
            get_material_query = f""" SELECT pm.* , creator.admin_name, updater.admin_name
            FROM product_materials AS pm
            LEFT JOIN admin AS creator ON pm.pm_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON pm.pm_last_updated_by = updater.admin_admin_id
            ORDER BY pm.pm_material_id ASC
            """
            cursor.execute(get_material_query)
            material_data = cursor.fetchall()

            return {
                "status": True,
                "frame_material": material_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_master_material(mid, status):
    try:
        with getConnection().cursor() as cursor:
            set_material_query = f"""
            UPDATE product_materials SET pm_status = '{status}' WHERE pm_material_id = '{mid}';
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


def get_central_inventory_materials_by_id(materialId):
    try:
        with getConnection().cursor() as cursor:
            get_material_query = f""" SELECT pm.* , creator.admin_name, updater.admin_name
            FROM product_materials AS pm
            LEFT JOIN admin AS creator ON pm.pm_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON pm.pm_last_updated_by = updater.admin_admin_id
            WHERE pm.pm_material_id = {materialId}
            """
            cursor.execute(get_material_query)
            material_data = cursor.fetchone()

            return {
                "status": True,
                "product_material": material_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301