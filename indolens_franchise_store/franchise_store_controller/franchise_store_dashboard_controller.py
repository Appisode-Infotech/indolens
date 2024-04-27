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
                        SELECT COUNT(DISTINCT so_order_id)  AS order_stats
                        FROM sales_order
                        WHERE so_order_status {status_condition} 
                            AND so_created_by_store_type = '{store_type}' 
                            AND so_created_by_store = '{store_id}'
                    """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchone()

            return {
                "status": True,
                "count": orders_list['order_stats']
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_sales_stats(store_type, store_id):
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                                SELECT IFNULL(SUM(so_product_total_cost), 0) AS total_sale
                                FROM sales_order
                                WHERE so_created_by_store_type = {store_type} AND so_created_by_store = {store_id} AND
                                so_order_status != 7
                                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchone()

            return {
                "status": True,
                "sale": orders_list['total_sale'] if orders_list['total_sale'] is not None else 0
            }, 200


    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301