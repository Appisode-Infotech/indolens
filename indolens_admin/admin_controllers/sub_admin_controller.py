import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.own_store_resp_model import get_own_store

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_sub_admin(sub_admin):
    try:
        with connection.cursor() as cursor:
            create_sub_admin_query = f""" """

            cursor.execute(create_sub_admin_query)
            return {
                "status": True,
                "message": "sub admin added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301



