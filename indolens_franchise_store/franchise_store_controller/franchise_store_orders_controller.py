import datetime
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.sales_detail_resp_model import get_order_detail
from indolens_admin.admin_models.admin_resp_model.sales_resp_model import get_sales_orders
from indolens_own_store.own_store_model.response_model.store_resp_model import get_store

def getIndianTime():
    ist = pytz.timezone('Asia/Kolkata')
    today = datetime.datetime.now(ist)
    return today

def get_all_orders(status, pay_status, store_id):
    status_conditions = {
        "All": "LIKE '%'",
        "New": "= 1",
        "Processing": "= 2",
        "Ready": "= 3",
        "Dispatched": "= 4",
        "Delivered Store": "= 5",
        "Delivered Customer": "= 6",
        "Cancelled": "= 7",
    }
    status_condition = status_conditions[status]
    payment_status_values = {
        "All": "LIKE '%'",
        "Pending": "= 1",
        "Completed": "= 2",
        "Refunded": "= 3",
    }
    payment_status_value = payment_status_values[pay_status]
    try:
        with connection.cursor() as cursor:
            get_order_query = f"""
                SELECT 
                    so.*, 
                    c.name, 
                    SUM(product_total_cost) AS total_cost, 
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN os.store_name 
                        ELSE fs.store_name 
                    END AS store_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN creator_os.name 
                        ELSE creator_fs.name 
                    END AS creator_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN updater_os.name 
                        ELSE updater_fs.name 
                    END AS updater_name
                FROM sales_order AS so
                LEFT JOIN customers AS c ON c.customer_id = so.customer_id
                LEFT JOIN own_store os ON so.created_by_store = os.store_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store fs ON so.created_by_store = fs.store_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees creator_os ON so.created_by = creator_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees creator_fs ON so.created_by = creator_fs.employee_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees updater_os ON so.updated_by = updater_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees updater_fs ON so.updated_by = updater_fs.employee_id AND so.created_by_store_type = 2
                WHERE so.order_status {status_condition} AND so.payment_status {payment_status_value} AND so.created_by_store_type = 2
                AND so.created_by_store = {store_id}
                GROUP BY so.order_id ORDER BY so.sale_item_id DESC     
                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                       "status": True,
                       "orders_list": get_sales_orders(orders_list),
                       "dash_orders_list": get_sales_orders(orders_list)[:15]
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_all_store_orders(store_id, store_type):
    try:
        with connection.cursor() as cursor:
            get_order_query = f"""
                SELECT 
                    so.*, 
                    c.name, 
                    SUM(product_total_cost) AS total_cost, 
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN os.store_name 
                        ELSE fs.store_name 
                    END AS store_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN creator_os.name 
                        ELSE creator_fs.name 
                    END AS creator_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN updater_os.name 
                        ELSE updater_fs.name 
                    END AS updater_name
                FROM sales_order AS so
                LEFT JOIN customers AS c ON c.customer_id = so.customer_id
                LEFT JOIN own_store os ON so.created_by_store = os.store_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store fs ON so.created_by_store = fs.store_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees creator_os ON so.created_by = creator_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees creator_fs ON so.created_by = creator_fs.employee_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees updater_os ON so.updated_by = updater_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees updater_fs ON so.updated_by = updater_fs.employee_id AND so.created_by_store_type = 2
                WHERE so.created_by_store = {store_id} AND so.created_by_store_type = {store_type}
                GROUP BY so.order_id          
                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                       "status": True,
                       "orders_list": get_sales_orders(orders_list)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_order_details(orderId):
    try:
        with connection.cursor() as cursor:
            get_order_details_query = f"""
                SELECT 
                    so.*,
                    (SELECT SUM(unit_sale_price*purchase_quantity) AS total_cost FROM sales_order WHERE order_id = '{orderId}' 
                    GROUP BY order_id ), 
                    (SELECT SUM(product_total_cost) AS discount_cost FROM sales_order WHERE order_id = '{orderId}' 
                    GROUP BY order_id ), 
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN os.store_name 
                        ELSE fs.store_name 
                    END AS store_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN creator_os.name 
                        ELSE creator_fs.name 
                    END AS creator_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN updater_os.name 
                        ELSE updater_fs.name 
                    END AS updater_name,
                    c.*, ci.*, pc.category_name, pm.material_name,
                    ft.frame_type_name, fsh.shape_name,co.color_name, u.unit_name, b.brand_name
                FROM sales_order AS so
                LEFT JOIN customers AS c ON c.customer_id = so.customer_id
                LEFT JOIN central_inventory AS ci ON ci.product_id = so.product_id
                LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                LEFT JOIN frame_shapes AS fsh ON ci.frame_shape_id = fsh.shape_id
                LEFT JOIN product_colors AS co ON ci.color_id = co.color_id
                LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                LEFT JOIN brands AS b ON ci.brand_id = b.brand_id
                LEFT JOIN own_store os ON so.created_by_store = os.store_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store fs ON so.created_by_store = fs.store_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees creator_os ON so.created_by = creator_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees creator_fs ON so.created_by = creator_fs.employee_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees updater_os ON so.updated_by = updater_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees updater_fs ON so.updated_by = updater_fs.employee_id AND so.created_by_store_type = 2
                WHERE so.order_id = '{orderId}' GROUP BY so.sale_item_id  
                """
            cursor.execute(get_order_details_query)
            orders_details = cursor.fetchall()

            return {
                "status": True,
                "orders_details": get_order_detail(orders_details)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_all_customer_orders(customerId):
    try:
        with connection.cursor() as cursor:
            get_order_query = f"""
                SELECT 
                    so.*, 
                    c.name, 
                    SUM(product_total_cost) AS total_cost, 
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN os.store_name 
                        ELSE fs.store_name 
                    END AS store_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN creator_os.name 
                        ELSE creator_fs.name 
                    END AS creator_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN updater_os.name 
                        ELSE updater_fs.name 
                    END AS updater_name
                FROM sales_order AS so
                LEFT JOIN customers AS c ON c.customer_id = so.customer_id
                LEFT JOIN own_store os ON so.created_by_store = os.store_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store fs ON so.created_by_store = fs.store_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees creator_os ON so.created_by = creator_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees creator_fs ON so.created_by = creator_fs.employee_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees updater_os ON so.updated_by = updater_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees updater_fs ON so.updated_by = updater_fs.employee_id AND so.created_by_store_type = 2
                WHERE so.customer_id = {customerId}
                GROUP BY so.order_id  ORDER BY so.customer_id DESC       
                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                       "status": True,
                       "orders_list": get_sales_orders(orders_list)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def franchise_order_status_change(orderID, orderStatus):
    try:
        with connection.cursor() as cursor:
            get_order_status_change_query = f"""
                UPDATE sales_order SET order_status = {orderStatus}
                WHERE order_id = '{orderID}'
                """
            cursor.execute(get_order_status_change_query)

            add_order_track_query = f""" 
                                        INSERT INTO order_track (order_id, status, created_on) 
                                        VALUES ('{orderID}', {orderStatus}, '{getIndianTime()}' ) """
            cursor.execute(add_order_track_query)

            return {
                       "status": True,
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def franchise_payment_status_change(orderID, paymentStatus):
    try:
        with connection.cursor() as cursor:
            get_payment_status_change = f"""
                UPDATE sales_order SET payment_status = {paymentStatus}
                WHERE order_id = '{orderID}'
                """
            cursor.execute(get_payment_status_change)

            if paymentStatus == "3":
                get_order_status_change_query = f"""
                                UPDATE sales_order SET order_status = 6
                                WHERE order_id = '{orderID}'
                                """
                cursor.execute(get_order_status_change_query)

            return {
                       "status": True,
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_store_details(storeId, storeType):
    try:
        with connection.cursor() as cursor:

            if storeType == 1:
                get_own_stores_query = f""" SELECT own_store.*
                                                    FROM own_store
                                                    WHERE own_store.store_id = '{storeId}' """
                cursor.execute(get_own_stores_query)
                stores_data = cursor.fetchall()

            else:
                get_franchise_stores_query = f""" SELECT franchise_store.* FROM franchise_store
                                                    WHERE franchise_store.store_id = '{storeId}' """
                cursor.execute(get_franchise_stores_query)
                stores_data = cursor.fetchall()

            return {
                "status": True,
                "store_data": get_store(stores_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301