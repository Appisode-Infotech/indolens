import datetime

import pymysql
import pytz
from django.db import connection

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
                    SELECT *
                    FROM sales_order
                    WHERE order_status {status_condition} AND created_by_store_type = {store_type} 
                    GROUP BY order_id          
                    """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                "status": True,
                "count": len(orders_list)
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
            total_sale = orders_list[0] if orders_list[0] is not None else 0

            return {
                "status": True,
                "sale": total_sale
            }, 200


    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_sales_expense_analytics(store_type):
    try:
        with connection.cursor() as cursor:
            get_order_query = f"""
                                SELECT
                                  os.store_id,
                                  os.store_name,
                                  IFNULL(SUM(so.product_total_cost), 0) AS total_sale
                                FROM
                                  own_store os
                                LEFT JOIN
                                  sales_order so ON os.store_id = so.created_by_store AND so.order_status != 7
                                GROUP BY
                                  os.store_id, os.store_name;

                                """
            cursor.execute(get_order_query)
            sales_list = cursor.fetchall()

            return {
                "status": True,
                "sale": sales_list
            }, 200


    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
