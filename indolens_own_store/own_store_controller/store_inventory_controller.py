import datetime
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.master_category_resp_model import get_product_categories
from indolens_own_store.own_store_model.response_model.product_request_list_resp_model import get_request_product_list
from indolens_own_store.own_store_model.response_model.stock_request_product_resp_model import \
    get_products_for_stock_request
from indolens_own_store.own_store_model.response_model.store_inventory_product_resp_model import \
    get_store_inventory_stocks


ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

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
                                    WHERE si.product_quantity <= {quantity} AND si.store_id = '{store_id}' AND si.store_type = 1 
                                    ORDER BY si.store_inventory_id DESC"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()

            get_product_category_query = f""" SELECT pc.* , creator.name, updater.name
                                    FROM product_categories AS pc 
                                    LEFT JOIN admin AS creator ON pc.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON pc.last_updated_by = updater.admin_id 
                                    ORDER BY pc.category_id DESC"""
            cursor.execute(get_product_category_query)
            stores_data = cursor.fetchall()
            return {
                "status": True,
                "stocks_list": get_store_inventory_stocks(product_list),
                "product_category": get_product_categories(stores_data)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e), "stocks_list": []}, 301
    except Exception as e:
        return {"status": False, "message": str(e), "stocks_list": []}, 301


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
                                    WHERE si.store_id = {store_id}  AND si.store_type = 1 AND ci.category_id != 2 
                                    AND ci.category_id != 3
                                    ORDER BY si.store_inventory_id DESC"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()

            get_product_category_query = f""" SELECT pc.* , creator.name, updater.name
                        FROM product_categories AS pc 
                        LEFT JOIN admin AS creator ON pc.created_by = creator.admin_id
                        LEFT JOIN admin AS updater ON pc.last_updated_by = updater.admin_id 
                        ORDER BY pc.category_id DESC"""
            cursor.execute(get_product_category_query)
            stores_data = cursor.fetchall()
            return {
                "status": True,
                "stocks_list": get_store_inventory_stocks(product_list),
                "product_category": get_product_categories(stores_data)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
def get_all_available_products_for_store(store_id):
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
                                    WHERE si.store_id = {store_id}  AND si.store_type = 1 AND ci.category_id != 2 
                                    AND ci.category_id != 3 AND si.product_quantity != 0
                                    ORDER BY si.store_inventory_id DESC"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()

            get_product_category_query = f""" SELECT pc.* , creator.name, updater.name
                        FROM product_categories AS pc 
                        LEFT JOIN admin AS creator ON pc.created_by = creator.admin_id
                        LEFT JOIN admin AS updater ON pc.last_updated_by = updater.admin_id 
                        ORDER BY pc.category_id DESC"""
            cursor.execute(get_product_category_query)
            stores_data = cursor.fetchall()
            return {
                "status": True,
                "stocks_list": get_store_inventory_stocks(product_list),
                "product_category": get_product_categories(stores_data)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def getstore_product_by_id(assigned_store, productId):
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
                                    LEFT JOIN own_store AS os ON os.store_id = '{assigned_store}' 
                                    WHERE si.store_id = {assigned_store} AND si.store_inventory_id = {productId}
                                    ORDER BY si.store_inventory_id DESC"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()

            return {
                "status": True,
                "stocks_list": get_store_inventory_stocks(product_list),
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_central_inventory_products(store_id):
    try:
        with connection.cursor() as cursor:
            get_all_product_query = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name, 
                                    (SELECT product_quantity 
                                                     FROM store_inventory 
                                                     WHERE store_id = {store_id} AND store_type = 1 AND product_id = ci.product_id
                                                    ) AS store_quantity, 
                                    0 as store_id, 0 as store_name
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
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id 
                                    WHERE ci.category_id <> 3 AND ci.category_id <> 2 AND ci.status = 1 AND ci.
                                    product_quantity != 0
                                    GROUP BY ci.product_id ORDER BY ci.product_id DESC
                                     """

            cursor.execute(get_all_product_query)
            product_list = cursor.fetchall()

            get_stores_product_query = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                                ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name, 
                                                (SELECT product_quantity 
                                                     FROM store_inventory 
                                                     WHERE store_id = {store_id} AND store_type = 1 AND product_id = store_products.product_id
                                                    ) AS store_quantity,  
                                                store_products.store_id, os.store_name
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
                                                LEFT JOIN store_inventory AS si ON ci.product_id = si.product_id AND si.store_type = 1
                                                LEFT JOIN own_store AS os ON os.store_id = store_products.store_id 
                                                AND si.store_type = 1
                                                LEFT JOIN brands AS b ON ci.brand_id = b.brand_id 
                                                WHERE store_products.store_type = 1 AND 
                                                store_products.product_quantity != 0 AND store_products.store_id != {store_id}
                                                GROUP BY store_products.store_inventory_id ORDER BY store_products.store_inventory_id DESC"""

            cursor.execute(get_stores_product_query)
            store_product_list = cursor.fetchall()
            print(get_products_for_stock_request(store_product_list))
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
                               last_updated_by,
                               unit_cost
                           ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            cursor.execute(stock_req_query, (
                stock_obj.request_from_store_id, stock_obj.store_type, stock_obj.product_id, stock_obj.product_quantity,
                0, 0, 1, stock_obj.request_to_store_id, 0, getIndianTime(), stock_obj.created_by, getIndianTime(),
                stock_obj.created_by,
                stock_obj.unit_cost))
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
            get_all_stock_request_query = f""" SELECT rp.*, ci.*, creator.name, updater.name, pc.category_name, 
                                    pm.material_name, ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, 
                                    b.brand_name, 
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
                                    LEFT JOIN own_store AS from_store ON rp.request_to_store_id = from_store.store_id
                                    LEFT JOIN own_store os ON rp.store_id = os.store_id AND rp.store_type = 1
                                    LEFT JOIN franchise_store fstore ON rp.store_id = fstore.store_id AND rp.store_type = 2
                                    WHERE ( ( rp.store_id = {store_id} AND rp.store_type = 1 ) OR rp.request_to_store_id = {store_id}) AND rp.request_status LIKE '{status}' 
                                    ORDER BY rp.request_products_id DESC"""

            cursor.execute(get_all_stock_request_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "stocks_request_list": get_request_product_list(product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def request_delivery_status_change(request_id, status, updated_by):
    try:
        with connection.cursor() as cursor:
            update_stock_request_query = f"""UPDATE request_products SET delivery_status = {status}
                                                WHERE request_products_id = '{request_id}' """
            cursor.execute(update_stock_request_query)
            if status == 2:
                fetch_req_product_query = f"""SELECT * FROM request_products 
                                        WHERE request_products_id = '{request_id}'"""
                cursor.execute(fetch_req_product_query)
                product_details = cursor.fetchone()
                quantity = product_details[4]

                update_store_Inventory = f"""INSERT INTO store_inventory 
                                               (store_id, store_type, product_id, product_quantity, created_on, 
                                               created_by, last_updated_on, last_updated_by) 
                                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                               ON DUPLICATE KEY UPDATE
                                               product_quantity = product_quantity + {quantity}, 
                                               last_updated_on = '{getIndianTime()}', 
                                               last_updated_by = {updated_by}"""

                cursor.execute(update_store_Inventory,
                               (product_details[1], product_details[2], product_details[3],
                                product_details[4], getIndianTime(), updated_by, getIndianTime(), updated_by))

            return {
                "status": True,
                "message": "updated delivery status"
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
