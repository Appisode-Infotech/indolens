import datetime
import json

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_controllers.master_category_controller import get_all_central_inventory_category
from indolens_admin.admin_models.admin_resp_model.central_inventory_product_resp_model import get_products
from indolens_admin.admin_models.admin_resp_model.master_brand_resp_model import get_brands
from indolens_admin.admin_models.admin_resp_model.master_category_resp_model import get_product_categories
from indolens_admin.admin_models.admin_resp_model.master_color_resp_model import get_product_colors
from indolens_admin.admin_models.admin_resp_model.master_frame_type_resp_model import get_frame_types
from indolens_admin.admin_models.admin_resp_model.master_material_resp_model import get_product_materials
from indolens_admin.admin_models.admin_resp_model.master_shapes_resp_model import get_frame_shapes
from indolens_admin.admin_models.admin_resp_model.master_units_resp_model import get_master_units
from indolens_admin.admin_models.admin_resp_model.product_request_list_resp_model import get_request_product_list
from indolens_admin.admin_models.admin_resp_model.store_inventory_product_resp_model import get_store_stocks

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_all_active_types():
    try:
        with connection.cursor() as cursor:
            get_product_category_query = f""" SELECT pc.* , creator.name, updater.name
                           FROM product_categories AS pc 
                           LEFT JOIN admin AS creator ON pc.created_by = creator.admin_id
                           LEFT JOIN admin AS updater ON pc.last_updated_by = updater.admin_id
                           WHERE pc.status = 1
                           """
            get_product_brand_query = f""" SELECT br.* , creator.name, updater.name
                           FROM brands AS br 
                           LEFT JOIN admin AS creator ON br.created_by = creator.admin_id
                           LEFT JOIN admin AS updater ON br.last_updated_by = updater.admin_id
                           WHERE br.status = 1
                           """
            get_material_query = f""" SELECT pm.* , creator.name, updater.name
                            FROM product_materials AS pm
                            LEFT JOIN admin AS creator ON pm.created_by = creator.admin_id
                            LEFT JOIN admin AS updater ON pm.last_updated_by = updater.admin_id
                            WHERE pm.status = 1
                            """
            get_frame_types_query = f""" SELECT ft.* , creator.name, updater.name
                            FROM frame_types AS ft
                            LEFT JOIN admin AS creator ON ft.created_by = creator.admin_id
                            LEFT JOIN admin AS updater ON ft.last_updated_by = updater.admin_id
                            WHERE ft.status = 1 
                            """
            get_product_shape_query = f""" SELECT fs.* , creator.name, updater.name
                           FROM frame_shapes AS fs 
                           LEFT JOIN admin AS creator ON fs.created_by = creator.admin_id
                           LEFT JOIN admin AS updater ON fs.last_updated_by = updater.admin_id
                           WHERE fs.status = 1
                           """
            get_frame_color_query = f""" SELECT pc.* , creator.name, updater.name
                            FROM product_colors AS pc
                            LEFT JOIN admin AS creator ON pc.created_by = creator.admin_id
                            LEFT JOIN admin AS updater ON pc.last_updated_by = updater.admin_id
                            WHERE pc.status = 1
                            """
            get_units_query = f""" SELECT u.*, creator.name, updater.name 
                                                           FROM units AS u
                                                            LEFT JOIN admin AS creator ON u.created_by = creator.admin_id
                                                            LEFT JOIN admin AS updater ON u.last_updated_by = updater.admin_id
                                                            WHERE u.status = 1
                                                            """
            cursor.execute(get_product_category_query)
            product_categories = get_product_categories(cursor.fetchall())
            cursor.execute(get_product_brand_query)
            product_brands = get_brands(cursor.fetchall())
            cursor.execute(get_material_query)
            product_materials = get_product_materials(cursor.fetchall())
            cursor.execute(get_frame_types_query)
            frame_types = get_frame_types(cursor.fetchall())
            cursor.execute(get_product_shape_query)
            frame_shapes = get_frame_shapes(cursor.fetchall())
            cursor.execute(get_frame_color_query)
            colors = get_product_colors(cursor.fetchall())
            cursor.execute(get_units_query)
            master_units = get_master_units(cursor.fetchall())
            return {
                       "status": True,
                       "product_categories": product_categories,
                       "product_brands": product_brands,
                       "product_materials": product_materials,
                       "frame_types": frame_types,
                       "frame_shapes": frame_shapes,
                       "colors": colors,
                       "master_units": master_units,
                   }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def add_central_inventory_products(product_obj, file):
    try:
        with connection.cursor() as cursor:
            add_product_query = f""" INSERT INTO central_inventory 
                                                (product_name, product_description, product_images, 
                                                category_id, brand_id, material_id, frame_type_id, frame_shape_id, 
                                                color_id, unit_id, origin, cost_price, sale_price, model_number, hsn, 
                                                created_on, created_by, last_updated_on, last_updated_by, 
                                                product_quantity, product_gst) 
                                                VALUES ('{product_obj.product_title}','{product_obj.product_description}',
                                                '{json.dumps(file.product_img)}','{product_obj.category_id}',
                                                '{product_obj.brand_id}','{product_obj.material_id}',
                                                '{product_obj.frame_type_id}','{product_obj.frame_shape_id}',
                                                '{product_obj.color_id}','{product_obj.unit_id}','{product_obj.origin}',
                                                '{product_obj.cost_price}','{product_obj.sale_price}', 
                                                '{product_obj.model_number}', '{product_obj.hsn_number}',
                                                '{today}','{product_obj.created_by}','{today}',
                                                '{product_obj.last_updated_by}', '{product_obj.product_quantity}', 
                                                '{product_obj.product_gstin}') """

            cursor.execute(add_product_query)
            productId = cursor.lastrowid
            return {
                       "status": True,
                       "productId": productId
                   }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_central_inventory_products(status):
    try:
        status_conditions = {
            "All": "LIKE '%'",
            "Active": "= 1",
            "Inactive": "= 0"
        }
        status_condition = status_conditions[status]
        with connection.cursor() as cursor:
            get_all_product_query = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name
                                    FROM central_inventory As ci
                                    LEFT JOIN admin AS creator ON ci.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON ci.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id
                                    WHERE ci.status {status_condition} """

            cursor.execute(get_all_product_query)
            product_list = cursor.fetchall()
            return {
                       "status": True,
                       "product_list": get_products(product_list),
                       "categoriesList": get_all_central_inventory_category()[0]['product_category']
                   }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_out_of_stock_central_inventory_products(quantity):
    try:
        with connection.cursor() as cursor:
            get_all_product_query = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name
                                    FROM central_inventory As ci
                                    LEFT JOIN admin AS creator ON ci.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON ci.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id
                                    WHERE ci.product_quantity <= '{quantity}'"""

            cursor.execute(get_all_product_query)
            stocks_list = cursor.fetchall()
            return {
                       "status": True,
                       "stocks_list": get_products(stocks_list),
                       "categories_list": get_all_central_inventory_category()[0]['product_category']
                   }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_out_of_stock_products_for_store(quantity):
    try:
        with connection.cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT si.*, ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name,
                                    CASE
                                        WHEN si.store_type = 1 THEN os.store_name
                                        ELSE fstore.store_name
                                    END AS store_name
                                    FROM store_inventory As si
                                    LEFT JOIN central_inventory AS ci ON ci.product_id = si.product_id
                                    LEFT JOIN admin AS creator ON si.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON si.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id
                                    LEFT JOIN own_store os ON si.store_id = os.store_id AND si.store_type = 1
                                    LEFT JOIN franchise_store fstore ON si.store_id = fstore.store_id AND si.store_type = 2;
                                    WHERE si.product_quantity <= '{quantity}'"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                       "status": True,
                       "stocks_list": get_store_stocks(product_list)
                   }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_stock_requests(status):
    try:
        with connection.cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT rp.*, ci.*, creator.name, updater.name, pc.category_name, 
                                    pm.material_name, ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name,
                                    CASE
                                        WHEN rp.store_type = 1 THEN os.store_name
                                        ELSE fstore.store_name
                                    END AS store_name,
                                    from_store.store_name
                                    FROM request_products As rp
                                    LEFT JOIN central_inventory AS ci ON ci.product_id = rp.product_id
                                    LEFT JOIN admin AS creator ON rp.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON rp.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id 
                                    LEFT JOIN own_store os ON rp.store_id = os.store_id AND rp.store_type = 1
                                    LEFT JOIN own_store AS from_store ON rp.request_to_store_id = from_store.store_id
                                    LEFT JOIN franchise_store fstore ON rp.store_id = fstore.store_id AND rp.store_type = 2
                                    WHERE rp.request_status LIKE '{status}'"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                       "status": True,
                       "stocks_request_list": get_request_product_list(product_list)
                   }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def change_stock_request_status(requestId, status, updator):
    try:
        with connection.cursor() as cursor:
            fetch_req_product_query = f"""SELECT * FROM request_products 
                        WHERE request_products_id = '{requestId}'"""
            cursor.execute(fetch_req_product_query)
            product_details = cursor.fetchone()
            quantity = product_details[4]

            fetch_inventory_product_query = f"""SELECT product_quantity FROM central_inventory 
                        WHERE product_id = {product_details[3]} """
            cursor.execute(fetch_inventory_product_query)
            available_quantity = cursor.fetchone()[0]

            if status == 1:
                if available_quantity > quantity:
                    update_stock_request_query = f"""UPDATE request_products SET request_status = '{status}' 
                    WHERE request_products_id = '{requestId}' """
                    cursor.execute(update_stock_request_query)

                    update_central_Inventory = f"""UPDATE central_inventory SET product_quantity = product_quantity - {quantity} 
                                                                        WHERE product_id = {product_details[3]}"""
                    cursor.execute(update_central_Inventory)

                    update_store_Inventory = f"""INSERT INTO store_inventory 
                                                                   (store_id, store_type, product_id, product_quantity, created_on, 
                                                                   created_by, last_updated_on, last_updated_by) 
                                                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                                                   ON DUPLICATE KEY UPDATE
                                                                   product_quantity = product_quantity + {quantity}, 
                                                                   last_updated_on = '{today}', 
                                                                   last_updated_by = {updator}"""

                    cursor.execute(update_store_Inventory, (product_details[1], product_details[2], product_details[3],
                                                            product_details[4], today, updator, today, updator))

                    return {
                               "status": True,
                               "message": "Status Changed"
                           }, 200

                else:
                    return {
                               "status": False,
                               "message": f"The requested quantity is {quantity} and available quantity is {available_quantity} in inventory"
                           }, 200
            else:
                update_stock_request_query = f"""UPDATE request_products SET request_status = '{status}' 
                                    WHERE request_products_id = '{requestId}' """
                cursor.execute(update_stock_request_query)
                return {
                           "status": True,
                           "message": "Status Changed"
                       }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
