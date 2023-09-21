import json

import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.accountant_resp_model import get_accountants
from indolens_admin.admin_models.admin_resp_model.sales_executive_resp_model import get_sales_executives

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_accountant(accountant, files):
    try:
        with connection.cursor() as cursor:
            insert_accountant_query = f"""
                INSERT INTO accountant (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, document_2_type, document_2_url, 
                    status, created_by, created_on, last_updated_by, last_updated_on
                ) VALUES (
                    '{accountant.name}', '{accountant.email}', '{accountant.phone}', '{accountant.password}',
                    '{files.profile_pic}', '{accountant.address}', '{accountant.document_1_type}', 
                    '{json.dumps(files.document1)}', '{accountant.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{accountant.created_by}', '{today}', '{accountant.last_updated_by}', '{today}'
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_accountant_query)
            aid = cursor.lastrowid

            return {
                "status": True,
                "message": "Accountant Added",
                "aid": aid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301



def get_all_accountant():
    try:
        with connection.cursor() as cursor:
            get_accountant_query = f"""
            SELECT ac.*, creator.name, updater.name
            FROM accountant AS ac
            LEFT JOIN admin AS creator ON ac.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON ac.last_updated_by = updater.admin_id
            GROUP BY ac.accountant_id
            """
            cursor.execute(get_accountant_query)
            accountant = cursor.fetchall()
            print(accountant)

            return {
                "status": True,
                "accountant_list": get_accountants(accountant)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_accountant_by_id(aid):
    try:
        with connection.cursor() as cursor:
            get_accountant_query = f"""
            SELECT ac.*, creator.name, updater.name
            FROM accountant AS ac
            LEFT JOIN admin AS creator ON ac.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON ac.last_updated_by = updater.admin_id
            WHERE accountant_id = '{aid}'
            GROUP BY ac.accountant_id
            """
            cursor.execute(get_accountant_query)
            accountant = cursor.fetchall()

            return {
                "status": True,
                "accountant": get_accountants(accountant)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_accountant(aid, status):
    try:
        with connection.cursor() as cursor:
            update_accountant_query = f"""
                UPDATE accountant
                SET
                    status = {status}
                WHERE
                    accountant_id = {aid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_accountant_query)

            return {
                "status": True,
                "message": "Accountant updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
