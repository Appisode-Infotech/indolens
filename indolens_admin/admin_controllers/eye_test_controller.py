import datetime
import json

import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_models.admin_resp_model.eye_test_print_resp_model import get_eye_test_print_resp
from indolens_own_store.own_store_model.response_model.eye_test_resp_model import get_eye_test_resp

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today
def get_eye_test():
    try:
        with getConnection().cursor() as cursor:
            get_eye_test_query = f""" SELECT et.*, c.customer_name, c.customer_phone, 
                                            CASE 
                                                WHEN et.et_created_by_store_type = 1 THEN creator_os.ose_name 
                                                ELSE creator_fs.fse_name 
                                            END AS creator_name,
                                            CASE 
                                                WHEN et.et_created_by_store_type = 1 THEN updater_os.ose_name 
                                                ELSE updater_fs.fse_name 
                                            END AS updater_name 
                                            FROM eye_test as et
                                            LEFT JOIN customers AS c ON et.et_customer_id = c.customer_customer_id
                                            LEFT JOIN own_store_employees creator_os ON et.et_created_by = creator_os.ose_employee_id AND et.et_created_by_store_type = 1
                                            LEFT JOIN franchise_store_employees creator_fs ON et.et_created_by = creator_fs.fse_employee_id AND et.et_created_by_store_type = 2
                                            LEFT JOIN own_store_employees updater_os ON et.et_updated_by = updater_os.ose_employee_id AND et.et_created_by_store_type = 1
                                            LEFT JOIN franchise_store_employees updater_fs ON et.et_updated_by = updater_fs.fse_employee_id AND et.et_created_by_store_type = 2
                                            ORDER BY et.et_eye_test_id DESC
                                             """
            cursor.execute(get_eye_test_query)
            eye_test = cursor.fetchall()
            return {
                "status": True,
                "eye_test_list": eye_test
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_eye_test_by_id(testId):
    try:
        with getConnection().cursor() as cursor:
            get_eye_test_query = f""" SELECT et.*, c.customer_name, c.customer_phone,c.customer_age, 
                                                                    CASE 
                                                                        WHEN et.et_created_by_store_type = 1 THEN creator_os.ose_name 
                                                                        ELSE creator_fs.fse_name 
                                                                    END AS creator_name,
                                                                    CASE 
                                                                        WHEN et.et_created_by_store_type = 1 THEN updater_os.ose_name 
                                                                        ELSE updater_fs.fse_name 
                                                                    END AS updater_name,
                                                                    CASE
                                                                        WHEN et.et_created_by_store_type = 1 THEN os.os_store_name
                                                                        ELSE fs.fs_store_name
                                                                    END AS store_name,
                                                                    CASE
                                                                        WHEN et.et_created_by_store_type = 1 THEN os.os_store_phone
                                                                        ELSE fs.fs_store_phone
                                                                    END AS store_phone,
                                                                    CASE
                                                                        WHEN et.et_created_by_store_type = 1 THEN os.os_store_address
                                                                        ELSE fs.fs_store_address
                                                                    END AS store_address
                                                                    FROM eye_test as et
                                                                    LEFT JOIN own_store os ON et.et_created_by_store_id = os.os_store_id AND et.et_created_by_store_type = 1
                                                                    LEFT JOIN franchise_store fs ON et.et_created_by_store_id = fs.fs_store_id AND et.et_created_by_store_type = 2
                                                                    LEFT JOIN customers AS c ON et.et_customer_id = c.customer_customer_id
                                                                    LEFT JOIN own_store_employees creator_os ON et.et_created_by = creator_os.ose_employee_id AND et.et_created_by_store_type = 1
                                                                    LEFT JOIN franchise_store_employees creator_fs ON et.et_created_by = creator_fs.fse_employee_id AND et.et_created_by_store_type = 2
                                                                    LEFT JOIN own_store_employees updater_os ON et.et_updated_by = updater_os.ose_employee_id AND et.et_created_by_store_type = 1
                                                                    LEFT JOIN franchise_store_employees updater_fs ON et.et_updated_by = updater_fs.fse_employee_id AND et.et_created_by_store_type = 2
                                                                    WHERE et.et_eye_test_id = {testId}
                                                                     """
            cursor.execute(get_eye_test_query)
            eye_test = cursor.fetchone()
            eye_test['et_power_attributes'] = json.loads(eye_test['et_power_attributes']) if eye_test['et_power_attributes'] else []

            return {
                "status": True,
                "eye_test": eye_test
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
