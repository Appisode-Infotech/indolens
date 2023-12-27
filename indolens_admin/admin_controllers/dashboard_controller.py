import datetime
import pymysql
import pytz
from django.db import connection

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_order_stats(status, store_type):
    status_conditions = {
        "New": "= 1",
        "Completed": "= 5",
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
                        SELECT SUM(product_total_cost) AS total_sale
                        FROM sales_order
                        WHERE created_by_store_type = {store} 
                        """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchone()
            print(orders_list[0])

            return {
                "status": True,
                "sale": orders_list[0]
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301