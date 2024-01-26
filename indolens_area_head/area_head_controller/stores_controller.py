import datetime

import pymysql
import pytz
import requests
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.franchise_store_resp_model import get_franchise_store
from indolens_admin.admin_models.admin_resp_model.own_store_resp_model import get_own_store

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_area_head_own_stores(status, assigned_stores):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    stores = tuple(assigned_stores)

    try:
        with connection.cursor() as cursor:

            get_own_stores_query = f"""
                                        SELECT own_store.*, own_store_employees.name, own_store_employees.employee_id AS manager_name
                                        FROM own_store
                                        LEFT JOIN own_store_employees ON own_store.store_id = own_store_employees.assigned_store_id AND own_store_employees.role = 1
                                        WHERE own_store.status {status_condition} AND own_store.store_id IN {stores}
                                        ORDER BY own_store.store_id DESC
                                        """
            cursor.execute(get_own_stores_query)
            stores_data = cursor.fetchall()
            print(stores_data)
            return {
                "status": True,
                "own_stores": get_own_store(stores_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


