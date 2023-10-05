import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.master_brand_resp_model import get_brands

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def add_product_brand(brand_obj):
    try:
        with connection.cursor() as cursor:
            create_brand_query = f"""
                INSERT INTO brands (
                    brand_id, brand_name, category_id, brand_description, 
                    status, created_on, created_by, last_updated_on, last_updated_by
                ) 
                VALUES (
                    '{brand_obj.brand_id}', '{brand_obj.brand_name}',
                    '{brand_obj.category_id}', '{brand_obj.brand_description}',
                    '{brand_obj.status}', '{today}',
                    '{brand_obj.created_by}', '{today}',
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

def get_all_central_inventory_brand():
    try:
        with connection.cursor() as cursor:
            get_product_brand_query = f""" SELECT br.* , creator.name, updater.name, category.category_name
            FROM brands AS br 
            LEFT JOIN admin AS creator ON br.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON br.last_updated_by = updater.admin_id
            LEFT JOIN product_categories AS category ON br.category_id = category.category_id"""
            cursor.execute(get_product_brand_query)
            brand_data = cursor.fetchall()
            print(brand_data)

            return {
                "status": True,
                "product_brand": get_brands(brand_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_product_brand(bid, status):
    try:
        with connection.cursor() as cursor:
            set_product_brand_query = f"""
            UPDATE brands SET status = '{status}' WHERE brand_id = '{bid}';
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