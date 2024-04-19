import datetime
import json

import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_models.admin_resp_model.master_units_resp_model import get_master_units

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def add_masters_units(data):
    try:
        with getConnection().cursor() as cursor:
            insert_master_units_query = f"""
                INSERT INTO units (
                    unit_name, unit_status, unit_created_on, unit_created_by, unit_last_updated_on,
        unit_last_updated_by
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
        with getConnection().cursor() as cursor:
            update_master_units_query = f"""
                UPDATE units SET
                    unit_name = '{data['unit_name']}',  
                    unit_last_updated_on = '{getIndianTime()}',
                    unit_last_updated_by = '{data['updated_by']}'
                WHERE unit_unit_id = {data['unit_id']}
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
        with getConnection().cursor() as cursor:
            get_units_query = f""" SELECT  
                u.unit_unit_id, 
                u.unit_name, 
                u.unit_status,
                CASE 
                    WHEN u.unit_status = 1 THEN 'Active'
                    ELSE 'Inactive'
                END AS status, 
                DATE_FORMAT(u.unit_created_on, '%d/%m/%Y %h:%i %p') AS unit_created_on, 
                DATE_FORMAT(u.unit_last_updated_on, '%d/%m/%Y %h:%i %p') AS unit_last_updated_on, 
                creator.admin_name AS creator, updater.admin_name AS updater
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
        with getConnection().cursor() as cursor:
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