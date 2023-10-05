import datetime
import json

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.sales_executive_resp_model import get_sales_executives

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_own_sales_executives(sales_executives, files):
    try:
        with connection.cursor() as cursor:
            insert_sales_executives_query = f"""
                INSERT INTO own_store_employees (
                   name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role
                ) VALUES (
                    '{sales_executives.name}', '{sales_executives.email}', '{sales_executives.phone}', '{sales_executives.password}',
                    '{files.profile_pic}', '{sales_executives.address}', '{sales_executives.document_1_type}', 
                    '{json.dumps(files.document1)}', '{sales_executives.document_2_type}', '{json.dumps(files.document2)}', 0,
                    '{sales_executives.created_by}', '{today}', '{sales_executives.last_updated_by}', '{today}', 3
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_sales_executives_query)
            seid = cursor.lastrowid

            return {
                "status": True,
                "message": "Sales Executives added",
                "seid": seid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def create_franchise_sales_executives(sales_executives, files):
    try:
        with connection.cursor() as cursor:
            insert_sales_executives_query = f"""
                INSERT INTO franchise_store_employees (
                   name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on, role
                ) VALUES (
                    '{sales_executives.name}', '{sales_executives.email}', '{sales_executives.phone}', '{sales_executives.password}',
                    '{files.profile_pic}', '{sales_executives.address}', '{sales_executives.document_1_type}', 
                    '{json.dumps(files.document1)}', '{sales_executives.document_2_type}', '{json.dumps(files.document2)}', 0,
                    '{sales_executives.created_by}', '{today}', '{sales_executives.last_updated_by}', '{today}', 3
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_sales_executives_query)
            seid = cursor.lastrowid

            return {
                "status": True,
                "message": "Sales Executives added",
                "seid": seid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_sales_executive():
    try:
        with connection.cursor() as cursor:
            get_sales_executive_query = f"""
            SELECT se.*, creator.name, updater.name, os.store_name
            FROM sales_executive AS se
            LEFT JOIN own_store AS os ON se.assigned_store_id = os.store_id
            LEFT JOIN admin AS creator ON se.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON se.last_updated_by = updater.admin_id
            GROUP BY se.sales_executive_id
            """
            cursor.execute(get_sales_executive_query)
            sales_executive = cursor.fetchall()
            print(sales_executive)

            return {
                "status": True,
                "sales_executive_list": get_sales_executives(sales_executive)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_sales_executive_by_id(seid):
    try:
        with connection.cursor() as cursor:
            get_sales_executive_query = f"""
            SELECT se.*, creator.name, updater.name, os.store_name
            FROM sales_executive AS se
            LEFT JOIN own_store AS os ON se.assigned_store_id = os.store_id
            LEFT JOIN admin AS creator ON se.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON se.last_updated_by = updater.admin_id
            WHERE sales_executive_id = '{seid}'
            GROUP BY se.sales_executive_id
            """
            cursor.execute(get_sales_executive_query)
            sales_executive = cursor.fetchall()
            print(sales_executive)

            return {
                "status": True,
                "sales_executive": get_sales_executives(sales_executive)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_sales_executive(seid, status):
    try:
        with connection.cursor() as cursor:
            update_marketing_head_query = f"""
                UPDATE sales_executive
                SET
                    status = {status}
                WHERE
                    sales_executive_id = {seid}
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
