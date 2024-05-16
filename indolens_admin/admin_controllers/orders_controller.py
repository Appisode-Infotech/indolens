import datetime
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_models.admin_resp_model.completed_order_resp_model import get_completed_sales_orders
from indolens_admin.admin_models.admin_resp_model.invoice_detail_resp_model import get_order_invoice_detail
from indolens_admin.admin_models.admin_resp_model.sales_detail_resp_model import get_order_detail
from indolens_admin.admin_models.admin_resp_model.sales_resp_model import get_sales_orders
from indolens_own_store.own_store_model.response_model.invoice_data_resp_model import get_invoice_detail
from indolens_own_store.own_store_model.response_model.order_track import order_track
from indolens_own_store.own_store_model.response_model.sales_order_payment_track_resp_model import \
    sales_order_payment_track_response
from indolens_own_store.own_store_model.response_model.store_resp_model import get_store

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def get_all_orders(status, pay_status, store):
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
    store_values = {
        "All": "LIKE '%'",
        "Own Stores": "= 1",
        "Franchise Stores": "= 2",
    }
    store_condition = store_values[store]
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                SELECT 
                    so.*, 
                    c.customer_name, 
                    SUM(so_product_total_cost) AS total_cost, 
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN os.os_store_name 
                        ELSE fs.fs_store_name 
                    END AS store_name,
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN creator_os.ose_name 
                        ELSE creator_fs.fse_name 
                    END AS creator_name,
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN updater_os.ose_name 
                        ELSE updater_fs.fse_name 
                    END AS updater_name
                FROM sales_order AS so
                LEFT JOIN customers AS c ON c.customer_customer_id = so.so_customer_id
                LEFT JOIN own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                LEFT JOIN franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                LEFT JOIN own_store_employees creator_os ON so.so_created_by = creator_os.ose_employee_id AND so.so_created_by_store_type = 1
                LEFT JOIN franchise_store_employees creator_fs ON so.so_created_by = creator_fs.fse_employee_id AND so.so_created_by_store_type = 2
                LEFT JOIN own_store_employees updater_os ON so.so_updated_by = updater_os.ose_employee_id AND so.so_created_by_store_type = 1
                LEFT JOIN franchise_store_employees updater_fs ON so.so_updated_by = updater_fs.fse_employee_id AND so.so_created_by_store_type = 2
                WHERE so.so_order_status {status_condition} AND so.so_payment_status {payment_status_value} AND so.so_created_by_store_type {store_condition}
                GROUP BY so.so_order_id ORDER BY so.so_sale_item_id DESC         
                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                "status": True,
                "orders_list": orders_list,
                "latest_orders": orders_list[:15]
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_completed_orders(status, pay_status, store):
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
    store_values = {
        "All": "LIKE '%'",
        "Own Stores": "= 1",
        "Franchise Stores": "= 2",
    }
    store_condition = store_values[store]
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                SELECT 
                    so.*, 
                    c.customer_name, 
                    SUM(so_product_total_cost) AS total_cost, 
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN os.os_store_name 
                        ELSE fs.fs_store_name 
                    END AS store_name,
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN creator_os.ose_name 
                        ELSE creator_fs.fse_name 
                    END AS creator_name,
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN updater_os.ose_name 
                        ELSE updater_fs.fse_name 
                    END AS updater_name,
                    i.invoice_invoice_number
                FROM sales_order AS so
                LEFT JOIN customers AS c ON c.customer_customer_id = so.so_customer_id
                LEFT JOIN invoice AS i ON i.invoice_order_id = so.so_order_id
                LEFT JOIN own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                LEFT JOIN franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                LEFT JOIN own_store_employees creator_os ON so.so_created_by = creator_os.ose_employee_id AND so.so_created_by_store_type = 1
                LEFT JOIN franchise_store_employees creator_fs ON so.so_created_by = creator_fs.fse_employee_id AND so.so_created_by_store_type = 2
                LEFT JOIN own_store_employees updater_os ON so.so_updated_by = updater_os.ose_employee_id AND so.so_created_by_store_type = 1
                LEFT JOIN franchise_store_employees updater_fs ON so.so_updated_by = updater_fs.fse_employee_id AND so.so_created_by_store_type = 2
                WHERE so.so_order_status {status_condition} AND so.so_payment_status {payment_status_value} AND so.so_created_by_store_type {store_condition}
                GROUP BY so.so_order_id ORDER BY so.so_sale_item_id DESC         
                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                "status": True,
                "orders_list": orders_list
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_store_orders(store_id, store_type):
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                            SELECT 
                                so.*, 
                                c.customer_name, 
                                SUM(so_product_total_cost) AS total_cost, 
                                CASE 
                                    WHEN so.so_created_by_store_type = 1 THEN os.os_store_name 
                                    ELSE fs.fs_store_name 
                                END AS store_name,
                                CASE 
                                    WHEN so.so_created_by_store_type = 1 THEN creator_os.ose_name 
                                    ELSE creator_fs.fse_name 
                                END AS creator_name,
                                CASE 
                                    WHEN so.so_created_by_store_type = 1 THEN updater_os.ose_name 
                                    ELSE updater_fs.fse_name 
                                END AS updater_name
                            FROM sales_order AS so
                            LEFT JOIN customers AS c ON c.customer_customer_id = so.so_customer_id
                            LEFT JOIN own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                            LEFT JOIN franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                            LEFT JOIN own_store_employees creator_os ON so.so_created_by = creator_os.ose_employee_id AND so.so_created_by_store_type = 1
                            LEFT JOIN franchise_store_employees creator_fs ON so.so_created_by = creator_fs.fse_employee_id AND so.so_created_by_store_type = 2
                            LEFT JOIN own_store_employees updater_os ON so.so_updated_by = updater_os.ose_employee_id AND so.so_created_by_store_type = 1
                            LEFT JOIN franchise_store_employees updater_fs ON so.so_updated_by = updater_fs.fse_employee_id AND so.so_created_by_store_type = 2
                            WHERE so.so_created_by_store = {store_id} AND so.so_created_by_store_type = {store_type}
                            GROUP BY so.so_order_id ORDER BY so.so_sale_item_id DESC         
                            """
            cursor.execute(get_order_query)

            orders_list = cursor.fetchall()

            return {
                "status": True,
                "orders_list": orders_list
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_store_sales(store_id, store_type):
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                                SELECT IFNULL(SUM(so_product_total_cost), 0) AS total_sale
                                FROM sales_order
                                WHERE so_created_by_store_type = {store_type} AND so_created_by_store = {store_id}
                                AND so_order_status != 7
                                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchone()
            total_sale = orders_list['total_sale'] if orders_list['total_sale'] is not None else 0

            return {
                "status": True,
                "sale": total_sale
            }, 200


    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_customer_orders(customerId):
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                                SELECT 
                                    so.*, 
                                    c.customer_name, 
                                    SUM(so_product_total_cost) AS total_cost, 
                                    CASE 
                                        WHEN so.so_created_by_store_type = 1 THEN os.os_store_name 
                                        ELSE fs.fs_store_name 
                                    END AS store_name,
                                    CASE 
                                        WHEN so.so_created_by_store_type = 1 THEN creator_os.ose_name 
                                        ELSE creator_fs.fse_name 
                                    END AS creator_name,
                                    CASE 
                                        WHEN so.so_created_by_store_type = 1 THEN updater_os.ose_name 
                                        ELSE updater_fs.fse_name 
                                    END AS updater_name
                                FROM sales_order AS so
                                LEFT JOIN customers AS c ON c.customer_customer_id = so.so_customer_id
                                LEFT JOIN own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                                LEFT JOIN franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                                LEFT JOIN own_store_employees creator_os ON so.so_created_by = creator_os.ose_employee_id AND so.so_created_by_store_type = 1
                                LEFT JOIN franchise_store_employees creator_fs ON so.so_created_by = creator_fs.fse_employee_id AND so.so_created_by_store_type = 2
                                LEFT JOIN own_store_employees updater_os ON so.so_updated_by = updater_os.ose_employee_id AND so.so_created_by_store_type = 1
                                LEFT JOIN franchise_store_employees updater_fs ON so.so_updated_by = updater_fs.fse_employee_id AND so.so_created_by_store_type = 2
                                WHERE so.so_customer_id = {customerId}
                                GROUP BY so.so_order_id ORDER BY so.so_sale_item_id DESC         
                                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                "status": True,
                "orders_list": orders_list
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_order_details(orderId):
    try:
        with getConnection().cursor() as cursor:
            get_order_details_query = f"""
                SELECT 
                    so.*,
                    (SELECT SUM(so_unit_sale_price * so_purchase_quantity)  FROM sales_order 
                    WHERE so_order_id = '{orderId}' GROUP BY so_order_id) AS total_cost ,
                    (SELECT SUM(so_product_total_cost)  FROM sales_order 
                    WHERE so_order_id = '{orderId}' GROUP BY so_order_id) AS discount_cost,
                    (SELECT SUM(so_product_total_cost) - so_amount_paid FROM sales_order 
                    WHERE so_order_id = '{orderId}' GROUP BY so_order_id) AS balance_amount,
                    (SELECT SUM(so_unit_sale_price * so_purchase_quantity) - SUM(so_product_total_cost) FROM sales_order 
                    WHERE so_order_id = '{orderId}' GROUP BY so_order_id) AS discounted_amount,
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN os.os_store_name 
                        ELSE fs.fs_store_name 
                    END AS store_name,
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN creator_os.ose_name 
                        ELSE creator_fs.fse_name 
                    END AS creator_name,
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN updater_os.ose_name 
                        ELSE updater_fs.fse_name 
                    END AS updater_name,
                    c.*, ci.*, pc.pc_category_name, pm.pm_material_name,
                    ft.ftype_name, fsh.fshape_name,co.pcol_color_name, u.unit_name, b.brand_name,
                    ROUND((ci.ci_product_gst / 2), 2) AS product_gst_half, l.lab_name,
                    ROUND(((100 * so.so_unit_sale_price / (100 + ci.ci_product_gst)) - (so.so_discount_percentage / 100) * (100 * so.so_unit_sale_price / (100 + ci.ci_product_gst))), 2) AS discounted_total_cost
                FROM 
                    sales_order AS so
                LEFT JOIN 
                    customers AS c ON c.customer_customer_id = so.so_customer_id
                LEFT JOIN 
                    lab AS l ON so.so_assigned_lab = l.lab_lab_id
                LEFT JOIN 
                    central_inventory AS ci ON ci.ci_product_id = so.so_product_id
                LEFT JOIN 
                    product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                LEFT JOIN 
                    product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                LEFT JOIN 
                    frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                LEFT JOIN 
                    frame_shapes AS fsh ON ci.ci_frame_shape_id = fsh.fshape_shape_id
                LEFT JOIN 
                    product_colors AS co ON ci.ci_color_id = co.pcol_color_id
                LEFT JOIN 
                    units AS u ON ci.ci_unit_id = u.unit_unit_id
                LEFT JOIN 
                    brands AS b ON ci.ci_brand_id = b.brand_brand_id
                LEFT JOIN 
                    own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                LEFT JOIN 
                    franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                LEFT JOIN 
                    own_store_employees creator_os ON so.so_created_by = creator_os.ose_employee_id AND so.so_created_by_store_type = 1
                LEFT JOIN 
                    franchise_store_employees creator_fs ON so.so_created_by = creator_fs.fse_employee_id AND so.so_created_by_store_type = 2
                LEFT JOIN 
                    own_store_employees updater_os ON so.so_updated_by = updater_os.ose_employee_id AND so.so_created_by_store_type = 1
                LEFT JOIN 
                    franchise_store_employees updater_fs ON so.so_updated_by = updater_fs.fse_employee_id AND so.so_created_by_store_type = 2
                WHERE 
                    so.so_order_id = '{orderId}'
            """
            cursor.execute(get_order_details_query)

            orders_details = cursor.fetchall()

            return {
                "status": True,
                "orders_details": orders_details,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_payment_logs(orderId):
    try:
        with getConnection().cursor() as cursor:
            get_payment_logs_query = f"""
                SELECT so.*, 
                    CASE 
                        WHEN so.sopt_created_by_store_type = 1 THEN creator_os.ose_name 
                        ELSE creator_fs.fse_name 
                    END AS creator_name
                FROM sales_order_payment_track AS so
                LEFT JOIN own_store_employees creator_os ON so.sopt_created_by_id = creator_os.ose_employee_id AND so.sopt_created_by_store_type = 1
                LEFT JOIN franchise_store_employees creator_fs ON so.sopt_created_by_id = creator_fs.fse_employee_id AND so.sopt_created_by_store_type = 2
                WHERE so.sopt_order_id = '{orderId}' GROUP BY so.sopt_id  
                """
            cursor.execute(get_payment_logs_query)
            payment_logs = cursor.fetchall()

            return {
                "status": True,
                "payment_logs": payment_logs
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_invoice_details(orderId):
    try:
        with getConnection().cursor() as cursor:
            get_order_details_query = f""" SELECT * FROM invoice WHERE invoice_order_id = '{orderId}'"""
            cursor.execute(get_order_details_query)
            orders_details = cursor.fetchone()
            return {
                "status": True,
                "invoice_details": orders_details
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_order_creator_role(employeeID, storeType):
    status_conditions = {
        1: "own_store_employees",
        2: "franchise_store_employees",
    }
    status_condition = status_conditions[storeType]
    role_conditions = {
        1: "ose_role",
        2: "fse_role",
    }
    role_condition = role_conditions[storeType]
    employee_conditions = {
        1: "ose_employee_id",
        2: "fse_employee_id",
    }
    employee_condition = employee_conditions[storeType]
    try:
        with getConnection().cursor() as cursor:
            get_order_creator_query = f"""
                    SELECT {role_condition} FROM {status_condition} WHERE {employee_condition} = {employeeID}
                    """
            cursor.execute(get_order_creator_query)
            role = cursor.fetchone()

            return {
                "status": True,
                "role": role[role_condition] if role else None
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_store_details(storeId, storeType):
    try:
        with getConnection().cursor() as cursor:

            if storeType == 1:
                get_own_stores_query = f""" SELECT own_store.*
                                                    FROM own_store
                                                    WHERE own_store.os_store_id = '{storeId}' """
                cursor.execute(get_own_stores_query)
                stores_data = cursor.fetchone()

            else:
                get_franchise_stores_query = f""" SELECT franchise_store.* FROM franchise_store
                                                    WHERE franchise_store.fs_store_id = '{storeId}' """
                cursor.execute(get_franchise_stores_query)
                stores_data = cursor.fetchone()

            return {
                "status": True,
                "store_data": stores_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_order_track(orderId):
    try:
        with getConnection().cursor() as cursor:
            get_order_track_query = f""" SELECT track_id, order_id, status, 
                                        DATE_FORMAT(created_on, '%d/%m/%Y %h:%i %p') AS created_on
                                        FROM order_track
                                        WHERE order_id = '{orderId}' """
            cursor.execute(get_order_track_query)
            order_trak = cursor.fetchall()
            print(order_trak)

            get_order_store_details_query = f"""
                SELECT 
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN os.os_store_name 
                        ELSE fs.fs_store_name 
                    END AS store_name,
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN os.os_store_address 
                        ELSE fs.fs_store_address 
                    END AS store_address,
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN os.os_store_lat 
                        ELSE fs.fs_store_lat 
                    END AS store_lat,
                    CASE 
                        WHEN so.so_created_by_store_type = 1 THEN os.os_store_lng 
                        ELSE fs.fs_store_lng 
                    END AS store_lng
                FROM sales_order AS so
                LEFT JOIN own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                LEFT JOIN franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                WHERE so.so_order_id = '{orderId}' 
                GROUP BY so.so_sale_item_id  
            """
            cursor.execute(get_order_store_details_query)
            store_data = cursor.fetchone()
            print(store_data)

            store_details = {
                "store_name": store_data['store_name'],
                "store_address": store_data['store_address'],
                "store_lat": store_data['store_lat'],
                "store_lng": store_data['store_lng'],

            }

            return {
                "status": True,
                "order_track": order_trak,
                "store_details": store_details
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
