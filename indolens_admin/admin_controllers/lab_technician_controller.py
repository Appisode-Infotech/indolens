import datetime
import json

import bcrypt
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_models.admin_resp_model.lab_technician_resp_model import get_lab_technicians

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def create_lab_technician(lab_technician, files):
    try:
        hashed_password = bcrypt.hashpw(lab_technician.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with getConnection().cursor() as cursor:
            insert_marketing_head_query = f"""
                INSERT INTO lab_technician (
                    name, email, phone, password, profile_pic, 
                    address, document_1_type, document_1_url, document_2_type, document_2_url, 
                    status, created_by, created_on, last_updated_by, last_updated_on,assigned_lab_id 
                ) VALUES (
                    '{lab_technician.name}', '{lab_technician.email}', '{lab_technician.phone}', '{hashed_password}',
                    '{files.profile_pic}', '{lab_technician.address}', '{lab_technician.document_1_type}', 
                    '{json.dumps(files.document1)}', '{lab_technician.document_2_type}', '{json.dumps(files.document2)}', 
                    1, '{lab_technician.created_by}', '{getIndianTime()}', '{lab_technician.last_updated_by}', '{getIndianTime()}', 0
                )
            """

            # Execute the query using your cursor
            cursor.execute(insert_marketing_head_query)
            ltid = cursor.lastrowid

            subject = email_template_controller.get_lab_tech_creation_email_subject(lab_technician.name)
            body = email_template_controller.get_lab_tech_creation_email_body(lab_technician.name, 'Lab Technician',
                                                                              lab_technician.email,
                                                                              lab_technician.password)
            send_notification_controller.send_email(subject, body, lab_technician.email)

            return {
                "status": True,
                "message": "Lab Technician added",
                "ltid": ltid
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_lab_technician(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_lab_technician_query = f"""
            SELECT lt.*, creator.name, updater.name, l.lab_name
            FROM lab_technician AS lt
            LEFT JOIN lab AS l ON lt.assigned_lab_id = l.lab_id
            LEFT JOIN admin AS creator ON lt.created_by = creator.admin_id
            LEFT JOIN admin AS updater ON lt.last_updated_by = updater.admin_id
            WHERE lt.status {status_condition}
            GROUP BY lt.lab_technician_id ORDER BY lt.lab_technician_id DESC
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
        with getConnection().cursor() as cursor:
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
def edit_lab_technician(lab_tech_obj, files):
    try:
        with getConnection().cursor() as cursor:
            update_lab_tech_obj_query = f"""
                                UPDATE lab_technician
                                SET 
                                    name = '{lab_tech_obj.name}',
                                    email = '{lab_tech_obj.email}',
                                    phone = '{lab_tech_obj.phone}',
                                    {'profile_pic = ' + f"'{files.profile_pic}'," if files.profile_pic is not None else ''}
                                    address = '{lab_tech_obj.address}',
                                    last_updated_by = '{lab_tech_obj.last_updated_by}',
                                    last_updated_on = '{getIndianTime()}'
                                WHERE lab_technician_id = {lab_tech_obj.lab_technician_id}
                            """
            cursor.execute(update_lab_tech_obj_query)

            return {
                "status": True,
                "message": "Lab Technician updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_lab_technician(ltid, status):
    try:
        with getConnection().cursor() as cursor:
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


def assign_lab(labtechId, labId):
    try:
        with getConnection().cursor() as cursor:
            update_lab_technician_query = f"""
                UPDATE lab_technician
                SET
                    assigned_lab_id = {labId}
                WHERE
                    lab_technician_id = {labtechId}
            """
            # Execute the update query using your cursor
            cursor.execute(update_lab_technician_query)

            return {
                       "status": True,
                       "message": "Lab assigned"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def unassign_lab(labtechId, labId):
    try:
        with getConnection().cursor() as cursor:
            update_lab_technician_query = f"""
                UPDATE lab_technician
                SET
                    assigned_lab_id = 0
                WHERE
                    lab_technician_id = {labtechId}
            """
            # Execute the update query using your cursor
            cursor.execute(update_lab_technician_query)

            return {
                       "status": True,
                       "message": "Lab un assigned"
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
