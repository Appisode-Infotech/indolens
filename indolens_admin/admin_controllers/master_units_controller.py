import datetime
import json

import pymysql
import pytz
from indolens.db_connection import connection

from indolens_admin.admin_models.admin_resp_model.master_units_resp_model import get_master_units

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def add_masters_units(data):
    try:
        with connection.cursor() as cursor:
            insert_master_units_query = f"""
                INSERT INTO units (
                    unit_name,  status, created_on, created_by,  last_updated_on,
                    last_updated_by
                ) VALUES (
                    '{data['unit_name']}', 0,  '{getIndianTime()}','{data['created_by']}',  '{getIndianTime()}', '{data['created_by']}'
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_master_units_query)
            uid = cursor.lastrowid

            return {
                "status": True,
                "message": "Units added",
                "uid": uid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def edit_master_units(data):
    try:
        with connection.cursor() as cursor:
            update_master_units_query = f"""
                UPDATE  units SET
                    unit_name = '{data['unit_name']}',  last_updated_on = '{getIndianTime()}',
                    last_updated_by = {data['updated_by']}
                    WHERE unit_id = {data['unit_id']}
            """

            # Execute the query using your cursor
            cursor.execute(update_master_units_query)
            uid = cursor.lastrowid

            return {
                "status": True,
                "message": "Units updated",
                "uid": uid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_units():
    try:
        with connection.cursor() as cursor:
            get_units_query = f""" SELECT u.*, creator.admin_name, updater.admin_name 
                                           FROM units AS u
                                            LEFT JOIN admin AS creator ON u.unit_created_by = creator.admin_admin_id
                                            LEFT JOIN admin AS updater ON u.unit_last_updated_by = updater.admin_admin_id
                                            ORDER BY u.unit_unit_id ASC
                                             """
            cursor.execute(get_units_query)
            master_units = cursor.fetchall()
            return {
                       "status": True,
                       "units_list": master_units

                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def enable_disable_master_units(uid, status):
    try:
        with connection.cursor() as cursor:
            set_units_query = f"""
            UPDATE units SET unit_status = '{status}' WHERE unit_unit_id = '{uid}';
            """
            cursor.execute(set_units_query)

            return {
                "status": True,
                "message": "Updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301