import datetime
import json

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_franchise_store.franchise_store_model.franchise_store_resp_model.franchise_store_customer_resp_model import \
    get_franchise_store_customers

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_all_franchise_store_customers(store_id):
    try:
        with connection.cursor() as cursor:
            get_store_customers_query = f""" SELECT c.*, os.store_name, creator.name, updater.name 
                                            FROM customers AS c
                                            LEFT JOIN franchise_store AS os ON c.created_by_store_id = os.store_id
                                            LEFT JOIN franchise_store_employees AS creator ON c.created_by_employee_id = creator.employee_id
                                            LEFT JOIN franchise_store_employees AS updater ON c.updated_by_employee_id = updater.employee_id
                                            WHERE c.created_by_store_id = {store_id} AND c.created_by_store_type = 2 """
            cursor.execute(get_store_customers_query)
            store_customers = cursor.fetchall()
            return {
                "status": True,
                "store_customers_list": get_franchise_store_customers(store_customers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_customers_by_id(customer_id):
    try:
        with connection.cursor() as cursor:
            get_store_customers_query = f""" SELECT c.*, os.store_name, creator.name, updater.name 
                                            FROM customers AS c
                                            LEFT JOIN franchise_store AS os ON c.created_by_store_id = os.store_id
                                            LEFT JOIN franchise_store_employees AS creator ON c.created_by_employee_id = creator.employee_id
                                            LEFT JOIN franchise_store_employees AS updater ON c.updated_by_employee_id = updater.employee_id
                                            WHERE c.customer_id = {customer_id} """
            cursor.execute(get_store_customers_query)
            store_customers = cursor.fetchall()
            return {
                "status": True,
                "customers": get_franchise_store_customers(store_customers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

