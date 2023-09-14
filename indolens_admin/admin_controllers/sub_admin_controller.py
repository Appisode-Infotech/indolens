import json

import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.sub_admin_resp_model import get_sub_admin

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_sub_admin(sub_admin, files):
    try:
        with connection.cursor() as cursor:
            insert_admin_query = f"""
                INSERT INTO admin (
                    name, email, phone, password, role, profile_pic, 
                    address, document_1_type, document_1_url, document_2_type, document_2_url, 
                    status, created_by, created_on, last_updated_by, last_updated_on
                ) VALUES (
                    '{sub_admin.full_name}', '{sub_admin.email}', '{sub_admin.phone}', '{sub_admin.password}', 2, 
                    '{files.profile_pic}', '{sub_admin.complete_address}', '{sub_admin.document_1_type}', 
                    '{json.dumps(files.document1)}', '{sub_admin.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{sub_admin.created_by}', '{today}', '{sub_admin.last_updated_by}', '{today}'
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_admin_query)

            return {
                "status": True,
                "message": "sub admin added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_sub_admin():
    try:
        with connection.cursor() as cursor:
            get_all_sub_admin_query = f""" SELECT a.*, creator.name, updater.name 
                                            FROM admin AS a
                                            LEFT JOIN admin AS creator ON a.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON a.last_updated_by = updater.admin_id
                                            WHERE a.role = 2"""
            cursor.execute(get_all_sub_admin_query)
            sub_admins = cursor.fetchall()
            return {
                "status": True,
                "sub_admins": get_sub_admin(sub_admins)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_sub_admin_by_id(said):
    try:
        with connection.cursor() as cursor:
            get_all_sub_admin_query = f""" SELECT a.*, creator.name, updater.name 
                                            FROM admin AS a
                                            LEFT JOIN admin AS creator ON a.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON a.last_updated_by = updater.admin_id
                                            WHERE a.role = 2 and a.admin_id = '{said}'"""
            cursor.execute(get_all_sub_admin_query)
            sub_admins = cursor.fetchall()
            return {
                "status": True,
                "sub_admin": get_sub_admin(sub_admins)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_sub_admin(sub_admin):
    try:
        with connection.cursor() as cursor:
            update_admin_query = f"""
                UPDATE admin
                SET
                    name = '{sub_admin.full_name}',
                    email = '{sub_admin.email}',
                    phone = '{sub_admin.phone}',
                    password = '{sub_admin.password}',
                    profile_pic = '{sub_admin.profile_pic}',
                    address = '{sub_admin.complete_address}',
                    document_1_type = '{sub_admin.document_1_type}',
                    document_1_url = '{sub_admin.document1}',
                    document_2_type = '{sub_admin.document_2_type}',
                    document_2_url = '{sub_admin.document2}',
                    status = 1,
                    last_updated_by = '{sub_admin.last_updated_by}',
                    last_updated_on = '{today}'
                WHERE
                    admin_id = {sub_admin.admin_id}
            """

            # Execute the update query using your cursor
            cursor.execute(update_admin_query)

            return {
                "status": True,
                "message": "sub admin updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
