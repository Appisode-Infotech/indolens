import datetime
import json

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_franchise_store.franchise_store_model.franchise_store_resp_model.franchise_store_customer_resp_model import \
    get_franchise_store_customers

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def get_all_franchise_store_customers(store_id):
    try:
        with connection.cursor() as cursor:
            get_store_customers_query = f""" SELECT c.*, os.store_name, creator.name, updater.name,
                                            (SELECT SUM(so.product_total_cost) FROM sales_order AS so WHERE so.customer_id = c.customer_id AND so.order_status != 7) AS total_spend,
                                            (SELECT COUNT(DISTINCT so.order_id) FROM sales_order AS so WHERE so.customer_id = c.customer_id) AS order_count
                                            FROM customers AS c
                                            LEFT JOIN franchise_store AS os ON c.created_by_store_id = os.store_id
                                            LEFT JOIN franchise_store_employees AS creator ON c.created_by_employee_id = creator.employee_id
                                            LEFT JOIN franchise_store_employees AS updater ON c.updated_by_employee_id = updater.employee_id
                                            WHERE c.created_by_store_id = {store_id} AND c.created_by_store_type = 2 
                                            ORDER BY c.customer_id DESC"""
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
            get_store_customers_query = f""" SELECT c.*, os.store_name, creator.name, updater.name,
                                            (SELECT SUM(product_total_cost) AS total_spend FROM sales_order 
                                            WHERE customer_id = '{customer_id}'),
                                            (SELECT COUNT(DISTINCT order_id) AS order_count FROM sales_order WHERE customer_id = {customer_id})
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


def get_all_customers():
    try:
        with connection.cursor() as cursor:
            get_store_customers_query = f""" SELECT c.*, os.store_name, creator.name, updater.name,
                                            (SELECT SUM(so.product_total_cost) FROM sales_order AS so WHERE so.customer_id = c.customer_id) AS total_spend,
                                            (SELECT COUNT(DISTINCT so.order_id) FROM sales_order AS so WHERE so.customer_id = c.customer_id) AS order_count
                                            FROM customers AS c
                                            LEFT JOIN own_store AS os ON c.created_by_store_id = os.store_id
                                            LEFT JOIN own_store_employees AS creator ON c.created_by_employee_id = creator.employee_id
                                            LEFT JOIN own_store_employees AS updater ON c.updated_by_employee_id = updater.employee_id """
            cursor.execute(get_store_customers_query)
            store_customers = cursor.fetchall()
            return {
                "status": True,
                "customers_list": get_franchise_store_customers(store_customers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
