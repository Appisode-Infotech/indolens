import datetime

import json
import re

import pymysql
import pytz
from django.db import connection

from indolens_own_store.own_store_controller import lens_sale_power_attribute_controller
from indolens_own_store.own_store_model.response_model.store_expense_resp_model import get_store_expenses

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def convert_to_db_date_format(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    return date_obj.date()


def create_store_expense(expense_obj):
    try:
        with connection.cursor() as cursor:
            insert_expense_obj_query = f"""
                            INSERT INTO store_expense (
                                store_id, store_type, expense_amount, expense_reason, expense_date, created_on, created_by
                            ) VALUES ( 
                                '{expense_obj.store_id}', '{expense_obj.store_type}', '{expense_obj.expense_amount}', 
                                '{expense_obj.expense_reason}', '{today}', '{today}', '{expense_obj.created_by}') """

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


def make_sale(cart_data, customerData, billingDetailsData, employee_id, store_id):
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
                                                {employee_id},{store_id}, 1, '{today}',{employee_id},{store_id},'1', 
                                                '{today}')
                                                ON DUPLICATE KEY UPDATE 
                                                `name` = '{customerData.get('name')}', 
                                                `gender` = '{customerData.get('gender')}', 
                                                `age` = '{customerData.get('age')}', 
                                                `email` = '{customerData.get('email')}', 
                                                `language` = '{customerData.get('language')}', 
                                                `city` = '{customerData.get('city')}', 
                                                `address` = '{customerData.get('address')}', 
                                                `updated_by_employee_id` = {employee_id}, 
                                                `updated_by_store_id` = {store_id}, 
                                                `updated_by_store_type` = 1, 
                                                `updated_on` = '{today}' """
            cursor.execute(create_update_customer)
            customer_id = cursor.lastrowid
            print(customer_id)

            for data in cart_data:
                new_data = {re.sub(r'\[\d+\]', '', key): value for key, value in data.items()}
                if new_data.get('product_category_id') == '2':
                    discount_percentage = new_data.get('discount_percentage')
                    if discount_percentage == "":
                        discount_percentage = 0
                    power_attributes = lens_sale_power_attribute_controller.get_power_attribute(new_data)
                    discount_checked = new_data.get('discount_checked')
                    is_discount_applied = 1 if discount_checked and discount_checked.lower() == 'on' else 0
                    insert_len_sales_query = f""" INSERT INTO `sales_order`
                                            (`order_id`, `product_id`, `hsn`, `unit_sale_price`, `unit_type`,
                                            `purchase_quantity`, `product_total_cost`, `discount_percentage`,
                                            `is_discount_applied`, `power_attribute`, `assigned_lab`, `customer_id`,
                                            `order_status`, `payment_status`, `delivery_status`, `payment_mode`,
                                            `amount_paid`, `estimated_delivery_date`, `created_by_store`,
                                            `created_by`, `created_on`, `updated_by`, `updated_on`, `created_by_store_type`)
                                            VALUES
                                            ('{billingDetailsData.get('orderId')}', {new_data.get('product')}, '{new_data.get('product_hsn')}', 
                                            {new_data.get('unit_price')}, '{new_data.get('unit_type')}', 
                                            {new_data.get('purchase_qty')}, {new_data.get('product_total')}, 
                                            {discount_percentage}, {is_discount_applied}, 
                                            '{json.dumps(power_attributes)}', {billingDetailsData.get('assignedLab')}, 
                                            {customer_id}, 1, 1, 1, 1, {billingDetailsData.get('amount_paid')}, %s, 
                                            {store_id}, {billingDetailsData.get('orderByEmployee')}, 
                                            '{today}', {billingDetailsData.get('orderByEmployee')}, '{today}', 1) """

                    cursor.execute(insert_len_sales_query,
                                   (convert_to_db_date_format(billingDetailsData.get('estDeliveryDate'))))

                    update_central_Inventory = f"""UPDATE central_inventory SET product_quantity = product_quantity - {new_data.get('purchase_qty')}
                                                                                                WHERE product_id = {new_data.get('product')}"""
                    cursor.execute(update_central_Inventory)

                elif new_data.get('product_category_id') == '3':
                    discount_percentage = new_data.get('discount_percentage')
                    if discount_percentage == "":
                        discount_percentage = 0
                    power_attributes = lens_sale_power_attribute_controller.get_power_attribute(new_data)
                    discount_checked = new_data.get('discount_checked')
                    is_discount_applied = 1 if discount_checked and discount_checked.lower() == 'on' else 0
                    insert_contact_len_sales_query = f""" INSERT INTO `sales_order`
                                                                (`order_id`, `product_id`, `hsn`, `unit_sale_price`, `unit_type`,
                                                                `purchase_quantity`, `product_total_cost`, `discount_percentage`,
                                                                `is_discount_applied`, `power_attribute`, `assigned_lab`, `customer_id`,
                                                                `order_status`, `payment_status`, `delivery_status`, `payment_mode`,
                                                                `amount_paid`, `estimated_delivery_date`, `created_by_store`,
                                                                `created_by`, `created_on`, `updated_by`, `updated_on`, `created_by_store_type`)
                                                                VALUES
                                                                ('{billingDetailsData.get('orderId')}', {new_data.get('product')}, '{new_data.get('product_hsn')}', 
                                                                '{new_data.get('unit_price')}', '{new_data.get('unit_type')}', 
                                                                {new_data.get('purchase_qty')}, {new_data.get('product_total')}, 
                                                                {discount_percentage}, {is_discount_applied}, 
                                                                '{json.dumps(power_attributes)}', 1, 
                                                                {customer_id}, {billingDetailsData.get('assignedLab')}, 1, 1, 1, {billingDetailsData.get('amount_paid')}, %s, 
                                                                {store_id}, {billingDetailsData.get('orderByEmployee')}, 
                                                                '{today}', {billingDetailsData.get('orderByEmployee')}, '{today}', 1) """
                    cursor.execute(insert_contact_len_sales_query,
                                   (convert_to_db_date_format(billingDetailsData.get('estDeliveryDate'))))

                    update_central_Inventory = f"""UPDATE central_inventory
                                                SET product_quantity = product_quantity - {new_data.get('purchase_qty')}
                                                WHERE product_id = {new_data.get('product')}"""
                    cursor.execute(update_central_Inventory)
                else:
                    discount_percentage = new_data.get('discount_percentage')
                    if discount_percentage == "":
                        discount_percentage = 0
                    discount_checked = new_data.get('discount_checked')
                    is_discount_applied = 1 if discount_checked and discount_checked.lower() == 'on' else 0
                    power_attributes = {}
                    insert_contact_len_sales_query = f"""
                                                            INSERT INTO `sales_order`
                                                            (`order_id`, `product_id`, `hsn`, `unit_sale_price`, `unit_type`,
                                                            `purchase_quantity`, `product_total_cost`, `discount_percentage`,
                                                            `is_discount_applied`, `assigned_lab`, `customer_id`,
                                                            `order_status`, `payment_status`, `delivery_status`, `payment_mode`,
                                                            `amount_paid`, `estimated_delivery_date`, `created_by_store`,
                                                            `created_by`, `created_on`, `updated_by`, `updated_on`, `power_attribute`, `created_by_store_type`)
                                                            VALUES
                                                            ('{billingDetailsData.get('orderId')}', {new_data.get('product')}, '{new_data.get('product_hsn')}', 
                                                            {new_data.get('unit_price')}, '{new_data.get('unit_type')}', 
                                                            {new_data.get('purchase_qty')}, {new_data.get('product_total')}, 
                                                            {discount_percentage}, {is_discount_applied}, 
                                                            {billingDetailsData.get('assignedLab')}, {customer_id}, 1, 1, 1, 1, {billingDetailsData.get('amount_paid')}, %s, 
                                                            {store_id}, {billingDetailsData.get('orderByEmployee')}, '{today}', {billingDetailsData.get('orderByEmployee')}, '{today}', '{power_attributes}', 1 )
                                                        """

                    cursor.execute(insert_contact_len_sales_query,
                                   (convert_to_db_date_format(billingDetailsData.get('estDeliveryDate'))))
                    update_central_Inventory = f"""UPDATE store_inventory SET
                     product_quantity = product_quantity - {new_data.get('purchase_qty')}
                                          WHERE product_id = {new_data.get('product')} AND
                                                store_id = {store_id} AND store_type = 1"""
                    cursor.execute(update_central_Inventory)

            return {
                "status": True,
                "message": "success",
                "order_id": billingDetailsData.get('orderId')
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
