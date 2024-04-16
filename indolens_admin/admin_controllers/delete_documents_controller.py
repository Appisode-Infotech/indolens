import datetime
import json
import os

import pymysql
import pytz
from indolens.db_connection import getConnection

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
            with getConnection().cursor() as cursor:
                get_documents_query = f"""
                SELECT {document_type} FROM {table} WHERE {condition} = {user_id} """
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[document_type])
                print(documents)
                documents.remove(documenturl)
                print(documents)
                cursor.execute(f""" UPDATE {table} SET {document_type} = '{json.dumps(documents)}', 
                ose_last_updated_on = '{getIndianTime()}', ose_last_updated_by = {updated_by} WHERE {condition} = {user_id} """)

                get_role = f""" SELECT ose_role from {table} Where {condition} = {user_id}"""
                cursor.execute(get_role)
                role = cursor.fetchone()
                print(role)
            return {
                "status": True,
                "role": role['ose_role'],
                "message": "Document Deleted Successfully"
            }, 200
        else:
            with getConnection().cursor() as cursor:
                get_role = f""" SELECT ose_role from {table} Where {condition} = {user_id}"""
                cursor.execute(get_role)
                role = cursor.fetchone()
            return {
                "status": False,
                "role": role['ose_role'],
                "message": f"Document Doesn't Exist"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def delete_fse_document(documenturl, document_type, table, condition, user_id, updated_by):
    try:
        parts = documenturl.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        file_path = os.path.join("media", folder_name, file_name)
        print("==============================")
        print(file_path)

        if os.path.exists(file_path):
            os.remove(file_path)
            with getConnection().cursor() as cursor:
                get_documents_query = f"""
                SELECT {document_type} FROM {table} WHERE {condition} = {user_id} """
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[document_type])
                print(documents)
                documents.remove(documenturl)
                print(documents)
                cursor.execute(f""" UPDATE {table} SET {document_type} = '{json.dumps(documents)}', 
                fse_last_updated_on = '{getIndianTime()}', fse_last_updated_by = {updated_by} WHERE {condition} = {user_id} """)

                get_role = f""" SELECT fse_role from {table} Where {condition} = {user_id}"""
                cursor.execute(get_role)
                role = cursor.fetchone()
                print(role)
            return {
                "status": True,
                "role": role['fse_role'],
                "message": "Document Deleted Successfully"
            }, 200
        else:
            with getConnection().cursor() as cursor:
                get_role = f""" SELECT fse_role from {table} Where {condition} = {user_id}"""
                cursor.execute(get_role)
                role = cursor.fetchone()
            return {
                "status": False,
                "role": role['fse_role'],
                "message": f"Document Doesn't Exist"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def delete_admin_document(documenturl, document_type, table, condition, user_id, updated_by):
    try:
        parts = documenturl.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        file_path = os.path.join("media", folder_name, file_name)
        print("==============================")
        print(file_path)

        if os.path.exists(file_path):
            os.remove(file_path)
            with getConnection().cursor() as cursor:
                get_documents_query = f"""
                SELECT {document_type} FROM {table} WHERE {condition} = {user_id} """
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[document_type])
                print(documents)
                documents.remove(documenturl)
                print(documents)
                cursor.execute(f""" UPDATE {table} SET {document_type} = '{json.dumps(documents)}', 
                admin_last_updated_on = '{getIndianTime()}', admin_last_updated_by = {updated_by} WHERE {condition} = {user_id} """)

                get_role = f""" SELECT admin_role from {table} Where {condition} = {user_id}"""
                cursor.execute(get_role)
                role = cursor.fetchone()
                print(role)
            return {
                "status": True,
                "role": role['admin_role'],
                "message": "Document Deleted Successfully"
            }, 200
        else:
            with getConnection().cursor() as cursor:
                get_role = f""" SELECT admin_role from {table} Where {condition} = {user_id}"""
                cursor.execute(get_role)
                role = cursor.fetchone()
            return {
                "status": False,
                "role": role['admin_role'],
                "message": f"Document Doesn't Exist"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def delete_ah_document(documenturl, document_type, table, condition, user_id, updated_by):
    try:
        parts = documenturl.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        file_path = os.path.join("media", folder_name, file_name)
        print("==============================")
        print(file_path)

        if os.path.exists(file_path):
            os.remove(file_path)
            with getConnection().cursor() as cursor:
                get_documents_query = f"""
                SELECT {document_type} FROM {table} WHERE {condition} = {user_id} """
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[document_type])
                print(documents)
                documents.remove(documenturl)
                print(documents)
                cursor.execute(f""" UPDATE {table} SET {document_type} = '{json.dumps(documents)}', 
                ah_last_updated_on = '{getIndianTime()}', ah_last_updated_by = {updated_by} WHERE {condition} = {user_id} """)
            return {
                "status": True,
                "message": "Document Deleted Successfully"
            }, 200
        else:
            return {
                "status": False,
                "message": f"Document Doesn't Exist"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def delete_accountant_document(documenturl, document_type, table, condition, user_id, updated_by):
    try:
        parts = documenturl.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        file_path = os.path.join("media", folder_name, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            with getConnection().cursor() as cursor:
                get_documents_query = f"""
                SELECT {document_type} FROM {table} WHERE {condition} = {user_id} """
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[document_type])
                documents.remove(documenturl)
                cursor.execute(f""" UPDATE {table} SET {document_type} = '{json.dumps(documents)}', 
                ac_last_updated_on = '{getIndianTime()}', ac_last_updated_by = {updated_by} WHERE {condition} = {user_id} """)
            return {
                "status": True,
                "message": "Document Deleted Successfully"
            }, 200
        else:
            return {
                "status": False,
                "message": f"Document Doesn't Exist"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def delete_lt_document(documenturl, document_type, table, condition, user_id, updated_by):
    try:
        parts = documenturl.split('/')
        folder_name = parts[0]
        file_name = parts[-1]
        file_path = os.path.join("media", folder_name, file_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            with getConnection().cursor() as cursor:
                get_documents_query = f"""
                SELECT {document_type} FROM {table} WHERE {condition} = {user_id} """
                cursor.execute(get_documents_query)
                documents = json.loads(cursor.fetchone()[document_type])
                documents.remove(documenturl)
                cursor.execute(f""" UPDATE {table} SET {document_type} = '{json.dumps(documents)}', 
                lt_last_updated_on = '{getIndianTime()}', lt_last_updated_by = {updated_by} WHERE {condition} = {user_id} """)
            return {
                "status": True,
                "message": "Document Deleted Successfully"
            }, 200
        else:
            return {
                "status": False,
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
            with getConnection().cursor() as cursor:
                get_documents_query = f"""
                SELECT ci_product_images FROM central_inventory Where ci_product_id = {productId}
                """
                cursor.execute(get_documents_query)
                documents = cursor.fetchone()
                print(documents)
                print(json.loads(documents['ci_product_images']))
                documents = json.loads(documents['ci_product_images'])
                documents.remove(imageURL)
                print(documents)
                cursor.execute(
                    f""" UPDATE central_inventory SET ci_product_images = '{json.dumps(documents)}' WHERE ci_product_id = {productId}""")
            return {
                "status": True,
                "message": "Document Deleted Successfully"
            }, 200
        else:
            return {
                "status": False,
                "message": f"{file_name} Document Doesn't Exist"
            }, 400

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
