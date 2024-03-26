import datetime

import pymysql
import pytz
from indolens.db_connection import connection

from indolens_admin.admin_models.admin_resp_model.store_analytics_resp_model import store_analytics

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_order_stats(status, store_type):
    status_conditions = {
        "New": "= 1",
        "Completed": "= 6",
    }
    status_condition = status_conditions[status]
    try:
        with connection.cursor() as cursor:
            get_order_query = f"""
                    SELECT count(*)
                    FROM sales_order
                    WHERE order_status {status_condition} AND created_by_store_type = {store_type} 
                    GROUP BY order_id          
                    """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchone()
            if orders_list is None:
                count = 0
            else:
                count = orders_list['count(*)']
            return {
                "status": True,
                "count": count
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_sales_stats(store):
    try:
        with connection.cursor() as cursor:
            get_order_query = f"""
                                SELECT IFNULL(SUM(product_total_cost), 0) AS total_sale
                                FROM sales_order
                                WHERE created_by_store_type = {store} AND order_status != 7
                                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchone()
            return {
                "status": True,
                "sale": orders_list['total_sale']
            }, 200


    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_store_analytics():
    try:
        with connection.cursor() as cursor:
            own_store_sales_query = f"""
                SELECT
                    os.store_id,
                    os.store_name,
                    COALESCE(SUM(so.product_total_cost), 0) AS total_sale,
                    COALESCE((SELECT IFNULL(SUM(expense_amount), 0) 
                              FROM store_expense 
                              WHERE store_id = os.store_id 
                                AND store_type = 1), 0) AS total_expense,
                    COALESCE(SUM(so.product_total_cost), 0) - COALESCE((SELECT IFNULL(SUM(expense_amount), 0) 
                                                                         FROM store_expense 
                                                                         WHERE store_id = os.store_id 
                                                                           AND store_type = 1), 0) AS net_profit
                FROM
                    own_store os
                LEFT JOIN
                    sales_order so ON os.store_id = so.created_by_store 
                                  AND so.created_by_store_type = 1 
                                  AND so.order_status != 7
                GROUP BY
                    os.store_id, os.store_name;
            """

            cursor.execute(own_store_sales_query)
            own_sales_analytics = cursor.fetchall()

            franchise_store_sales_query = f"""
                                 SELECT
                                    fs.store_id,
                                    fs.store_name,
                                    COALESCE(SUM(so.product_total_cost), 0) AS total_sale,
                                    COALESCE((SELECT IFNULL(SUM(expense_amount), 0) 
                                              FROM store_expense 
                                              WHERE store_id = fs.store_id 
                                                AND store_type = 2), 0) AS total_expense,
                                    COALESCE(SUM(so.product_total_cost), 0) - COALESCE((SELECT IFNULL(SUM(expense_amount), 0) 
                                                                                         FROM store_expense 
                                                                                         WHERE store_id = fs.store_id 
                                                                                           AND store_type = 2), 0) AS net_profit
                                FROM
                                    franchise_store fs
                                LEFT JOIN
                                    sales_order so ON fs.store_id = so.created_by_store 
                                                  AND so.created_by_store_type = 2 
                                                  AND so.order_status != 7
                                GROUP BY
                                    fs.store_id, fs.store_name; """
            cursor.execute(franchise_store_sales_query)
            franchise_sales_analytics = cursor.fetchall()

            return {
                "status": True,
                "own_sales_analytics": own_sales_analytics,
                "franchise_sales_analytics": franchise_sales_analytics
            }, 200


    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
