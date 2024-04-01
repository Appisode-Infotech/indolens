import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_models.admin_resp_model.store_expenses_resp_model import get_store_expenses


def get_store_expense_amount(store_id, store_type):
    try:
        with getConnection().cursor() as cursor:
            get_store_expense_query = f"""
                SELECT IFNULL(SUM(se_expense_amount), 0) AS total_expense 
                FROM store_expense 
                WHERE se_store_id = {store_id} 
                AND se_store_type = {store_type}
            """
            cursor.execute(get_store_expense_query)
            expense = cursor.fetchone()

            total_expense = expense['total_expense'] if expense['total_expense'] is not None else 0

            return {
                "status": True,
                "store_expense": total_expense
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_store_expense_list(store_id, store_type):
    try:
        with getConnection().cursor() as cursor:
            get_store_expense_query = f"""
                SELECT se.*, CASE 
                           WHEN se.se_store_type = 1 THEN creator_own.ose_name
                           WHEN se.se_store_type = 2 THEN creator_franchise.fse_name
                       END AS creator_name
                FROM store_expense AS se
                LEFT JOIN own_store_employees AS creator_own ON se.se_created_by = creator_own.ose_employee_id AND se.se_store_type = 1
                LEFT JOIN franchise_store_employees AS creator_franchise ON se.se_created_by = creator_franchise.fse_employee_id AND se.se_store_type = 2
                WHERE se.se_store_id = {store_id} 
                AND se.se_store_type = {store_type}
            """
            cursor.execute(get_store_expense_query)
            expense = cursor.fetchall()

            return {
                "status": True,
                "store_expense": expense
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
