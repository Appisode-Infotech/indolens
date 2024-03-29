import datetime
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.eye_test_print_resp_model import get_eye_test_print_resp
from indolens_own_store.own_store_model.response_model.eye_test_resp_model import get_eye_test_resp

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today
def get_eye_test():
    try:
        with connection.cursor() as cursor:
            get_eye_test_query = f""" SELECT et.*, c.name, c.phone, 
                                            CASE 
                                                WHEN et.created_by_store_type = 1 THEN creator_os.name 
                                                ELSE creator_fs.name 
                                            END AS creator_name,
                                            CASE 
                                                WHEN et.created_by_store_type = 1 THEN updater_os.name 
                                                ELSE updater_fs.name 
                                            END AS updater_name 
                                            FROM eye_test as et
                                            LEFT JOIN customers AS c ON et.customer_id = c.customer_id
                                            LEFT JOIN own_store_employees creator_os ON et.created_by = creator_os.employee_id AND et.created_by_store_type = 1
                                            LEFT JOIN franchise_store_employees creator_fs ON et.created_by = creator_fs.employee_id AND et.created_by_store_type = 2
                                            LEFT JOIN own_store_employees updater_os ON et.updated_by = updater_os.employee_id AND et.created_by_store_type = 1
                                            LEFT JOIN franchise_store_employees updater_fs ON et.updated_by = updater_fs.employee_id AND et.created_by_store_type = 2
                                            ORDER BY et.eye_test_id DESC
                                             """
            cursor.execute(get_eye_test_query)
            eye_test = cursor.fetchall()
            return {
                "status": True,
                "eye_test_list": get_eye_test_resp(eye_test)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_eye_test_by_id(testId):
    try:
        with connection.cursor() as cursor:
            get_eye_test_by_id_query = f""" SELECT et.*, c.name, c.phone, c.age, 
                                            CASE 
                                                WHEN et.created_by_store_type = 1 THEN creator_os.name 
                                                ELSE creator_fs.name 
                                            END AS creator_name,
                                            CASE 
                                                WHEN et.created_by_store_type = 1 THEN updater_os.name 
                                                ELSE updater_fs.name 
                                            END AS updater_name,
                                            CASE
                                                WHEN et.created_by_store_type = 1 THEN os.store_name
                                                WHEN et.created_by_store_type = 2 THEN fs.store_name
                                            END AS store_name,
                                            CASE
                                                WHEN et.created_by_store_type = 1 THEN os.store_address
                                                WHEN et.created_by_store_type = 2 THEN fs.store_address
                                            END AS store_address
                                            FROM eye_test as et
                                            LEFT JOIN own_store os ON et.created_by_store_id = os.store_id AND et.created_by_store_type = 1
                                            LEFT JOIN franchise_store fs ON et.created_by_store_id = fs.store_id AND et.created_by_store_type = 2
                                            LEFT JOIN customers AS c ON et.customer_id = c.customer_id
                                            LEFT JOIN own_store_employees creator_os ON et.created_by = creator_os.employee_id AND et.created_by_store_type = 1
                                            LEFT JOIN franchise_store_employees creator_fs ON et.created_by = creator_fs.employee_id AND et.created_by_store_type = 2
                                            LEFT JOIN own_store_employees updater_os ON et.updated_by = updater_os.employee_id AND et.created_by_store_type = 1
                                            LEFT JOIN franchise_store_employees updater_fs ON et.updated_by = updater_fs.employee_id AND et.created_by_store_type = 2
                                            WHERE et.eye_test_id = {testId}
                                             """
            cursor.execute(get_eye_test_by_id_query)
            eye_test = cursor.fetchall()
            return {
                "status": True,
                "eye_test": get_eye_test_print_resp(eye_test)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
