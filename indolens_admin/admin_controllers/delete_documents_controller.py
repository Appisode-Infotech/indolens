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

