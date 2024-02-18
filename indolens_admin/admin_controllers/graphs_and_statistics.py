import datetime

import pymysql
import pytz
from django.db import connection

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def get_own_vs_franchise_sales_stats(start_date, end_date):
    print(start_date)
    print(end_date)
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
