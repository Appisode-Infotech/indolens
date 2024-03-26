import datetime
import json
import os

import pymysql
import pytz
from indolens.db_connection import connection


ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def delete_document(documenturl, document_type, table, condition, user_id, updated_by):
    try:
        parts = documenturl.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        file_path = os.path.join("media", folder_name, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            with connection.cursor() as cursor:
                get_documents_query = f"""
                SELECT {document_type} FROM {table} WHERE {condition} = {user_id} """
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[0])
                documents.remove(documenturl)
                cursor.execute(f""" UPDATE {table} SET {document_type} = '{json.dumps(documents)}', 
                last_updated_on = '{getIndianTime()}', last_updated_by = {updated_by} WHERE {condition} = {user_id} """)
                get_role = f""" SELECT role from {table} Where {condition} = {user_id}"""
                cursor.execute(get_role)
                role = cursor.fetchone()
            return {
                "status": True,
                "role": role[0],
                "message": "Document Deleted Successfully"
            }, 200
        else:
            with connection.cursor() as cursor:
                get_role = f""" SELECT role from {table} Where {condition} = {user_id}"""
                cursor.execute(get_role)
                role = cursor.fetchone()
            return {
                "status": False,
                "role": role[0],
                "message": f"Document Doesn't Exist"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def delete_product_image(imageURL, productId):
    try:
        parts = imageURL.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        file_path = os.path.join("media", folder_name, file_name)

        if os.path.exists(file_path):
            print("file found")
            os.remove(file_path)
            print("file deletd")
            with connection.cursor() as cursor:
                get_documents_query = f"""
                SELECT product_images FROM central_inventory Where product_id = {productId}
                """
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[0])
                documents.remove(imageURL)
                cursor.execute(f""" UPDATE central_inventory SET product_images = '{json.dumps(documents)}' WHERE product_id = {productId}""")
            return {
                "status": True,
                "message": "Document Deleted Successfully"
            }
        else:
            return {
                "status": False,
                "message": f"{file_name} Document Doesn't Exist"
            }

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301