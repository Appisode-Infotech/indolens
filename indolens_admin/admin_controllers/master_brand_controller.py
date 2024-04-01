import pymysql
from indolens.db_connection import getConnection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.master_brand_resp_model import get_brands

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def add_product_brand(brand_obj):
    try:
        with getConnection().cursor() as cursor:
            create_brand_query = f"""
                INSERT INTO brands (
                    brand_name, brand_category_id, brand_description, 
                    brand_status, brand_created_on, brand_created_by, brand_last_updated_on, brand_last_updated_by
                ) 
                VALUES (
                    '{brand_obj.brand_name}',
                    0, '{brand_obj.brand_description}',
                    0, '{getIndianTime()}',
                    '{brand_obj.created_by}', '{getIndianTime()}',
                    '{brand_obj.last_updated_by}'
                )
            """

            cursor.execute(create_brand_query)
            return {
                "status": True,
                "message": "Brand added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def edit_product_brand(brand_obj):
    try:
        with getConnection().cursor() as cursor:
            update_brand_query = f"""
                UPDATE  brands SET
                    brand_name = '{brand_obj.brand_name}', 
                    brand_description = '{brand_obj.brand_description}', 
                    brand_last_updated_on = '{getIndianTime()}', brand_last_updated_by = '{brand_obj.last_updated_by}'
                    WHERE brand_brand_id = {brand_obj.brand_id}
            """

            cursor.execute(update_brand_query)
            return {
                "status": True,
                "message": "Brand updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_all_central_inventory_brand():
    try:
        with getConnection().cursor() as cursor:
            get_product_brand_query = f""" SELECT br.* , creator.admin_name, updater.admin_name
            FROM brands AS br 
            LEFT JOIN admin AS creator ON br.brand_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON br.brand_last_updated_by = updater.admin_admin_id
            ORDER BY br.brand_brand_id ASC
            """
            cursor.execute(get_product_brand_query)
            brand_data = cursor.fetchall()

            return {
                "status": True,
                "product_brand": brand_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_product_brand(bid, status):
    try:
        with getConnection().cursor() as cursor:
            set_product_brand_query = f"""
            UPDATE brands SET brand_status = '{status}' WHERE brand_brand_id = '{bid}';
            """
            cursor.execute(set_product_brand_query)

            return {
                "status": True,
                "message": "Updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_central_inventory_brand_by_id(brandId):
    try:
        with getConnection().cursor() as cursor:
            get_product_brand_query = f""" SELECT br.* , creator.admin_name, updater.admin_name
            FROM brands AS br 
            LEFT JOIN admin AS creator ON br.brand_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON br.brand_last_updated_by = updater.admin_admin_id
            WHERE br.brand_brand_id = {brandId}
            """
            cursor.execute(get_product_brand_query)
            brand_data = cursor.fetchall()

            return {
                "status": True,
                "product_brand": brand_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301