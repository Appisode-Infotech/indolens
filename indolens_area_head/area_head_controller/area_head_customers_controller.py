import datetime
import json

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.customer_resp_model import get_customers

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_all_area_stores_customers(assigned_stores):
    try:
        with connection.cursor() as cursor:
            get_store_customers_query = f""" SELECT c.*, os.store_name, creator.name, updater.name 
                                            FROM customers AS c
                                            LEFT JOIN own_store AS os ON c.created_by_store_id = os.store_id
                                            LEFT JOIN own_store_employees AS creator ON c.created_by_employee_id = creator.employee_id
                                            LEFT JOIN own_store_employees AS updater ON c.updated_by_employee_id = updater.employee_id 
                                            WHERE c.created_by_store_type = 1 AND c.created_by_store_id IN {tuple(assigned_stores)} """
            cursor.execute(get_store_customers_query)
            store_customers = cursor.fetchall()
            return {
                "status": True,
                "customers_list": get_customers(store_customers)
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
                                            LEFT JOIN own_store AS os ON c.created_by_store_id = os.store_id
                                            LEFT JOIN own_store_employees AS creator ON c.created_by_employee_id = creator.employee_id
                                            LEFT JOIN own_store_employees AS updater ON c.updated_by_employee_id = updater.employee_id
                                            WHERE c.customer_id = {customer_id} """
            cursor.execute(get_store_customers_query)
            store_customers = cursor.fetchall()
            return {
                "status": True,
                "customer": get_customers(store_customers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

