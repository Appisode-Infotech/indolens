import datetime
import json

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_own_store.own_store_model.response_model.store_customer_resp_model import get_store_customers

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_all_store_customers(store_id):
    try:
        with connection.cursor() as cursor:
            get_store_customers_query = f""" SELECT c.*, os.store_name, creator.name, updater.name 
                                            FROM customers AS c
                                            LEFT JOIN own_store AS os ON c.created_by_store_id = os.store_id
                                            LEFT JOIN own_store_employees AS creator ON c.created_by_employee_id = creator.employee_id
                                            LEFT JOIN own_store_employees AS updater ON c.updated_by_employee_id = updater.employee_id
                                            WHERE c.created_by_store_id = {store_id} """
            cursor.execute(get_store_customers_query)
            store_customers = cursor.fetchall()
            print(store_customers)
            return {
                "status": True,
                "store_customers_list": get_store_customers(store_customers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

