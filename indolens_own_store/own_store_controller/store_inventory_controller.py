import datetime
import pymysql
import pytz
from django.db import connection

from indolens_own_store.own_store_model.response_model.central_inventory_product_resp_model import get_products
from indolens_own_store.own_store_model.response_model.product_request_list_resp_model import get_request_product_list
from indolens_own_store.own_store_model.response_model.stock_request_product_resp_model import \
    get_products_for_stock_request
from indolens_own_store.own_store_model.response_model.store_inventory_product_resp_model import \
    get_store_inventory_stocks

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_all_out_of_stock_products_for_store(quantity, store_id):
    try:
        with connection.cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT si.*, ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name,
                                    os.store_name
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
                                    LEFT JOIN own_store AS os ON os.store_id = '{store_id}'
                                    WHERE si.product_quantity <= {quantity} AND si.store_id = '{store_id}' AND si.store_type = 1 """

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "stocks_list": get_store_inventory_stocks(product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_products_for_store(store_id):
    try:
        with connection.cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT si.*, ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name,
                                    os.store_name
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
                                    LEFT JOIN own_store AS os ON os.store_id = '{store_id}' 
                                    WHERE si.store_id = {store_id}  AND si.store_type = 1 """

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "stocks_list": get_store_inventory_stocks(product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_central_inventory_products():
    try:
        with connection.cursor() as cursor:
            get_all_product_query = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name, 
                                    si.product_quantity, 0 as store_id
                                    FROM central_inventory As ci
                                    LEFT JOIN admin AS creator ON ci.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON ci.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN store_inventory AS si ON ci.product_id = si.product_id AND si.store_type = 1
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id GROUP BY ci.product_id """

            cursor.execute(get_all_product_query)
            product_list = cursor.fetchall()

            get_stores_product_query = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                                ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name, 
                                                si.product_quantity, store_products.store_id
                                                FROM store_inventory AS store_products 
                                                LEFT JOIN central_inventory As ci ON store_products.product_id = ci.product_id
                                                LEFT JOIN admin AS creator ON ci.created_by = creator.admin_id
                                                LEFT JOIN admin AS updater ON ci.last_updated_by = updater.admin_id
                                                LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                                LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                                LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                                LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                                LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                                LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                                LEFT JOIN store_inventory AS si ON ci.product_id = si.product_id 
                                                AND si.store_type = 1
                                                LEFT JOIN brands AS b ON ci.brand_id = b.brand_id 
                                                WHERE store_products.store_type = 1 AND 
                                                store_products.product_quantity != 0 
                                                GROUP BY store_products.product_id"""

            cursor.execute(get_stores_product_query)
            store_product_list = cursor.fetchall()
            return {
                "status": True,
                "product_list": get_products_for_stock_request(product_list + store_product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def create_store_stock_request(stock_obj):
    try:
        with connection.cursor() as cursor:
            stock_req_query = """INSERT INTO request_products ( 
                               store_id, 
                               store_type, 
                               product_id, 
                               product_quantity, 
                               request_status, 
                               delivery_status, 
                               is_requested,
                               request_to_store_id,
                               payment_status,
                               created_on, 
                               created_by, 
                               last_updated_on, 
                               last_updated_by
                           ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            cursor.execute(stock_req_query, (
                stock_obj.request_from_store_id, stock_obj.store_type, stock_obj.product_id, stock_obj.product_quantity,
                0, 0, 1, stock_obj.request_to_store_id, 0, today, stock_obj.created_by, today, stock_obj.created_by))
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
        with connection.cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT rp.*, ci.*, creator.name, updater.name, pc.category_name, 
                                    pm.material_name, ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, 
                                    b.brand_name, os.store_name
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
                                    LEFT JOIN own_store os ON os.store_id = {store_id}
                                    WHERE rp.store_id = {store_id} AND rp.request_status LIKE '{status}' 
                                    AND rp.store_type = 1 """

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            print(product_list)
            return {
                "status": True,
                "stocks_request_list": get_request_product_list(product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
