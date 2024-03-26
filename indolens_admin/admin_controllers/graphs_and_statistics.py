import datetime
from datetime import datetime, timedelta

import pymysql
import pytz
from indolens.db_connection import connection

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def get_own_vs_franchise_sales_stats(start_date, end_date):
    try:
        with connection.cursor() as cursor:
            get_own_store_sales_stats_query = f"""
                                WITH RECURSIVE DateRange AS (
                                    SELECT '{start_date}' AS date
                                    UNION ALL
                                    SELECT DATE_ADD(date, INTERVAL 1 DAY)
                                    FROM DateRange
                                    WHERE DATE_ADD(date, INTERVAL 1 DAY) <= '{end_date}'
                                )
                                SELECT DateRange.date AS report_date, COALESCE(SUM(s.product_total_cost), 0) AS total_cost
                                FROM DateRange
                                LEFT JOIN sales_order s
                                ON DATE(s.created_on) = DateRange.date AND s.order_status != 7 AND s.created_by_store_type = 1
                                GROUP BY DateRange.date"""

            cursor.execute(get_own_store_sales_stats_query)
            own_store_sale_stats = cursor.fetchall()
            get_franchise_store_sales_stats_query = f"""
                                WITH RECURSIVE DateRange AS (
                                    SELECT '{start_date}' AS date
                                    UNION ALL
                                    SELECT DATE_ADD(date, INTERVAL 1 DAY)
                                    FROM DateRange
                                    WHERE DATE_ADD(date, INTERVAL 1 DAY) <= '{end_date}'
                                )
                                SELECT DateRange.date AS report_date, COALESCE(SUM(s.product_total_cost), 0) AS total_cost
                                FROM DateRange
                                LEFT JOIN sales_order s
                                ON DATE(s.created_on) = DateRange.date AND s.order_status != 7 AND s.created_by_store_type = 2
                                GROUP BY DateRange.date"""

            cursor.execute(get_franchise_store_sales_stats_query)
            franchise_store_sale_stats = cursor.fetchall()

            own_store_stats_list = [total_cost for _, total_cost in own_store_sale_stats]
            franchise_store_stats_list = [total_cost for _, total_cost in franchise_store_sale_stats]
            return {
                "status": True,
                "message": "stats fetched",
                "own_store_sale_stats": own_store_stats_list,
                "franchise_store_sale_stats": franchise_store_stats_list,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_store_sales_stats(start_date, end_date, store_type, store_id):
    try:
        with connection.cursor() as cursor:
            get_store_sales_stats_query = f"""
                                WITH RECURSIVE DateRange AS (
                                    SELECT '{start_date}' AS date
                                    UNION ALL
                                    SELECT DATE_ADD(date, INTERVAL 1 DAY)
                                    FROM DateRange
                                    WHERE DATE_ADD(date, INTERVAL 1 DAY) <= '{end_date}'
                                )
                                SELECT DateRange.date AS report_date, COALESCE(SUM(s.product_total_cost), 0) AS total_cost
                                FROM DateRange
                                LEFT JOIN sales_order s
                                ON DATE(s.created_on) = DateRange.date AND s.order_status != 7 
                                AND s.created_by_store_type = {store_type} AND s.created_by_store = {store_id}
                                GROUP BY DateRange.date"""

            cursor.execute(get_store_sales_stats_query)
            store_sale_stats = cursor.fetchall()

            store_stats_list = [total_cost for _, total_cost in store_sale_stats]
            return {
                "status": True,
                "message": "stats fetched",
                "store_sale_stats": store_stats_list,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_customer_stats(days):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days - 1)).strftime('%Y-%m-%d')
    try:
        with connection.cursor() as cursor:
            get_customer_stats_query = f"""
                                WITH RECURSIVE DateRange AS (
                                    SELECT '{start_date}' AS date
                                    UNION ALL
                                    SELECT DATE_ADD(date, INTERVAL 1 DAY)
                                    FROM DateRange
                                    WHERE DATE_ADD(date, INTERVAL 1 DAY) <= '{end_date}'
                                )
                                SELECT DateRange.date AS report_date, COALESCE(COUNT(c.customer_id), 0) AS total_customer
                                FROM DateRange
                                LEFT JOIN customers c
                                ON DATE(c.created_on) = DateRange.date
                                GROUP BY DateRange.date"""

            cursor.execute(get_customer_stats_query)
            customer_stats = cursor.fetchall()

            customer_stats_list = [total_cost for _, total_cost in customer_stats]
            return {
                "status": True,
                "message": "stats fetched",
                "customer_stats": customer_stats_list,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_store_customer_stats(days, store_type, store_id):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days - 1)).strftime('%Y-%m-%d')
    try:
        with connection.cursor() as cursor:
            get_customer_stats_query = f"""
                                WITH RECURSIVE DateRange AS (
                                    SELECT '{start_date}' AS date
                                    UNION ALL
                                    SELECT DATE_ADD(date, INTERVAL 1 DAY)
                                    FROM DateRange
                                    WHERE DATE_ADD(date, INTERVAL 1 DAY) <= '{end_date}'
                                )
                                SELECT DateRange.date AS report_date, COALESCE(COUNT(c.customer_id), 0) AS total_customer
                                FROM DateRange
                                LEFT JOIN customers c
                                ON DATE(c.created_on) = DateRange.date AND c.created_by_store_id = {store_id} 
                                AND c.created_by_store_type = {store_type}
                                GROUP BY DateRange.date"""

            cursor.execute(get_customer_stats_query)
            customer_stats = cursor.fetchall()

            customer_stats_list = [total_cost for _, total_cost in customer_stats]
            return {
                "status": True,
                "message": "stats fetched",
                "customer_stats": customer_stats_list,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_orders_stats(days):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days - 1)).strftime('%Y-%m-%d')
    try:
        with connection.cursor() as cursor:
            get_order_stats_query = f"""
                                WITH RECURSIVE DateRange AS (
                                    SELECT '{start_date}' AS date
                                    UNION ALL
                                    SELECT DATE_ADD(date, INTERVAL 1 DAY)
                                    FROM DateRange
                                    WHERE DATE_ADD(date, INTERVAL 1 DAY) <= '{end_date}'
                                )
                                SELECT DateRange.date AS report_date, COALESCE(COUNT(DISTINCT s.order_id), 0) AS total_order
                                FROM DateRange
                                LEFT JOIN sales_order s
                                ON DATE(s.created_on) = DateRange.date
                                GROUP BY DateRange.date"""

            cursor.execute(get_order_stats_query)
            order_stats = cursor.fetchall()

            order_stats_list = [total_cost for _, total_cost in order_stats]
            return {
                "status": True,
                "message": "stats fetched",
                "order_stats": order_stats_list,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_store_orders_stats(days, store_type, store_id):
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days - 1)).strftime('%Y-%m-%d')
    try:
        with connection.cursor() as cursor:
            get_order_stats_query = f"""
                                WITH RECURSIVE DateRange AS (
                                    SELECT '{start_date}' AS date
                                    UNION ALL
                                    SELECT DATE_ADD(date, INTERVAL 1 DAY)
                                    FROM DateRange
                                    WHERE DATE_ADD(date, INTERVAL 1 DAY) <= '{end_date}'
                                )
                                SELECT DateRange.date AS report_date, COALESCE(COUNT(DISTINCT s.order_id), 0) AS total_order
                                FROM DateRange
                                LEFT JOIN sales_order s
                                ON DATE(s.created_on) = DateRange.date AND s.created_by_store_type = {store_type} 
                                AND s.created_by_store = {store_id}
                                GROUP BY DateRange.date"""

            cursor.execute(get_order_stats_query)
            order_stats = cursor.fetchall()

            order_stats_list = [total_cost for _, total_cost in order_stats]
            return {
                "status": True,
                "message": "stats fetched",
                "order_stats": order_stats_list,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
