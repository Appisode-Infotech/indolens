import json

import pymysql
from django.db import connection

from indolens_admin.admin_models.admin_req_model import admin_auth_model
from indolens_admin.admin_models.admin_resp_model.admin_auth_resp_model import get_admin_user


def login(admin_obj):
    try:
        with connection.cursor() as cursor:
            login_query = f"""SELECT * FROM admin WHERE email = '{admin_obj.email}';"""
            cursor.execute(login_query)
            admin_data = cursor.fetchone()
            if admin_data is None:
                return {
                    "status": False,
                    "message": "Invalid admin email",
                    "admin": None
                }, 301
            elif admin_data[4] != admin_obj.password:
                return {
                    "status": False,
                    "message": "Invalid admin password",
                    "admin": None
                }, 301
            else:
                return {
                    "status": True,
                    "message": "admin login successfull",
                    "admin": admin_auth_model.admin_auth_model_from_dict(get_admin_user(admin_data))
                }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301