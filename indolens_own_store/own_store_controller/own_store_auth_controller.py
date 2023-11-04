import datetime

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_own_store.own_store_model.response_model.own_store_emp_resp_model import get_own_store_employees

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def login(store_ob):
    try:
        with connection.cursor() as cursor:
            login_query = f"""SELECT ose.*, os.store_name, creator.name, updater.name FROM own_store_employees AS ose 
                                LEFT JOIN own_store AS os ON ose.assigned_store_id = os.store_id
                                LEFT JOIN admin AS creator ON ose.created_by = creator.admin_id
                                LEFT JOIN admin AS updater ON ose.last_updated_by = updater.admin_id
                                WHERE ose.email = '{store_ob.email}'"""
            cursor.execute(login_query)
            admin_data = cursor.fetchall()
            if admin_data is None:
                return {
                    "status": False,
                    "message": "Invalid user email",
                    "store": None
                }, 301
            elif admin_data[0][13] == 0:
                return {
                    "status": False,
                    "message": "You Account is locked, please contact you Admin",
                    "store": None
                }, 301
            elif admin_data[0][7] == 0:
                return {
                    "status": False,
                    "message": "You Account is not assigned to any store, please contact you Admin",
                    "store": None
                }, 301
            elif bcrypt.checkpw(store_ob.password.encode('utf-8'), admin_data[0][4].encode('utf-8')):
                return {
                    "status": True,
                    "message": "user login successfull",
                    "store": get_own_store_employees(admin_data)
                }, 200
            else:
                return {
                    "status": False,
                    "message": "Invalid user password",
                    "store": None
                }, 301

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
