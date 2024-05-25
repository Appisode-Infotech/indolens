import datetime
import pymysql
import pytz
from indolens.db_connection import getConnection

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def get_order_stats(status, store_type):
    status_conditions = {
        "New": "= 1",
        "Completed": "= 5",
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                                    SELECT COUNT(DISTINCT so_order_id)  AS order_stats
                                    FROM sales_order
                                    WHERE so_order_status {status_condition} AND so_created_by_store_type = {store_type} 
                                    GROUP BY so_order_id  
                                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                "status": True,
                "count": orders_list['order_stats']
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_sales_stats(store):
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                                SELECT IFNULL(SUM(product_total_cost), 0) AS total_sale
                                FROM sales_order
                                WHERE created_by_store_type = {store} 
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


def get_store_employee_stats(store):
    print(store)
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                                SELECT COUNT(*) AS employee_count
                                FROM own_store_employees
                                WHERE ose_assigned_store_id IN {store} 
                                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchone()

            stores_tuple = eval(store)

            return {
                "status": True,
                "employee_count": orders_list['employee_count'],
                "store_count": len(stores_tuple)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301