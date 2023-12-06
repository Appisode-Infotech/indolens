import datetime
import json
import os

import pymysql
import pytz
from django.db import connection


ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def delete_document(documenturl, document_type, table, condition, user_id):
    try:
        parts = documenturl.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        file_path = os.path.join("media", folder_name, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            with connection.cursor() as cursor:
                get_documents_query = f"""
                SELECT {document_type} FROM {table} Where {condition} = {user_id}
                """
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[0])
                documents.remove(documenturl)
                cursor.execute(f""" UPDATE {table} SET {document_type} = {json.dumps(documents)} WHERE {condition} = {user_id}""")
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


def delete_product_image(imageURL, productId):
    try:
        parts = imageURL.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        file_path = os.path.join("media", folder_name, file_name)
        print(folder_name)
        print(file_name)
        print(file_path)

        if os.path.exists(file_path):
            print("file found")
            # os.remove(file_path)
            # print("deleted file")
            # with connection.cursor() as cursor:
            #     get_documents_query = f"""
            #     SELECT product_images FROM central_inventory Where product_id = {productId}
            #     """
            #     cursor.execute(get_documents_query)
            #     documents = json.loads(cursor.fetchone()[0])
            #     documents.remove(imageURL)
            #     print("updated document")
            #     print(documents)
            #     cursor.execute(f""" UPDATE central_inventory SET product_images = {json.dumps(documents)} WHERE product_id = {productId}""")
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