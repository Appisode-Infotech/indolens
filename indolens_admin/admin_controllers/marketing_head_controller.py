import json

import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.marketing_head_resp_model import get_marketing_heads

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_marketing_head(marketing_head, files):
    try:
        with connection.cursor() as cursor:
            insert_marketing_head_query = f"""
                INSERT INTO marketing_head (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, document_2_type, document_2_url, 
                    status, created_by, created_on, last_updated_by, last_updated_on
                ) VALUES (
                    '{marketing_head.fullName}', '{marketing_head.email}', '{marketing_head.phone}', '{marketing_head.password}',
                    '{files.profile_pic}', '{marketing_head.completeAddress}', '{marketing_head.document_1_type}', 
                    '{json.dumps(files.document1)}', '{marketing_head.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{marketing_head.created_by}', '{today}', '{marketing_head.last_updated_by}', '{today}'
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_marketing_head_query)
            mhid = cursor.lastrowid

            return {
                "status": True,
                "message": "Marketing Head added",
                "mhid": mhid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def marketing_heads_list(marketing_heads):
    pass


def get_all_marketing_head():
    try:
        with connection.cursor() as cursor:
            get_marketing_head_query = f"""
            SELECT mh.*, creator.name, updater.name, ah.name
            FROM marketing_head AS mh
            LEFT JOIN area_head AS ah ON mh.assigned_area_head = ah.area_head_id
            LEFT JOIN admin AS creator ON mh.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON mh.last_updated_by = updater.admin_id
            GROUP BY mh.marketing_head_id
            """
            cursor.execute(get_marketing_head_query)
            marketing_head = cursor.fetchall()
            print(marketing_head)

            return {
                "status": True,
                "marketing_heads_list": get_marketing_heads(marketing_head)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_marketing_head_by_id(mhid):
    try:
        with connection.cursor() as cursor:
            get_marketing_head_query = f"""
            SELECT mh.*, creator.name, updater.name, ah.name
            FROM marketing_head AS mh
            LEFT JOIN area_head AS ah ON mh.assigned_area_head = ah.area_head_id
            LEFT JOIN admin AS creator ON mh.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON mh.last_updated_by = updater.admin_id
            WHERE marketing_head_id = '{mhid}'
            GROUP BY mh.marketing_head_id
            """
            cursor.execute(get_marketing_head_query)
            marketing_head = cursor.fetchall()
            print(marketing_head)

            return {
                "status": True,
                "marketing_head": get_marketing_heads(marketing_head)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_marketing_head(mhid, status):
    try:
        with connection.cursor() as cursor:
            update_marketing_head_query = f"""
                UPDATE marketing_head
                SET
                    status = {status}
                WHERE
                    marketing_head_id = {mhid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_marketing_head_query)

            return {
                "status": True,
                "message": "Marketing  Head updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301