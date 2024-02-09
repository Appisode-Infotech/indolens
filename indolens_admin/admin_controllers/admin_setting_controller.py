import datetime
import string
import random

import bcrypt
import pymysql
from django.db import connection

import pytz

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def admin_setting(setting_obj):
    try:
        with connection.cursor() as cursor:
            # update_pwd_code_query = f"""INSERT INTO reset_password (email)
            #                                             VALUES ({setting_obj})"""
            # cursor.execute(update_pwd_code_query)
            return "ok"

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
