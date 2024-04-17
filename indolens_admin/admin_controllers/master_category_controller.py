import datetime

import pymysql
import pytz

from indolens.db_connection import getConnection
from indolens_admin.admin_models.admin_resp_model.master_category_resp_model import get_product_categories

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def add_product_category(product_cat_obj):
    try:
        with getConnection().cursor() as cursor:
            create_category_query = f"""
                INSERT INTO product_categories (
                    pc_category_name, pc_category_prefix, pc_category_description, 
                    pc_status, pc_created_on, pc_created_by, pc_last_updated_on, pc_last_updated_by
                ) 
                VALUES (
                    '{product_cat_obj.category_name}',
                    '{product_cat_obj.category_prefix}', '{product_cat_obj.category_description}',
                    0, '{getIndianTime()}',
                    '{product_cat_obj.created_by}', '{getIndianTime()}',
                    '{product_cat_obj.last_updated_by}'
                )
            """

            cursor.execute(create_category_query)
            return {
                "status": True,
                "message": "Product category added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_product_category(product_cat_obj):
    try:
        with getConnection().cursor() as cursor:
            update_category_query = f"""
                UPDATE  product_categories SET  
                    pc_category_name = '{product_cat_obj.category_name}', 
                    pc_category_prefix = '{product_cat_obj.category_prefix}', 
                    pc_category_description = '{product_cat_obj.category_description}', 
                    pc_last_updated_on = '{getIndianTime()}' , pc_last_updated_by = '{product_cat_obj.last_updated_by}'
                    WHERE pc_category_id = {product_cat_obj.category_id}
            """

            cursor.execute(update_category_query)
            return {
                "status": True,
                "message": "Product category updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)},301


def get_all_central_inventory_category():

    try:
        with getConnection().cursor() as cursor:
            get_product_category_query = f""" 
            SELECT 
                pc_category_id, 
                pc_category_name, 
                pc_category_prefix, 
                pc_category_description,
                pc_status, 
                CASE 
                    WHEN pc_status = 1 THEN 'Active'
                    ELSE 'Inactive'
                END AS status,
                DATE_FORMAT(pc_created_on, '%d/%m/%Y %h:%i %p') AS pc_created_on, 
                DATE_FORMAT(pc_last_updated_on, '%d/%m/%Y %h:%i %p') AS pc_last_updated_on, 
                creator.admin_name AS Creator, 
                updater.admin_name AS Updater
            FROM 
                product_categories AS pc 
            LEFT JOIN 
                admin AS creator ON pc.pc_created_by = creator.admin_admin_id
            LEFT JOIN 
                admin AS updater ON pc.pc_last_updated_by = updater.admin_admin_id 
            ORDER BY 
                pc.pc_category_id ASC
            """
            cursor.execute(get_product_category_query)
            product_category = cursor.fetchall()
            return {
                "status": True,
                "product_category": product_category
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_product_category(cid, status):
    try:
        with getConnection().cursor() as cursor:
            set_product_category_query = f"""
            UPDATE product_categories SET pc_status = '{status}' WHERE pc_category_id = '{cid}';
            """
            cursor.execute(set_product_category_query)

            return {
                "status": True,
                "message": "Updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_central_inventory_category_by_id(categoryId):
    try:
        with getConnection().cursor() as cursor:
            get_product_category_query = f""" SELECT pc.* , creator.admin_name, updater.admin_name
            FROM product_categories AS pc 
            LEFT JOIN admin AS creator ON pc.pc_created_by = creator.admin_admin_id
            LEFT JOIN admin AS updater ON pc.pc_last_updated_by = updater.admin_admin_id
            WHERE pc.pc_category_id = {categoryId}"""
            cursor.execute(get_product_category_query)
            product_category = cursor.fetchall()

            return {
                "status": True,
                "product_category": product_category
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
