import datetime
import json
import string
import random

import bcrypt
import pymysql
import pytz
import requests
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.admin_auth_resp_model import get_admin_user
from indolens_area_head.area_head_model.area_head_resp_models.area_head_resp_model import get_area_heads
from migrate_db import cursor

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)

def login(area_head):
    print(area_head.password)
    try:
        with connection.cursor() as cursor:
            login_query = f""" SELECT * 
                                FROM area_head                                
                                WHERE email = '{area_head.email}'"""
            cursor.execute(login_query)
            area_head_data = cursor.fetchall()
            print(area_head_data)
            
            if area_head_data is None:
                return {
                    "status": False,
                    "message": "Invalid email provided",
                    "area_head": None
                }, 301

            elif area_head is not None and area_head_data[0][12] != 0:
                if bcrypt.checkpw(area_head.password.encode('utf-8'), area_head_data[0][4].encode('utf-8')):
                    return {
                        "status": True,
                        "message": "Area Head login successfully",
                        "area_head": get_area_heads(area_head_data)
                    }, 200
                else:
                    return {
                        "status": False,
                        "message": "Invalid password provided",
                        "area_head": None
                    }, 301
            elif area_head is not None and area_head_data[0][12] == 0:
                return {
                    "status": False,
                    "message": "The id has been blocked, please contact admin",
                    "area_head": None
                }, 301

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
