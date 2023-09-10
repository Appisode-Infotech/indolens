import pymysql
from django.db import connection
import datetime
import pytz

from indolens_admin.admin_models.admin_resp_model.franchise_owner_resp_model import get_franchise_owners

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_franchise_owner(franchise_owner, files):
    try:
        with connection.cursor() as cursor:
            insert_franchise_owner_query = f"""
                INSERT INTO franchise_owner (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, document_2_type, document_2_url, 
                    status, created_by, created_on, last_updated_by, last_updated_on
                ) VALUES (
                    '{franchise_owner.full_name}', '{franchise_owner.email}', '{franchise_owner.phone}', '{franchise_owner.password}',
                    '{files.profile_pic}', '{franchise_owner.complete_address}', '{franchise_owner.document_1_type}', 
                    '{files.document1}', '{franchise_owner.document_2_type}', '{files.document2}', 
                    1, '{franchise_owner.created_by}', '{today}', '{franchise_owner.last_updated_by}', '{today}'
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_franchise_owner_query)
            foid = cursor.lastrowid

            return {
                "status": True,
                "message": "franchise owner added",
                "foid": foid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_franchise_owner():
    try:
        with connection.cursor() as cursor:
            get_all_franchise_owner_query = f""" SELECT a.*, os.store_name, creator.name, updater.name 
                                            FROM franchise_owner AS a
                                            LEFT JOIN franchise_store AS os ON a.franchise_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON a.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON a.last_updated_by = updater.admin_id """
            cursor.execute(get_all_franchise_owner_query)
            franchise_owners = cursor.fetchall()
            print(franchise_owners)
            return {
                "status": True,
                "franchise_owners": get_franchise_owners(franchise_owners)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_owner_by_id(foid):
    try:
        with connection.cursor() as cursor:
            get_all_franchise_owner_query = f""" SELECT a.*, os.store_name, creator.name, updater.name 
                                            FROM franchise_owner AS a
                                            LEFT JOIN franchise_store AS os ON a.franchise_store_id = os.store_id
                                            LEFT JOIN admin AS creator ON a.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON a.last_updated_by = updater.admin_id
                                             WHERE franchise_owner_id = '{foid}'"""
            cursor.execute(get_all_franchise_owner_query)
            franchise_owners = cursor.fetchall()
            return {
                "status": True,
                "franchise_owner": get_franchise_owners(franchise_owners)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_franchise_owner(franchise_owner):
    try:
        with connection.cursor() as cursor:
            update_franchise_owners_query = f"""
                UPDATE franchise_owner
                SET
                    name = '{franchise_owner.full_name}',
                    email = '{franchise_owner.email}',
                    phone = '{franchise_owner.phone}',
                    password = '{franchise_owner.password}',
                    profile_pic = '{franchise_owner.profile_pic}',
                    address = '{franchise_owner.complete_address}',
                    document_1_type = '{franchise_owner.document_1_type}',
                    document_1_url = '{franchise_owner.document1}',
                    document_2_type = '{franchise_owner.document_2_type}',
                    document_2_url = '{franchise_owner.document2}',
                    status = 1,
                    last_updated_by = '{franchise_owner.last_updated_by}',
                    last_updated_on = '{today}'
                WHERE
                    franchise_owner_id = {franchise_owner.franchise_owner_id}
            """

            # Execute the update query using your cursor
            cursor.execute(update_franchise_owners_query)

            return {
                "status": True,
                "message": "franchise owner updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
