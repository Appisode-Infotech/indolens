import datetime
import json
import re
import time

import pymysql
import pytz
from indolens.db_connection import getConnection

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


def create_franchise_store_expense(expense_obj):
    try:
        with getConnection().cursor() as cursor:
            insert_expense_obj_query = f"""
                            INSERT INTO store_expense (
                                se_store_id, se_store_type, se_expense_amount, se_expense_reason, se_expense_date, 
                                se_created_on, se_created_by
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


def get_all_franchise_store_expense(store_id, store_type):
    try:
        with getConnection().cursor() as cursor:
            get_expense_obj_query = f""" SELECT se.*, creator.fse_name AS creator_name FROM store_expense AS se
                                                        LEFT JOIN franchise_store_employees AS creator ON se.se_created_by = creator.fse_employee_id
                                                        WHERE se.se_store_id = {store_id} AND se.se_store_type= {store_type}
                                                        ORDER BY se.se_store_expense_id DESC"""
            cursor.execute(get_expense_obj_query)
            store_expense_data = cursor.fetchall()
            return {
                "status": True,
                "message": "success",
                "stor_expense_list": store_expense_data
            }, 200


    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def make_sale(cart_data, customerData, billingDetailsData, employee_id, store_id, order_id, total_amount):
    try:
        with getConnection().cursor() as cursor:
            create_update_customer = f"""INSERT INTO `customers`(`customer_name`, `customer_gender`, `customer_age`, 
                                                `customer_phone`, `customer_email`, `customer_language`, 
                                                `customer_city`, `customer_address`, `customer_created_by_employee_id`,
                                                `customer_created_by_store_id`, `customer_created_by_store_type`, 
                                                `customer_created_on`,
                                                `customer_updated_by_employee_id`, `customer_updated_by_store_id`, 
                                                `customer_updated_by_store_type`, `customer_updated_on`)
                                                VALUES ('{customerData.get('name')}','{customerData.get('gender')}',
                                                '{customerData.get('age')}','{customerData.get('phone')}',
                                                '{customerData.get('email')}','{customerData.get('language')}',
                                                '{customerData.get('city')}','{customerData.get('address')}',
                                                {billingDetailsData.get('orderByEmployee')},{store_id}, 2, '{getIndianTime()}',
                                                {billingDetailsData.get('orderByEmployee')},{store_id},'1', 
                                                '{getIndianTime()}')
                                                ON DUPLICATE KEY UPDATE 
                                                `customer_name` = '{customerData.get('name')}', 
                                                `customer_gender` = '{customerData.get('gender')}', 
                                                `customer_age` = '{customerData.get('age')}', 
                                                `customer_email` = '{customerData.get('email')}', 
                                                `customer_language` = '{customerData.get('language')}', 
                                                `customer_city` = '{customerData.get('city')}', 
                                                `customer_address` = '{customerData.get('address')}', 
                                                `customer_updated_by_employee_id` = {billingDetailsData.get('orderByEmployee')}, 
                                                `customer_updated_by_store_id` = {store_id}, 
                                                `customer_updated_by_store_type` = 2, 
                                                `customer_updated_on` = '{getIndianTime()}' """
            cursor.execute(create_update_customer)
            customer_id = cursor.lastrowid

            if billingDetailsData.get('amount_paid') != '0':
                order_payment_track_query = f"""INSERT INTO sales_order_payment_track (sopt_order_id, sopt_payment_amount, 
                                                    sopt_payment_mode, sopt_payment_type, sopt_created_by_store, 
                                                    sopt_created_by_store_type, sopt_created_by_id, sopt_created_on )
                                                    VALUES ('{order_id}', {billingDetailsData.get('amount_paid')},
                                                    {billingDetailsData.get('paymentMode')}, 1, {store_id}, 2,
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
                                            (`so_order_id`, `so_product_id`, `so_hsn`, `so_unit_sale_price`, `so_unit_type`,
                                            `so_purchase_quantity`, `so_product_total_cost`, `so_discount_percentage`,
                                            `so_is_discount_applied`, `so_power_attribute`, `so_assigned_lab`, 
                                            `so_customer_id`, `so_order_status`, `so_payment_status`, `so_delivery_status`, 
                                            `so_payment_mode`, `so_amount_paid`, `so_estimated_delivery_date`, 
                                            `so_created_by_store`, `so_created_by`, `so_created_on`, `so_updated_by`, 
                                            `so_updated_on`, `so_created_by_store_type`, `so_sales_note`, `so_linked_item`, `so_order_mode`)
                                            VALUES
                                            ('{order_id}', {new_data.get('product')}, 
                                            '{new_data.get('product_hsn')}', 
                                            {new_data.get('unit_price')}, '{new_data.get('unit_type')}', 
                                            {new_data.get('purchase_qty')}, {new_data.get('product_total')}, 
                                            {discount_percentage}, {is_discount_applied}, 
                                            '{json.dumps(power_attributes)}', {billingDetailsData.get('assignedLab')}, 
                                            {customer_id}, 1, 1, 1, {billingDetailsData.get('paymentMode')}, {billingDetailsData.get('amount_paid')}, %s, 
                                            {store_id}, {billingDetailsData.get('orderByEmployee')}, 
                                            '{getIndianTime()}', {billingDetailsData.get('orderByEmployee')}, 
                                            '{getIndianTime()}', 2, '{billingDetailsData.get('saleNote')}', 
                                            '{json.dumps(linked_items)}',1) """

                    cursor.execute(insert_len_sales_query,
                                   (convert_to_db_date_format(billingDetailsData.get('estDeliveryDate'))))

                    update_central_Inventory = f"""UPDATE central_inventory 
                                                    SET ci_product_quantity = ci_product_quantity - {new_data.get('purchase_qty')}
                                                    WHERE ci_product_id = {new_data.get('product')}"""
                    cursor.execute(update_central_Inventory)

                elif new_data.get('product_category_id') == '3':
                    discount_percentage = new_data.get('discount_percentage')
                    power_attributes = lens_sale_power_attribute_controller.get_power_attribute(new_data)
                    discount_checked = new_data.get('discount_checked')
                    is_discount_applied = 1 if discount_checked and discount_checked.lower() == 'on' else 0
                    if discount_percentage == "" or is_discount_applied == 0 or None:
                        discount_percentage = 0
                    insert_contact_len_sales_query = f""" INSERT INTO `sales_order`
                                                            (`so_order_id`, `so_product_id`, `so_hsn`, `so_unit_sale_price`, `so_unit_type`,
                                                            `so_purchase_quantity`, `so_product_total_cost`, `so_discount_percentage`,
                                                            `so_is_discount_applied`, `so_power_attribute`, `so_assigned_lab`, 
                                                            `so_customer_id`, `so_order_status`, `so_payment_status`, `so_delivery_status`, 
                                                            `so_payment_mode`, `so_amount_paid`, `so_estimated_delivery_date`, 
                                                            `so_created_by_store`, `so_created_by`, `so_created_on`, `so_updated_by`, 
                                                            `so_updated_on`, `so_created_by_store_type`, `so_sales_note`, `so_order_mode`)
                                                            VALUES
                                                            ('{order_id}', 
                                                            {new_data.get('product')}, '{new_data.get('product_hsn')}', 
                                                            '{new_data.get('unit_price')}', '{new_data.get('unit_type')}', 
                                                            {new_data.get('purchase_qty')}, {new_data.get('product_total')}, 
                                                            {discount_percentage}, {is_discount_applied}, 
                                                            '{json.dumps(power_attributes)}', {billingDetailsData.get('assignedLab')}, 
                                                            {customer_id}, 
                                                            1, 1, 1, {billingDetailsData.get('paymentMode')},{billingDetailsData.get('amount_paid')}, %s, 
                                                            {store_id}, {billingDetailsData.get('orderByEmployee')}, 
                                                            '{getIndianTime()}', 
                                                            {billingDetailsData.get('orderByEmployee')}, 
                                                            '{getIndianTime()}', 2, '{billingDetailsData.get('saleNote')}',1) """
                    cursor.execute(insert_contact_len_sales_query,
                                   (convert_to_db_date_format(billingDetailsData.get('estDeliveryDate'))))

                    update_central_Inventory = f"""UPDATE central_inventory
                                                SET ci_product_quantity = ci_product_quantity - {new_data.get('purchase_qty')}
                                                WHERE ci_product_id = {new_data.get('product')}"""
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
                                                    (`so_order_id`, `so_product_id`, `so_hsn`, `so_unit_sale_price`, `so_unit_type`,
                                                            `so_purchase_quantity`, `so_product_total_cost`, `so_discount_percentage`,
                                                            `so_is_discount_applied`, `so_assigned_lab`, 
                                                            `so_customer_id`, `so_order_status`, `so_payment_status`, `so_delivery_status`, 
                                                            `so_payment_mode`, `so_amount_paid`, `so_estimated_delivery_date`, 
                                                            `so_created_by_store`, `so_created_by`, `so_created_on`, `so_updated_by`, 
                                                            `so_updated_on`, `so_power_attribute`, `so_created_by_store_type`, `so_sales_note`, `so_order_mode`)
                                                                    VALUES
                                                    ('{order_id}', {new_data.get('product')}, '{new_data.get('product_hsn')}', 
                                                    {new_data.get('unit_price')}, '{new_data.get('unit_type')}', 
                                                    {new_data.get('purchase_qty')}, {new_data.get('product_total')}, 
                                                    {discount_percentage}, {is_discount_applied}, 
                                                    {billingDetailsData.get('assignedLab')}, {customer_id}, 1, 
                                                    1, 1, {billingDetailsData.get('paymentMode')}, {billingDetailsData.get('amount_paid')}, %s, 
                                                    {store_id}, {billingDetailsData.get('orderByEmployee')}, 
                                                    '{getIndianTime()}', {billingDetailsData.get('orderByEmployee')}, 
                                                    '{getIndianTime()}', '{power_attributes}', 2 , 
                                                    '{billingDetailsData.get('saleNote')}',1)
                                                """

                    cursor.execute(insert_contact_len_sales_query,
                                   (convert_to_db_date_format(billingDetailsData.get('estDeliveryDate'))))
                    update_central_Inventory = f"""UPDATE store_inventory SET
                     si_product_quantity = si_product_quantity - {new_data.get('purchase_qty')}
                                          WHERE si_product_id = {new_data.get('product')} AND
                                                si_store_id = {store_id} AND si_store_type = 2 """
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
            send_notification_controller.send_email(subject, body, customerData.get('email'))

            if float(total_amount) == float(billingDetailsData.get('amount_paid')):
                order_payment_status_change_query = f"""
                                            UPDATE sales_order 
                                            SET 
                                                so_payment_status = 2
                                            WHERE so_order_id = '{order_id}'
                                        """
                cursor.execute(order_payment_status_change_query)
                subject = email_template_controller.get_order_payment_status_change_email_subject(order_id)
                body = email_template_controller.get_order_payment_status_change_email_body(customerData.get('name'),
                                                                                            order_id,
                                                                                            'Completed',
                                                                                            getIndianTime())
                send_notification_controller.send_email(subject, body, customerData.get('email'))

            return {
                "status": True,
                "message": "success",
                "order_id": order_id
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
