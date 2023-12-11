import datetime
import json
import os

import pymysql
import pytz
from django.db import connection


ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def add_document(documenturl, document_type, table, condition, user_id):
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


def add_products_image(new_images, productId):
    try:
        with connection.cursor() as cursor:
            get_documents_query = f"""
            SELECT product_images FROM central_inventory Where product_id = {productId}
            """
            cursor.execute(get_documents_query)
            old_images = json.loads(cursor.fetchone()[0])
            product_image = old_images+new_images.product_img
            cursor.execute(
                f""" UPDATE central_inventory SET product_images = '{json.dumps(product_image)}' WHERE product_id = {productId}""")
        return {
            "status": True,
            "message": "Document Deleted Successfully"
        }

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def add_own_store_employee_image(file_data, employeeId, emp_obj):
    try:
        with connection.cursor() as cursor:
            get_document1_query = f"""
                        SELECT document_1_url FROM own_store_employees Where employee_id = {employeeId}
                        """
            cursor.execute(get_document1_query)
            old_images = json.loads(cursor.fetchone()[0])
            document1 = old_images + file_data.document1

            cursor.execute(
                f""" UPDATE own_store_employees SET document_1_url = '{json.dumps(document1)}', 
                document_1_type = '{emp_obj.document_1_type}' WHERE employee_id = {employeeId}""")

            get_document2_query = f"""
                        SELECT document_2_url FROM own_store_employees Where employee_id = {employeeId}
                        """
            cursor.execute(get_document2_query)
            old_images = json.loads(cursor.fetchone()[0])
            document2 = old_images + file_data.document2
            cursor.execute(
                f""" UPDATE own_store_employees SET document_2_url = '{json.dumps(document2)}', 
                document_2_type = '{emp_obj.document_2_type}' WHERE employee_id = {employeeId}""")

            get_role = f""" SELECT role from own_store_employees Where employee_id = {employeeId}"""
            cursor.execute(get_role)
            role = cursor.fetchone()

        return {
            "status": True,
            "role": role[0],
            "message": "Document Inserted Successfully"
        }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def add_franchise_store_employee_image(file_data, employeeId, emp_obj):
    try:
        with connection.cursor() as cursor:
            get_document1_query = f"""
                        SELECT document_1_url FROM franchise_store_employees Where employee_id = {employeeId}
                        """
            cursor.execute(get_document1_query)
            old_images = json.loads(cursor.fetchone()[0])
            document1 = old_images + file_data.document1

            cursor.execute(
                f""" UPDATE franchise_store_employees SET document_1_url = '{json.dumps(document1)}', 
                document_1_type = '{emp_obj.document_1_type}' WHERE employee_id = {employeeId}""")

            get_document2_query = f"""
                        SELECT document_2_url FROM franchise_store_employees Where employee_id = {employeeId}
                        """
            cursor.execute(get_document2_query)
            old_images = json.loads(cursor.fetchone()[0])
            document2 = old_images + file_data.document2
            cursor.execute(
                f""" UPDATE franchise_store_employees SET document_2_url = '{json.dumps(document2)}', 
                document_2_type = '{emp_obj.document_2_type}' WHERE employee_id = {employeeId}""")

            get_role = f""" SELECT role from franchise_store_employees Where employee_id = {employeeId}"""
            cursor.execute(get_role)
            role = cursor.fetchone()

        return {
            "status": True,
            "role": role[0],
            "message": "Document Inserted Successfully"
        }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301