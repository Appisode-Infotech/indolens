import pymysql
import pytz
from indolens.db_connection import connection

from indolens_admin.admin_models.admin_resp_model.store_expenses_resp_model import get_store_expenses


def get_store_expense_amount(store_id, store_type):
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


def get_store_expense_list(store_id, store_type):
    print(store_id, store_type)
    try:
        with connection.cursor() as cursor:
            get_store_expense_query = f"""
                SELECT se.*, CASE 
                           WHEN se.store_type = 1 THEN creator_own.name
                           WHEN se.store_type = 2 THEN creator_franchise.name
                       END AS creator_name
                FROM store_expense AS se
                LEFT JOIN own_store_employees AS creator_own ON se.created_by = creator_own.employee_id AND se.store_type = 1
                LEFT JOIN franchise_store_employees AS creator_franchise ON se.created_by = creator_franchise.employee_id AND se.store_type = 2
                WHERE se.store_id = {store_id} 
                AND se.store_type = {store_type}
            """
            cursor.execute(get_store_expense_query)
            expense = cursor.fetchall()

            return {
                "status": True,
                "store_expense": get_store_expenses(expense)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
