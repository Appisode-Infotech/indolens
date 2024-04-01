import datetime
import pymysql
import pytz
from indolens.db_connection import getConnection

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def get_order_stats(status, store_type, store_id):
    status_conditions = {
        "New": "= 1",
        "Completed": "= 6",
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                    SELECT *
                    FROM sales_order
                    WHERE order_status {status_condition} AND created_by_store_type = {store_type} AND created_by_store = {store_id}
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


def get_sales_stats(store_type, store_id):
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                                SELECT IFNULL(SUM(product_total_cost), 0) AS total_sale
                                FROM sales_order
                                WHERE created_by_store_type = {store_type} AND created_by_store = {store_id} AND
                                order_status != 7
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