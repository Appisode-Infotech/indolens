import datetime
import time
import json
import re

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_own_store.own_store_controller import lens_sale_power_attribute_controller
from indolens_own_store.own_store_model.response_model.store_expense_resp_model import get_store_expenses

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def convert_to_db_date_format(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    return date_obj.date()


def get_current_epoch_time():
    epoch_time = int(time.time())
    return epoch_time


def create_store_expense(expense_obj):
    try:
        with connection.cursor() as cursor:
            insert_expense_obj_query = f"""
                            INSERT INTO store_expense (
                                store_id, store_type, expense_amount, expense_reason, expense_date, created_on, created_by
                            ) VALUES ( 
                                '{expense_obj.store_id}', '{expense_obj.store_type}', '{expense_obj.expense_amount}', 
                                '{expense_obj.expense_reason}', '{getIndianTime()}', '{getIndianTime()}', '{expense_obj.created_by}') """

            cursor.execute(insert_expense_obj_query)
            return {
                "status": True,
                "message": f"Expense of amount:{expense_obj.expense_amount} added successfully for {expense_obj.expense_reason}"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_store_expense(store_id, store_type):
    try:
        with connection.cursor() as cursor:
            get_expense_obj_query = f""" SELECT se.*, creator.name FROM store_expense AS se
                                            LEFT JOIN own_store_employees AS creator ON se.created_by = creator.employee_id
                                            WHERE se.store_id = {store_id} AND se.store_type= {store_type}
                                            ORDER BY se.store_expense_id DESC"""
            cursor.execute(get_expense_obj_query)
            store_expense_data = cursor.fetchall()
            return {
                "status": True,
                "message": "success",
                "stor_expense_list": get_store_expenses(store_expense_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def make_sale(cart_data, customerData, billingDetailsData, employee_id, store_id, order_id):
    try:
        with connection.cursor() as cursor:
            create_update_customer = f"""INSERT INTO `customers`(`name`, `gender`, `age`, `phone`, `email`,
                                                `language`, `city`, `address`, `created_by_employee_id`,
                                                `created_by_store_id`, `created_by_store_type`, `created_on`,
                                                `updated_by_employee_id`, `updated_by_store_id`, `updated_by_store_type`,
                                                `updated_on`)
                                                VALUES ('{customerData.get('name')}','{customerData.get('gender')}',
                                                '{customerData.get('age')}','{customerData.get('phone')}',
                                                '{customerData.get('email')}','{customerData.get('language')}',
                                                '{customerData.get('city')}','{customerData.get('address')}',
                                                {billingDetailsData.get('orderByEmployee')},{store_id}, 1, '{getIndianTime()}',
                                                {billingDetailsData.get('orderByEmployee')},{store_id},'1', 
                                                '{getIndianTime()}')
                                                ON DUPLICATE KEY UPDATE 
                                                `name` = '{customerData.get('name')}', 
                                                `gender` = '{customerData.get('gender')}', 
                                                `age` = '{customerData.get('age')}', 
                                                `email` = '{customerData.get('email')}', 
                                                `language` = '{customerData.get('language')}', 
                                                `city` = '{customerData.get('city')}', 
                                                `address` = '{customerData.get('address')}', 
                                                `updated_by_employee_id` = {billingDetailsData.get('orderByEmployee')}, 
                                                `updated_by_store_id` = {store_id}, 
                                                `updated_by_store_type` = 1, 
                                                `updated_on` = '{getIndianTime()}' """
            cursor.execute(create_update_customer)
            customer_id = cursor.lastrowid

            if billingDetailsData.get('amount_paid') != '0':
                order_payment_track_query = f"""INSERT INTO sales_order_payment_track (order_id, payment_amount, 
                                                    payment_mode, payment_type, created_by_store, created_by_store_type, 
                                                    created_by_id, created_on )
                                                    VALUES ('{order_id}', {billingDetailsData.get('amount_paid')},
                                                    {billingDetailsData.get('paymentMode')}, 1, {store_id}, 1,
                                                    {billingDetailsData.get('orderByEmployee')}, '{getIndianTime()}')
                                                     """
                cursor.execute(order_payment_track_query)

            for data in cart_data:
                new_data = {re.sub(r'\[\d+\]', '', key): value for key, value in data.items()}
                if new_data.get('product_category_id') == '2':
                    discount_percentage = new_data.get('discount_percentage')
                    linked_items = [int(x) for x in new_data.get('linkedFrameIds', [])]

                    power_attributes = lens_sale_power_attribute_controller.get_power_attribute(new_data)
                    discount_checked = new_data.get('discount_checked')
                    is_discount_applied = 1 if discount_checked and discount_checked.lower() == 'on' else 0
                    if discount_percentage == "" or is_discount_applied == 0 or None:
                        discount_percentage = 0

                    insert_len_sales_query = f""" INSERT INTO `sales_order`
                                            (`order_id`, `product_id`, `hsn`, `unit_sale_price`, `unit_type`,
                                            `purchase_quantity`, `product_total_cost`, `discount_percentage`,
                                            `is_discount_applied`, `power_attribute`, `assigned_lab`, `customer_id`,
                                            `order_status`, `payment_status`, `delivery_status`, `payment_mode`,
                                            `amount_paid`, `estimated_delivery_date`, `created_by_store`,
                                            `created_by`, `created_on`, `updated_by`, `updated_on`, 
                                            `created_by_store_type`, sales_note, linked_item)
                                            VALUES
                                            ('{order_id}', {new_data.get('product')}, 
                                            '{new_data.get('product_hsn')}', 
                                            {new_data.get('unit_price')}, '{new_data.get('unit_type')}', 
                                            {new_data.get('purchase_qty')}, {new_data.get('product_total')}, 
                                            {discount_percentage}, {is_discount_applied}, 
                                            '{json.dumps(power_attributes)}', {billingDetailsData.get('assignedLab')}, 
                                            {customer_id}, 1, 1, 1, 1, {billingDetailsData.get('amount_paid')}, %s, 
                                            {store_id}, {billingDetailsData.get('orderByEmployee')}, 
                                            '{getIndianTime()}', {billingDetailsData.get('orderByEmployee')}, 
                                            '{getIndianTime()}', 1, '{billingDetailsData.get('saleNote')}', 
                                            '{json.dumps(linked_items)}') """

                    cursor.execute(insert_len_sales_query,
                                   (convert_to_db_date_format(billingDetailsData.get('estDeliveryDate'))))

                    update_central_Inventory = f"""UPDATE central_inventory SET product_quantity = product_quantity - {new_data.get('purchase_qty')}
                                                                                                WHERE product_id = {new_data.get('product')}"""
                    cursor.execute(update_central_Inventory)

                elif new_data.get('product_category_id') == '3':
                    discount_percentage = new_data.get('discount_percentage')
                    power_attributes = lens_sale_power_attribute_controller.get_power_attribute(new_data)
                    discount_checked = new_data.get('discount_checked')
                    is_discount_applied = 1 if discount_checked and discount_checked.lower() == 'on' else 0
                    if discount_percentage == "" or is_discount_applied == 0 or None:
                        discount_percentage = 0
                    insert_contact_len_sales_query = f""" INSERT INTO `sales_order`
                                                                (`order_id`, `product_id`, `hsn`, `unit_sale_price`, `unit_type`,
                                                                `purchase_quantity`, `product_total_cost`, `discount_percentage`,
                                                                `is_discount_applied`, `power_attribute`, `assigned_lab`, `customer_id`,
                                                                `order_status`, `payment_status`, `delivery_status`, `payment_mode`,
                                                                `amount_paid`, `estimated_delivery_date`, `created_by_store`,
                                                                `created_by`, `created_on`, `updated_by`, `updated_on`, 
                                                                `created_by_store_type`, `sales_note`)
                                                                VALUES
                                                                ('{order_id}', 
                                                                {new_data.get('product')}, '{new_data.get('product_hsn')}', 
                                                                '{new_data.get('unit_price')}', '{new_data.get('unit_type')}', 
                                                                {new_data.get('purchase_qty')}, {new_data.get('product_total')}, 
                                                                {discount_percentage}, {is_discount_applied}, 
                                                                '{json.dumps(power_attributes)}', {billingDetailsData.get('assignedLab')}, 
                                                                {customer_id}, 
                                                                1, 1, 1, 1, {billingDetailsData.get('amount_paid')}, %s, 
                                                                {store_id}, {billingDetailsData.get('orderByEmployee')}, 
                                                                '{getIndianTime()}', 
                                                                {billingDetailsData.get('orderByEmployee')}, 
                                                                '{getIndianTime()}', 1, '{billingDetailsData.get('saleNote')}') """
                    cursor.execute(insert_contact_len_sales_query,
                                   (convert_to_db_date_format(billingDetailsData.get('estDeliveryDate'))))

                    update_central_Inventory = f"""UPDATE central_inventory
                                                SET product_quantity = product_quantity - {new_data.get('purchase_qty')}
                                                WHERE product_id = {new_data.get('product')}"""
                    cursor.execute(update_central_Inventory)
                else:
                    discount_percentage = new_data.get('discount_percentage')
                    discount_checked = new_data.get('discount_checked')
                    is_discount_applied = 1 if discount_checked and discount_checked.lower() == 'on' else 0
                    if discount_percentage == "" or is_discount_applied == 0 or None:
                        discount_percentage = 0
                    power_attributes = {}
                    insert_contact_len_sales_query = f"""
                                                            INSERT INTO `sales_order`
                                                            (`order_id`, `product_id`, `hsn`, `unit_sale_price`, `unit_type`,
                                                            `purchase_quantity`, `product_total_cost`, `discount_percentage`,
                                                            `is_discount_applied`, `assigned_lab`, `customer_id`,
                                                            `order_status`, `payment_status`, `delivery_status`, `payment_mode`,
                                                            `amount_paid`, `estimated_delivery_date`, `created_by_store`,
                                                            `created_by`, `created_on`, `updated_by`, `updated_on`, 
                                                            `power_attribute`, `created_by_store_type`, `sales_note`)
                                                            VALUES
                                                            ('{order_id}', {new_data.get('product')}, '{new_data.get('product_hsn')}', 
                                                            {new_data.get('unit_price')}, '{new_data.get('unit_type')}', 
                                                            {new_data.get('purchase_qty')}, {new_data.get('product_total')}, 
                                                            {discount_percentage}, {is_discount_applied}, 
                                                            {billingDetailsData.get('assignedLab')}, {customer_id}, 1, 
                                                            1, 1, 1, {billingDetailsData.get('amount_paid')}, %s, 
                                                            {store_id}, {billingDetailsData.get('orderByEmployee')}, 
                                                            '{getIndianTime()}', {billingDetailsData.get('orderByEmployee')}, 
                                                            '{getIndianTime()}', '{power_attributes}', 1 , 
                                                            '{billingDetailsData.get('saleNote')}')
                                                        """

                    cursor.execute(insert_contact_len_sales_query,
                                   (convert_to_db_date_format(billingDetailsData.get('estDeliveryDate'))))
                    update_central_Inventory = f"""UPDATE store_inventory SET
                     product_quantity = product_quantity - {new_data.get('purchase_qty')}
                                          WHERE product_id = {new_data.get('product')} AND
                                                store_id = {store_id} AND store_type = 1"""
                    cursor.execute(update_central_Inventory)

            add_order_track_query = f""" 
                                        INSERT INTO order_track (order_id, status, created_on) 
                                        VALUES ('{order_id}', 1, '{getIndianTime()}' ) """
            cursor.execute(add_order_track_query)

            subject = email_template_controller.get_order_creation_email_subject(order_id)
            body = email_template_controller.get_order_placed_email_body(customerData.get('name'),
                                                                         order_id, getIndianTime(),
                                                                         convert_to_db_date_format(
                                                                             billingDetailsData.get('estDeliveryDate')))
            response = send_notification_controller.send_email(subject, body, customerData.get('email'))
            print("email response")
            print(response)

            return {
                "status": True,
                "message": "success",
                "order_id": order_id
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
