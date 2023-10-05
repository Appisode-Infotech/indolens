import datetime
import json

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.lab_technician_resp_model import get_lab_technicians

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_lab_technician(lab_technician, files):
    try:
        with connection.cursor() as cursor:
            insert_marketing_head_query = f"""
                INSERT INTO lab_technician (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, document_2_type, document_2_url, 
                    status, created_by, created_on, last_updated_by, last_updated_on
                ) VALUES (
                    '{lab_technician.name}', '{lab_technician.email}', '{lab_technician.phone}', '{lab_technician.password}',
                    '{files.profile_pic}', '{lab_technician.address}', '{lab_technician.document_1_type}', 
                    '{json.dumps(files.document1)}', '{lab_technician.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{lab_technician.created_by}', '{today}', '{lab_technician.last_updated_by}', '{today}'
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_marketing_head_query)

            return {
                       "status": True,
                       "message": "Lab Technician added",
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_lab_technician():
    try:
        with connection.cursor() as cursor:
            get_lab_technician_query = f"""
            SELECT lt.*, creator.name, updater.name, l.lab_name
            FROM lab_technician AS lt
            LEFT JOIN lab AS l ON lt.assigned_lab_id = l.lab_id
            LEFT JOIN admin AS creator ON lt.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON lt.last_updated_by = updater.admin_id
            GROUP BY lt.lab_technician_id
            """
            cursor.execute(get_lab_technician_query)
            lab_technician = cursor.fetchall()

            return {
                       "status": True,
                       "lab_technician_list": get_lab_technicians(lab_technician)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_technician_by_id(ltid):
    try:
        with connection.cursor() as cursor:
            get_lab_technician_query = f"""
                        SELECT lt.*, creator.name, updater.name, l.lab_name
                        FROM lab_technician AS lt
                        LEFT JOIN lab AS l ON lt.assigned_lab_id = l.lab_id
                        LEFT JOIN admin AS creator ON lt.created_by = creator.admin_id
                        LEFT JOIN admin AS updater ON lt.last_updated_by = updater.admin_id
                        WHERE lt.lab_technician_id = {ltid}
                        GROUP BY lt.lab_technician_id
                        """
            cursor.execute(get_lab_technician_query)
            lab_technician = cursor.fetchall()
            return {
                       "status": True,
                       "lab_technician": get_lab_technicians(lab_technician)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_lab_technician(ltid, status):
    try:
        with connection.cursor() as cursor:
            update_lab_technician_query = f"""
                UPDATE lab_technician
                SET
                    status = {status}
                WHERE
                    lab_technician_id = {ltid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_lab_technician_query)

            return {
                       "status": True,
                       "message": "Lab Technician   updated"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
