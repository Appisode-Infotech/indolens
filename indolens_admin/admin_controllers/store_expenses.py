import datetime
import pymysql
import pytz
from django.db import connection

def get_store_expense(store_id, store_type):
    try:
        with connection.cursor() as cursor:
            get_store_expense_query = f"""
                SELECT IFNULL(SUM(expense_amount), 0) AS total_expense 
                FROM store_expense 
                WHERE store_id = {store_id} 
                AND store_type = {store_type}
            """
            cursor.execute(get_store_expense_query)
            expense = cursor.fetchone()

            return {
                "status": True,
                "store_expense": expense[0]
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
