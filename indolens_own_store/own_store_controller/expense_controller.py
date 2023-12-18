import datetime
import re

import pymysql
import pytz
from django.db import connection

from indolens_own_store.own_store_controller import lens_sale_power_attribute_controller
from indolens_own_store.own_store_model.response_model.store_expense_resp_model import get_store_expenses

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_store_expense(expense_obj):
    try:
        with connection.cursor() as cursor:
            insert_expense_obj_query = f"""
                            INSERT INTO store_expense (
                                store_id, store_type, expense_amount, expense_reason, expense_date, created_on, created_by
                            ) VALUES ( 
                                '{expense_obj.store_id}', '{expense_obj.store_type}', '{expense_obj.expense_amount}', 
                                '{expense_obj.expense_reason}', '{today}', '{today}', '{expense_obj.created_by}') """

            cursor.execute(insert_expense_obj_query)
            return {
                "status": True,
                "message": f"Expense of amount:{expense_obj.expense_amount} added successfully for {expense_obj.expense_reason}"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_store_expense(store_id, store_type):
    try:
        with connection.cursor() as cursor:
            insert_expense_obj_query = f""" SELECT se.*, creator.name FROM store_expense AS se
                                            LEFT JOIN own_store_employees AS creator ON se.created_by = creator.employee_id
                                            WHERE se.store_id = {store_id} AND se.store_type= {store_type}"""
            cursor.execute(insert_expense_obj_query)
            store_expense_data = cursor.fetchall()
            return {
                "status": True,
                "message": "success",
                "stor_expense_list": get_store_expenses(store_expense_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def make_sale(cart_data, customerData, billingDetailsData):
    try:
        with connection.cursor() as cursor:
            for data in cart_data:
                new_data = {re.sub(r'\[\d+\]', '', key): value for key, value in data.items()}
                print("======================")
                if new_data.get('product_category_id') == '2':
                    print("===============================lense===============================")
                    print(new_data)
                    power_attributes = lens_sale_power_attribute_controller.get_power_attribute(new_data)
                elif new_data.get('product_category_id') == '3':
                    print("===============================Contact lense===============================")
                    print(new_data)
                    power_attributes = lens_sale_power_attribute_controller.get_power_attribute(new_data)
                else:
                    print("===============================Other Products===============================")
                    print(new_data)

            return {
                "status": True,
                "message": "success"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301