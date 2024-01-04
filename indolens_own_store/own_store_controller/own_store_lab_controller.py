import datetime

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.lab_resp_model import get_labs

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_all_active_labs():
    try:
        with connection.cursor() as cursor:
            get_lab_query = f""" SELECT l.*, creator.name, updater.name, lt.name, 
                                COUNT(DISTINCT CASE WHEN so.order_status IN (1, 2, 3) THEN so.order_id END)
                                FROM lab AS l
                                LEFT JOIN lab_technician AS lt ON lt.assigned_lab_id = l.lab_id
                                LEFT JOIN admin AS creator ON l.created_by = creator.admin_id
                                LEFT JOIN admin AS updater ON l.last_updated_by = updater.admin_id
                                LEFT JOIN sales_order AS so ON l.lab_id = so.assigned_lab
                                WHERE l.status = 1
                                GROUP BY l.lab_id
                                ORDER BY l.lab_id DESC"""
            cursor.execute(get_lab_query)
            lab_data = cursor.fetchall()
            return {
                "status": True,
                "lab_list": get_labs(lab_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_by_id(labid):
    try:
        with connection.cursor() as cursor:
            get_lab_query = f""" SELECT l.*, creator.name, updater.name, lt.name,  COUNT(DISTINCT so.order_id) AS order_count
                                FROM lab AS l
                                LEFT JOIN lab_technician AS lt ON lt.assigned_lab_id = l.lab_id
                                LEFT JOIN admin AS creator ON l.created_by = creator.admin_id
                                LEFT JOIN admin AS updater ON l.last_updated_by = updater.admin_id
                                LEFT JOIN sales_order AS so ON l.lab_id = so.assigned_lab
                                WHERE lab_id = '{labid}'"""
            cursor.execute(get_lab_query)
            lab_data = cursor.fetchall()
            return {
                "status": True,
                "lab_data": get_labs(lab_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
