import datetime
import json

import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_models.admin_resp_model.master_category_resp_model import get_product_categories
from indolens_franchise_store.franchise_store_model.franchise_store_resp_model.franchise_store_inventory_product_resp_model import \
    get_franchise_store_inventory_stocks
from indolens_own_store.own_store_model.response_model.product_request_list_resp_model import get_request_product_list
from indolens_own_store.own_store_model.response_model.stock_request_product_resp_model import \
    get_products_for_stock_request

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def get_all_out_of_stock_products_for_franchise_store(quantity, store_id):
    try:
        with getConnection().cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT si.*, ci.*, creator.admin_name, updater.admin_name, 
                                                pc.pc_category_name, pm.pm_material_name,
                                                ft.ftype_name, fs.fshape_name,c.pcol_color_name, u.unit_name, b.brand_name,
                                                os.os_store_name, 
                                                JSON_UNQUOTE(JSON_EXTRACT(ci.ci_product_images, '$[0]')) AS product_images
                                                FROM store_inventory As si
                                                LEFT JOIN central_inventory AS ci ON ci.ci_product_id = si.si_product_id
                                                LEFT JOIN admin AS creator ON si.si_created_by = creator.admin_admin_id
                                                LEFT JOIN admin AS updater ON si.si_last_updated_by = updater.admin_admin_id
                                                LEFT JOIN product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                                                LEFT JOIN product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                                                LEFT JOIN frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                                                LEFT JOIN frame_shapes AS fs ON ci.ci_frame_shape_id = fs.fshape_shape_id
                                                LEFT JOIN product_colors AS c ON ci.ci_color_id = c.pcol_color_id
                                                LEFT JOIN units AS u ON ci.ci_unit_id = u.unit_unit_id
                                                LEFT JOIN brands AS b ON ci.ci_brand_id = b.brand_brand_id
                                                LEFT JOIN own_store AS os ON os.os_store_id = '{store_id}'
                                                WHERE si.si_product_quantity <= {quantity} AND si.si_store_id = '{store_id}' 
                                                AND si.si_store_type = 2
                                                ORDER BY si.si_store_inventory_id DESC"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()

            get_product_category_query = f""" SELECT pc.*
                                                FROM product_categories AS pc 
                                                ORDER BY pc.pc_category_id DESC"""
            cursor.execute(get_product_category_query)
            stores_data = cursor.fetchall()
            return {
                "status": True,
                "stocks_list": product_list,
                "product_category": stores_data
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e), "stocks_list": []}, 301
    except Exception as e:
        return {"status": False, "message": str(e), "stocks_list": []}, 301


def get_all_products_for_franchise_store(store_id):
    try:
        with getConnection().cursor() as cursor:
            get_all_store_stock_query = f""" SELECT si.*, ci.*, creator.admin_name AS creator, 
                                                updater.admin_name AS updater, pc.pc_category_name, pm.pm_material_name,
                                                ft.ftype_name, fsh.fshape_name,co.pcol_color_name, u.unit_name, b.brand_name,
                                                os.os_store_name, 
                                                JSON_UNQUOTE(JSON_EXTRACT(ci.ci_product_images, '$[0]')) AS product_images
                                                FROM store_inventory As si
                                                LEFT JOIN central_inventory AS ci ON ci.ci_product_id = si.si_product_id
                                                LEFT JOIN admin AS creator ON si.si_created_by = creator.admin_admin_id
                                                LEFT JOIN admin AS updater ON si.si_last_updated_by = updater.admin_admin_id
                                                LEFT JOIN product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                                                LEFT JOIN product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                                                LEFT JOIN frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                                                LEFT JOIN frame_shapes AS fsh ON ci.ci_frame_shape_id = fsh.fshape_shape_id
                                                LEFT JOIN product_colors AS co ON ci.ci_color_id = co.pcol_color_id
                                                LEFT JOIN units AS u ON ci.ci_unit_id = u.unit_unit_id
                                                LEFT JOIN brands AS b ON ci.ci_brand_id = b.brand_brand_id
                                                LEFT JOIN own_store AS os ON os.os_store_id = '{store_id}' 
                                                WHERE si.si_store_id = {store_id}  AND si.si_store_type = 2 AND ci.ci_category_id != 2 
                                                AND ci.ci_category_id != 3
                                                ORDER BY si.si_store_inventory_id DESC"""

            cursor.execute(get_all_store_stock_query)
            product_list = cursor.fetchall()

            get_product_category_query = f""" SELECT pc.*
                                    FROM product_categories AS pc 
                                    ORDER BY pc.pc_category_id DESC"""
            cursor.execute(get_product_category_query)
            product_category = cursor.fetchall()

            return {
                "status": True,
                "stocks_list": product_list,
                "product_category": product_category
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_products_for_franchise_store_by_id(store_id, productId):
    try:
        with getConnection().cursor() as cursor:
            get_all_store_stock_query = f""" SELECT si.*, ci.*, creator.admin_name AS creator, 
                                            updater.admin_name AS updater, pc.pc_category_name, pm.pm_material_name,
                                            ft.ftype_name, fsh.fshape_name,co.pcol_color_name, u.unit_name, b.brand_name,
                                            os.os_store_name
                                            FROM store_inventory As si
                                            LEFT JOIN central_inventory AS ci ON ci.ci_product_id = si.si_product_id
                                            LEFT JOIN admin AS creator ON si.si_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON si.si_last_updated_by = updater.admin_admin_id
                                            LEFT JOIN product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                                            LEFT JOIN product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                                            LEFT JOIN frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                                            LEFT JOIN frame_shapes AS fsh ON ci.ci_frame_shape_id = fsh.fshape_shape_id
                                            LEFT JOIN product_colors AS co ON ci.ci_color_id = co.pcol_color_id
                                            LEFT JOIN units AS u ON ci.ci_unit_id = u.unit_unit_id
                                            LEFT JOIN brands AS b ON ci.ci_brand_id = b.brand_brand_id
                                            LEFT JOIN own_store AS os ON os.os_store_id = '{store_id}' 
                                            WHERE si.si_store_id = {store_id}  AND si.si_store_type = 2 AND 
                                            si.si_store_inventory_id = {productId}
                                            ORDER BY si.si_store_inventory_id DESC"""

            cursor.execute(get_all_store_stock_query)
            product_data = cursor.fetchone()
            product_data['ci_power_attribute'] = json.loads(product_data['ci_power_attribute'])
            product_data['ci_product_images'] = json.loads(product_data['ci_product_images'])
            return {
                "status": True,
                "stocks_list": product_data,
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_central_inventory_products(store_id):
    try:
        with getConnection().cursor() as cursor:
            get_all_product_query = f""" SELECT ci.*, creator.admin_name, updater.admin_name, pc.pc_category_name, pm.pm_material_name,
                                                    ft.ftype_name, fs.fshape_name,c.pcol_color_name, u.unit_name, b.brand_name,
                                                    (SELECT si_product_quantity FROM store_inventory 
                                                     WHERE si_store_id = {store_id} AND si_store_type = 2
                                                     AND si_product_id = ci.ci_product_id) AS store_quantity, 
                                                    0 AS target_store_id, 0 AS target_store_name
                                                    FROM central_inventory As ci
                                                    LEFT JOIN admin AS creator ON ci.ci_created_by = creator.admin_admin_id
                                                    LEFT JOIN admin AS updater ON ci.ci_last_updated_by = updater.admin_admin_id
                                                    LEFT JOIN product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                                                    LEFT JOIN product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                                                    LEFT JOIN frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                                                    LEFT JOIN frame_shapes AS fs ON ci.ci_frame_shape_id = fs.fshape_shape_id
                                                    LEFT JOIN product_colors AS c ON ci.ci_color_id = c.pcol_color_id
                                                    LEFT JOIN units AS u ON ci.ci_unit_id = u.unit_unit_id
                                                    LEFT JOIN brands AS b ON ci.ci_brand_id = b.brand_brand_id
                                                    WHERE ci.ci_category_id != 2 AND ci.ci_category_id != 3
                                                    GROUP BY ci.ci_product_id ORDER BY ci.ci_product_id DESC """

            cursor.execute(get_all_product_query)
            product_list = cursor.fetchall()

            get_stores_product_query = f""" SELECT ci.*, creator.admin_name, updater.admin_name, pc.pc_category_name, pm.pm_material_name,
                                                            ft.ftype_name, fs.fshape_name,c.pcol_color_name, u.unit_name, b.brand_name, 
                                                            (SELECT si_product_quantity FROM store_inventory 
                                                             WHERE si_store_id = {store_id} AND si_store_type = 2 
                                                             AND si_product_id = ci.ci_product_id) AS store_quantity, 
                                                            store_products.si_store_id AS target_store_id , os.os_store_name AS target_store_name
                                                            FROM store_inventory AS store_products 
                                                            LEFT JOIN central_inventory As ci ON store_products.si_product_id = ci.ci_product_id
                                                            LEFT JOIN admin AS creator ON ci.ci_created_by = creator.admin_admin_id
                                                            LEFT JOIN admin AS updater ON ci.ci_last_updated_by = updater.admin_admin_id
                                                            LEFT JOIN product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                                                            LEFT JOIN product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                                                            LEFT JOIN frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                                                            LEFT JOIN frame_shapes AS fs ON ci.ci_frame_shape_id = fs.fshape_shape_id
                                                            LEFT JOIN product_colors AS c ON ci.ci_color_id = c.pcol_color_id
                                                            LEFT JOIN units AS u ON ci.ci_unit_id = u.unit_unit_id
                                                            LEFT JOIN brands AS b ON ci.ci_brand_id = b.brand_brand_id
                                                            LEFT JOIN store_inventory AS si ON ci.ci_product_id = si.si_product_id AND si.si_store_type = 1
                                                            LEFT JOIN own_store AS os ON os.os_store_id = store_products.si_store_id 
                                                            AND si.si_store_type = 1
                                                            WHERE store_products.si_store_type = 1 AND 
                                                            store_products.si_product_quantity != 0
                                                            GROUP BY store_products.si_store_inventory_id ORDER BY store_products.si_store_inventory_id DESC"""

            cursor.execute(get_stores_product_query)
            store_product_list = cursor.fetchall()
            if product_list == ():
                print("product is NONE")
                product_list = []
            if store_product_list == ():
                print("store product is none")
                store_product_list = []
            return {
                "status": True,
                "product_list": (product_list + store_product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def create_store_stock_request(stock_obj):
    try:
        with getConnection().cursor() as cursor:
            stock_req_query = """INSERT INTO request_products ( 
                                   pr_store_id, 
                                   pr_store_type, 
                                   pr_product_id, 
                                   pr_product_quantity, 
                                   pr_request_status, 
                                   pr_delivery_status, 
                                   pr_is_requested,
                                   pr_request_to_store_id,
                                   pr_payment_status,
                                   pr_created_on, 
                                   pr_created_by, 
                                   pr_last_updated_on, 
                                   pr_last_updated_by,
                                   pr_unit_cost
                               ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            cursor.execute(stock_req_query, (stock_obj.request_from_store_id, 2, stock_obj.product_id,
                                             stock_obj.product_quantity, 0, 0, 1,
                                             stock_obj.request_to_store_id, 0, getIndianTime(), stock_obj.created_by,
                                             getIndianTime(), stock_obj.created_by, stock_obj.unit_cost))
            return {
                "status": True,
                "message": "success"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def view_all_store_stock_request(store_id, status):
    try:
        with getConnection().cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT rp.*, ci.*, creator.admin_name AS creator, 
                                                    updater.admin_name AS updater, pc.pc_category_name, 
                                                    pm.pm_material_name, ft.ftype_name, fs.fshape_name,c.pcol_color_name, u.unit_name, b.brand_name,
                                                    CASE
                                                        WHEN rp.pr_store_type = 1 THEN os.os_store_name
                                                        ELSE fstore.fs_store_name
                                                    END AS store_name,
                                                    from_store.os_store_name AS sender_store, si.si_product_quantity AS sender_store_quantity
                                                    FROM request_products As rp
                                                    LEFT JOIN central_inventory AS ci ON ci.ci_product_id = rp.pr_product_id
                                                    LEFT JOIN admin AS creator ON rp.pr_created_by = creator.admin_admin_id
                                                    LEFT JOIN admin AS updater ON rp.pr_last_updated_by = updater.admin_admin_id
                                                    LEFT JOIN product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                                                    LEFT JOIN product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                                                    LEFT JOIN frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                                                    LEFT JOIN frame_shapes AS fs ON ci.ci_frame_shape_id = fs.fshape_shape_id
                                                    LEFT JOIN product_colors AS c ON ci.ci_color_id = c.pcol_color_id
                                                    LEFT JOIN units AS u ON ci.ci_unit_id = u.unit_unit_id
                                                    LEFT JOIN brands AS b ON ci.ci_brand_id = b.brand_brand_id 
                                                    LEFT JOIN own_store os ON rp.pr_store_id = os.os_store_id AND rp.pr_store_type = 1
                                                    LEFT JOIN own_store AS from_store ON rp.pr_request_to_store_id = from_store.os_store_id
                                                    LEFT JOIN franchise_store fstore ON rp.pr_store_id = fstore.fs_store_id AND rp.pr_store_type = 2
                                                    LEFT JOIN store_inventory si ON si.si_product_id = rp.pr_product_id AND si.si_store_id = rp.pr_request_to_store_id AND si.si_store_type = 1
                                                    WHERE rp.pr_store_id = {store_id} AND rp.pr_store_type = 2  AND rp.pr_request_status LIKE '{status}' 
                                                    ORDER BY rp.pr_request_products_id DESC"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "stocks_request_list": product_list
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def request_delivery_status_change(request_id, status, updated_by):
    try:
        with getConnection().cursor() as cursor:
            update_stock_request_query = f"""UPDATE request_products SET pr_delivery_status = {status}
                                                WHERE pr_request_products_id = '{request_id}' """
            cursor.execute(update_stock_request_query)
            if status == 2:
                fetch_req_product_query = f"""SELECT * FROM request_products 
                                        WHERE pr_request_products_id = '{request_id}'"""
                cursor.execute(fetch_req_product_query)
                product_details = cursor.fetchone()
                quantity = product_details['pr_product_quantity']

                update_store_Inventory = f"""INSERT INTO store_inventory 
                                               (si_store_id, si_store_type, si_product_id, si_product_quantity,  
                                               si_created_on, si_created_by, si_last_updated_on, si_last_updated_by) 
                                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                               ON DUPLICATE KEY UPDATE
                                               si_product_quantity = si_product_quantity + {quantity}, 
                                               si_last_updated_on = '{getIndianTime()}', 
                                               si_last_updated_by = {updated_by}"""

                cursor.execute(update_store_Inventory,
                               (product_details['pr_store_id'], product_details['pr_store_type'],
                                product_details['pr_product_id'], product_details['pr_product_quantity'],
                                getIndianTime(), updated_by, getIndianTime(), updated_by))
            return {
                "status": True,
                "message": "updated delivery status"
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
