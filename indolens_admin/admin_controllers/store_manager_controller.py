import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.store_manager_resp_model import get_store_managers

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_store_manager(sub_admin, files):
    try:
        with connection.cursor() as cursor:
            insert_store_manager_query = f"""
                INSERT INTO store_manager (
                    name, email, phone, password, profile_pic, 
                    assigned_store_id, address, document_1_type, document_1_url, 
                    document_2_type, document_2_url, status, created_by, created_on, 
                    last_updated_by, last_updated_on
                ) VALUES (
                    '{sub_admin.name}', '{sub_admin.email}', '{sub_admin.phone}', '{sub_admin.password}', '{sub_admin.profile_pic}', 
                    '{sub_admin.assigned_store_id}', '{sub_admin.address}', '{sub_admin.document_1_type}', '{files.document1}', 
                    '{sub_admin.document_2_type}', '{files.document2}', 1, '{sub_admin.created_by}', '{today}', 
                    '{sub_admin.last_updated_by}', '{today}'
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_store_manager_query)
            return {
                "status": True,
                "message": "sub admin added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_store_manager():
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM store_manager AS sm
                                            LEFT JOIN own_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id """
            cursor.execute(get_store_manager_query)
            store_managers = cursor.fetchall()
            return {
                "status": True,
                "store_managers": get_store_managers(store_managers)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_store_manager_by_id(mid):
    try:
        with connection.cursor() as cursor:
            get_store_manager_query = f""" SELECT sm.*, os.store_name, creator.name, updater.name FROM store_manager AS sm
                                            LEFT JOIN own_store AS os ON sm.assigned_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON sm.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON sm.last_updated_by = updater.admin_id 
                                            WHERE sm.store_manager_id = '{mid}'"""
            cursor.execute(get_store_manager_query)
            store_manager = cursor.fetchall()
            return {
                "status": True,
                "store_manager": get_store_managers(store_manager)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301