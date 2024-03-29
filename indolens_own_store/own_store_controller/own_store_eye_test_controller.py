import datetime

import json
import re

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_own_store.own_store_controller import lens_sale_power_attribute_controller
from indolens_own_store.own_store_model.response_model.eye_test_resp_model import get_eye_test_resp
from indolens_own_store.own_store_model.response_model.store_expense_resp_model import get_store_expenses

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def add_eye_test(customerData, created_by, store_id):
    try:
        with connection.cursor() as cursor:
            create_update_customer = f"""INSERT INTO `customers`(`name`, `gender`, `age`, `phone`, `email`,
                                                `language`, `city`, `address`, `created_by_employee_id`,
                                                `created_by_store_id`, `created_by_store_type`, `created_on`,
                                                `updated_by_employee_id`, `updated_by_store_id`, `updated_by_store_type`,
                                                `updated_on`)
                                                VALUES ('{customerData.get('customer_name')}','{customerData.get('customer_gender')}',
                                                '{customerData.get('customer_age')}','{customerData.get('customer_phone')}',
                                                '{customerData.get('customer_email')}','{customerData.get('customer_language')}',
                                                '{customerData.get('customer_city')}','{customerData.get('customer_address')}',
                                                {created_by},{store_id}, 1, '{getIndianTime()}',{created_by},{store_id},'1', 
                                                '{getIndianTime()}')
                                                ON DUPLICATE KEY UPDATE 
                                                `name` = '{customerData.get('customer_name')}', 
                                                `gender` = '{customerData.get('customer_gender')}', 
                                                `age` = '{customerData.get('customer_age')}', 
                                                `email` = '{customerData.get('customer_email')}', 
                                                `language` = '{customerData.get('customer_language')}', 
                                                `city` = '{customerData.get('customer_city')}', 
                                                `address` = '{customerData.get('customer_address')}', 
                                                `updated_by_employee_id` = {created_by}, 
                                                `updated_by_store_id` = {store_id}, 
                                                `updated_by_store_type` = 1, 
                                                `updated_on` = '{getIndianTime()}' """
            cursor.execute(create_update_customer)
            customer_id = cursor.lastrowid

            power_attributes = lens_sale_power_attribute_controller.get_eye_test_power_attribute(customerData)

            add_eye_test_query = f""" INSERT INTO eye_test (customer_id, power_attributes, 
            created_by_store_id, created_by_store_type, created_by, created_on, updated_by, updated_on)
            VALUES({customer_id}, '{json.dumps(power_attributes)}', {store_id},1, {customerData.get('optometry_id')}, '{getIndianTime()}', {customerData.get('optometry_id')}, '{getIndianTime()}')"""
            cursor.execute(add_eye_test_query)
            test_id = cursor.lastrowid

            subject = email_template_controller.get_customer_eye_test_email_subject(customerData.get('customer_name'))
            body = email_template_controller.get_customer_eye_test_email_body(customerData.get('customer_name'), test_id)
            send_notification_controller.send_email(subject, body, customerData.get('customer_email'))

            return {
                "status": True,
                "message": "success"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


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
            get_eye_test_by_id_query = f""" SELECT et.*, c.name, c.phone, 
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
                                            WHERE et.eye_test_id = {testId}
                                             """
            cursor.execute(get_eye_test_by_id_query)
            eye_test = cursor.fetchall()
            return {
                "status": True,
                "eye_test": get_eye_test_resp(eye_test)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
