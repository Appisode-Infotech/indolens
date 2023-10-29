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
        print(documenturl)
        parts = documenturl.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        print(folder_name)
        print(file_name)
        file_path = os.path.join("media", folder_name, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_name} has been deleted.")
            with connection.cursor() as cursor:
                print("in the database connection")
                get_documents_query = f"""
                SELECT {document_type} FROM {table} Where {condition} = {user_id}
                """
                print(get_documents_query)
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[0])
                print(documents)
                documents.remove(documenturl)
                print(documents)
            return {
                "status": True,
                "message": "Document Deleted Successfully"
            }
        else:
            print(f"{file_name} does not exist.")
            return {
                "status": False,
                "message": "Document Doesn't Exist"
            }

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

