import datetime

import bcrypt
import pymysql
import pytz
from django.db import connection

from indolens_franchise_store.franchise_store_model.franchise_store_resp_model.franchise_store_emp_resp_model import \
    get_franchise_store_employees

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def login(store_ob):
    try:
        with connection.cursor() as cursor:
            login_query = f"""SELECT fse.*, fs.store_name, creator.name, updater.name FROM franchise_store_employees AS fse 
                                LEFT JOIN franchise_store AS fs ON fse.assigned_store_id = fs.store_id
                                LEFT JOIN admin AS creator ON fse.created_by = creator.admin_id
                                LEFT JOIN admin AS updater ON fse.last_updated_by = updater.admin_id
                                WHERE fse.email = '{store_ob.email}'"""
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
                    "store": get_franchise_store_employees(admin_data)
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
