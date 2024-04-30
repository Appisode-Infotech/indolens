import datetime
import json

import bcrypt
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_franchise_store.franchise_store_model.franchise_store_resp_model.franchise_store_customer_resp_model import \
    get_franchise_store_customers

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def get_all_franchise_store_customers(store_id):
    try:
        with getConnection().cursor() as cursor:
            get_store_customers_query = f""" SELECT c.*, 
                                            CASE 
                                                WHEN c.customer_created_by_store_type = 1 THEN os.os_store_name 
                                                ELSE fs.fs_store_name 
                                            END AS store_name, 
                                            CASE 
                                                WHEN c.customer_created_by_store_type = 1 THEN creator_os.ose_name 
                                                ELSE creator_fs.fse_name 
                                            END AS creator_name,
                                            CASE 
                                                WHEN c.customer_updated_by_store_type = 1 THEN updater_os.ose_name 
                                                ELSE updater_fs.fse_name 
                                            END AS updater_name,
                                            COALESCE((SELECT SUM(so.so_product_total_cost) FROM sales_order AS so WHERE so.so_customer_id = c.customer_customer_id AND so.so_order_status != 7), 0) AS total_spend,
                                            (SELECT COUNT(DISTINCT so.so_order_id) FROM sales_order AS so WHERE so.so_customer_id = c.customer_customer_id) AS order_count
                                            FROM customers AS c
                                            LEFT JOIN own_store AS os ON c.customer_created_by_store_id = os.os_store_id
                                            LEFT JOIN franchise_store AS fs ON c.customer_created_by_store_id = fs.fs_store_id
                                            LEFT JOIN own_store_employees creator_os ON c.customer_created_by_employee_id = creator_os.ose_employee_id AND c.customer_created_by_store_type = 1
                                            LEFT JOIN franchise_store_employees creator_fs ON c.customer_created_by_employee_id = creator_fs.fse_employee_id AND c.customer_created_by_store_type = 2
                                            LEFT JOIN own_store_employees updater_os ON c.customer_updated_by_employee_id = updater_os.ose_employee_id AND c.customer_updated_by_store_type = 1
                                            LEFT JOIN franchise_store_employees updater_fs ON c.customer_updated_by_employee_id = updater_fs.fse_employee_id AND c.customer_updated_by_store_type = 2
                                            WHERE c.customer_created_by_store_id = {store_id} AND c.customer_created_by_store_type = 2
                                            ORDER BY c.customer_customer_id DESC"""
            cursor.execute(get_store_customers_query)
            store_customers = cursor.fetchall()
            return {
                "status": True,
                "store_customers_list": store_customers
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_customers_by_id(customer_id):
    try:
        with getConnection().cursor() as cursor:
            get_store_customers_query = f""" SELECT c.*, 
                                                CASE 
                                                    WHEN c.customer_created_by_store_type = 1 THEN os.os_store_name 
                                                    ELSE fs.fs_store_name 
                                                END AS store_name, 
                                                CASE 
                                                    WHEN c.customer_created_by_store_type = 1 THEN creator_os.ose_name 
                                                    ELSE creator_fs.fse_name 
                                                END AS creator_name,
                                                CASE 
                                                    WHEN c.customer_updated_by_store_type = 1 THEN updater_os.ose_name 
                                                    ELSE updater_fs.fse_name 
                                                END AS updater_name,
                                                COALESCE((SELECT SUM(so.so_product_total_cost) FROM sales_order AS so WHERE so.so_customer_id = c.customer_customer_id AND so.so_order_status != 7), 0) AS total_spend,
                                                (SELECT COUNT(DISTINCT so.so_order_id) FROM sales_order AS so WHERE so.so_customer_id = c.customer_customer_id) AS order_count
                                                FROM customers AS c
                                                LEFT JOIN own_store AS os ON c.customer_created_by_store_id = os.os_store_id
                                                LEFT JOIN franchise_store AS fs ON c.customer_created_by_store_id = fs.fs_store_id
                                                LEFT JOIN own_store_employees creator_os ON c.customer_created_by_employee_id = creator_os.ose_employee_id AND c.customer_created_by_store_type = 1
                                                LEFT JOIN franchise_store_employees creator_fs ON c.customer_created_by_employee_id = creator_fs.fse_employee_id AND c.customer_created_by_store_type = 2
                                                LEFT JOIN own_store_employees updater_os ON c.customer_updated_by_employee_id = updater_os.ose_employee_id AND c.customer_updated_by_store_type = 1
                                                LEFT JOIN franchise_store_employees updater_fs ON c.customer_updated_by_employee_id = updater_fs.fse_employee_id AND c.customer_updated_by_store_type = 2
                                                WHERE c.customer_customer_id = {customer_id} """
            cursor.execute(get_store_customers_query)

            store_customers = cursor.fetchone()
            return {
                "status": True,
                "customers": store_customers
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_customers():
    try:
        with getConnection().cursor() as cursor:
            get_store_customers_query = f""" SELECT c.*, os.os_store_name, 
                                            CASE 
                                                WHEN c.customer_created_by_store_type = 1 THEN creator_os.ose_name 
                                                ELSE creator_fs.fse_name 
                                            END AS creator_name,
                                            CASE 
                                                WHEN c.customer_updated_by_store_type = 1 THEN updater_os.ose_name 
                                                ELSE updater_fs.fse_name 
                                            END AS updater_name,
                                            (SELECT SUM(so.so_product_total_cost) FROM sales_order AS so WHERE so.so_customer_id = c.customer_customer_id) AS total_spend,
                                            (SELECT COUNT(DISTINCT so.so_order_id) FROM sales_order AS so WHERE so.so_customer_id = c.customer_customer_id) AS order_count
                                            FROM customers AS c
                                            LEFT JOIN own_store AS os ON c.customer_created_by_store_id = os.os_store_id                                            
                                            LEFT JOIN own_store_employees creator_os ON c.customer_created_by_employee_id = creator_os.ose_employee_id AND c.customer_created_by_store_type = 1
                                            LEFT JOIN franchise_store_employees creator_fs ON c.customer_created_by_employee_id = creator_fs.fse_employee_id AND c.customer_created_by_store_type = 2
                                            LEFT JOIN own_store_employees updater_os ON c.customer_updated_by_employee_id = updater_os.ose_employee_id AND c.customer_updated_by_store_type = 1
                                            LEFT JOIN franchise_store_employees updater_fs ON c.customer_updated_by_employee_id = updater_fs.fse_employee_id AND c.customer_updated_by_store_type = 2
                                            ORDER BY c.customer_customer_id DESC"""
            cursor.execute(get_store_customers_query)
            store_customers = cursor.fetchall()
            return {
                "status": True,
                "customers_list": store_customers
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
