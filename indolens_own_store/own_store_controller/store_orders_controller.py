import datetime
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_controllers import email_template_controller, send_notification_controller
from indolens_admin.admin_models.admin_resp_model.completed_order_resp_model import get_completed_sales_orders
from indolens_admin.admin_models.admin_resp_model.sales_detail_resp_model import get_order_detail
from indolens_admin.admin_models.admin_resp_model.sales_resp_model import get_sales_orders


def getIndianTime():
    ist = pytz.timezone('Asia/Kolkata')
    today = datetime.datetime.now(ist)
    return today


def get_all_orders(status, pay_status, store_id):
    status_conditions = {
        "All": "LIKE '%'",
        "New": "= 1",
        "Processing": "= 2",
        "Ready": "= 3",
        "Dispatched": "= 4",
        "Delivered Store": "= 5",
        "Delivered Customer": "= 6",
        "Cancelled": "= 7",
    }
    status_condition = status_conditions[status]
    payment_status_values = {
        "All": "LIKE '%'",
        "Pending": "= 1",
        "Completed": "= 2",
        "Refunded": "= 3",
    }
    payment_status_value = payment_status_values[pay_status]
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                            SELECT 
                                so.*, 
                                c.customer_name AS customer_name, 
                                SUM(so_product_total_cost) AS total_cost, 
                                CASE 
                                    WHEN so.so_created_by_store_type = 1 THEN os.os_store_name 
                                    ELSE fs.fs_store_name 
                                END AS store_name,
                                CASE 
                                    WHEN so.so_created_by_store_type = 1 THEN creator_os.ose_name 
                                    ELSE creator_fs.fse_name 
                                END AS creator_name,
                                CASE 
                                    WHEN so.so_created_by_store_type = 1 THEN updater_os.ose_name 
                                    ELSE updater_fs.fse_name 
                                END AS updater_name,
                                i.invoice_invoice_number AS invoice_number
                            FROM sales_order AS so
                            LEFT JOIN invoice AS i ON i.invoice_order_id = so.so_order_id
                            LEFT JOIN customers AS c ON c.customer_customer_id = so.so_customer_id
                            LEFT JOIN own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                            LEFT JOIN franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                            LEFT JOIN own_store_employees creator_os ON so.so_created_by = creator_os.ose_employee_id AND so.so_created_by_store_type = 1
                            LEFT JOIN franchise_store_employees creator_fs ON so.so_created_by = creator_fs.fse_employee_id AND so.so_created_by_store_type = 2
                            LEFT JOIN own_store_employees updater_os ON so.so_updated_by = updater_os.ose_employee_id AND so.so_created_by_store_type = 1
                            LEFT JOIN franchise_store_employees updater_fs ON so.so_updated_by = updater_fs.fse_employee_id AND so.so_created_by_store_type = 2
                            WHERE so.so_order_status {status_condition} AND so.so_payment_status {payment_status_value} AND so.so_created_by_store_type = 1
                            AND so.so_created_by_store = {store_id}
                            GROUP BY so.so_order_id ORDER BY so.so_sale_item_id DESC         
                            """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                "status": True,
                "orders_list": orders_list,
                "dash_orders_list": orders_list[:15]
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_completed_orders(status, pay_status, store_id):
    status_conditions = {
        "All": "LIKE '%'",
        "New": "= 1",
        "Processing": "= 2",
        "Ready": "= 3",
        "Dispatched": "= 4",
        "Delivered Store": "= 5",
        "Delivered Customer": "= 6",
        "Cancelled": "= 7",
    }
    status_condition = status_conditions[status]
    payment_status_values = {
        "All": "LIKE '%'",
        "Pending": "= 1",
        "Completed": "= 2",
        "Refunded": "= 3",
    }
    payment_status_value = payment_status_values[pay_status]
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                SELECT 
                    so.*, 
                    c.name, 
                    SUM(product_total_cost) AS total_cost, 
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN os.store_name 
                        ELSE fs.store_name 
                    END AS store_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN creator_os.name 
                        ELSE creator_fs.name 
                    END AS creator_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN updater_os.name 
                        ELSE updater_fs.name 
                    END AS updater_name,
                    i.invoice_number
                FROM sales_order AS so
                LEFT JOIN customers AS c ON c.customer_id = so.customer_id
                LEFT JOIN invoice AS i ON i.order_id = so.order_id
                LEFT JOIN own_store os ON so.created_by_store = os.store_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store fs ON so.created_by_store = fs.store_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees creator_os ON so.created_by = creator_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees creator_fs ON so.created_by = creator_fs.employee_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees updater_os ON so.updated_by = updater_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees updater_fs ON so.updated_by = updater_fs.employee_id AND so.created_by_store_type = 2
                WHERE so.order_status {status_condition} AND so.payment_status {payment_status_value} AND so.created_by_store_type = 1
                AND so.created_by_store = {store_id}
                GROUP BY so.order_id ORDER BY so.sale_item_id DESC        
                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                "status": True,
                "orders_list": get_completed_sales_orders(orders_list)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_store_orders(store_id, store_type):
    try:
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                SELECT 
                    so.*, 
                    c.name, 
                    SUM(product_total_cost) AS total_cost, 
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN os.store_name 
                        ELSE fs.store_name 
                    END AS store_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN creator_os.name 
                        ELSE creator_fs.name 
                    END AS creator_name,
                    CASE 
                        WHEN so.created_by_store_type = 1 THEN updater_os.name 
                        ELSE updater_fs.name 
                    END AS updater_name
                FROM sales_order AS so
                LEFT JOIN customers AS c ON c.customer_id = so.customer_id
                LEFT JOIN own_store os ON so.created_by_store = os.store_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store fs ON so.created_by_store = fs.store_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees creator_os ON so.created_by = creator_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees creator_fs ON so.created_by = creator_fs.employee_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees updater_os ON so.updated_by = updater_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees updater_fs ON so.updated_by = updater_fs.employee_id AND so.created_by_store_type = 2
                WHERE so.created_by_store = {store_id} AND so.created_by_store_type = {store_type}
                GROUP BY so.order_id          
                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                "status": True,
                "orders_list": get_sales_orders(orders_list)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def order_status_change(orderID, orderStatus, updated_by, store_id):
    print(orderStatus)
    status_conditions = {
        "2": "Processing",
        "3": "Ready",
        "4": "Dispatched to store",
        "5": "Ready in store",
        "6": "Delivered to customer",
        "7": "Cancelled"
    }
    status_condition = status_conditions[orderStatus]

    try:
        with getConnection().cursor() as cursor:
            order_status_change_query = f"""
                UPDATE sales_order SET so_order_status = {orderStatus}, so_updated_on = '{getIndianTime()}',
                so_updated_by = {updated_by}
                WHERE so_order_id = '{orderID}' """
            cursor.execute(order_status_change_query)

            add_order_track_query = f""" 
                            INSERT INTO order_track (order_id, status, created_on) 
                            VALUES ('{orderID}', {orderStatus}, '{getIndianTime()}' ) """
            cursor.execute(add_order_track_query)

            get_order_details_query = f"""
                            SELECT 
                                so.*, c.customer_name AS customer_name, c.customer_email AS customer_email
                            FROM sales_order AS so
                            LEFT JOIN customers AS c ON c.customer_customer_id = so.so_customer_id
                            WHERE so.so_order_id = '{orderID}' GROUP BY so.so_sale_item_id  
                            """
            cursor.execute(get_order_details_query)
            order = cursor.fetchall()
            print(order)

            if orderStatus == "6":
                print("order completed")
                # payment_status_change_query = f"""
                #                 UPDATE sales_order SET payment_status = 2
                #                 WHERE order_id = '{orderID}'
                #                 """
                # cursor.execute(payment_status_change_query)

                get_last_invoice_query = f""" SELECT invoice_invoice_number
                                                FROM invoice
                                                WHERE invoice_store_id = {order[0]['so_created_by_store']} 
                                                AND invoice_store_type = {order[0]['so_created_by_store_type']}
                                                ORDER BY invoice_invoice_id DESC
                                                LIMIT 1;
                                                """
                cursor.execute(get_last_invoice_query)
                existing_invoice = cursor.fetchone()

                if existing_invoice:
                    last_invoice_number = existing_invoice['invoice_invoice_number']
                    store_code, store_id, date_part, number_part = last_invoice_number.split('_')
                    number_part = str(int(number_part) + 1).zfill(8)
                    invoice_number = f"{store_code}_{store_id}_{date_part}_{number_part}"
                else:
                    number_part = '00000001'
                    store_code = 'OS' if order[0]['created_by_store_type'] == 1 else 'FS'

                    store_id = order[0]['created_by_store']
                    date_part = getIndianTime().strftime('%d%m%Y')

                    invoice_number = f"{store_code}_{store_id}_{date_part}_{number_part}"

                create_invoice_query = f""" 
                                            INSERT INTO invoice (invoice_invoice_number, invoice_order_id , 
                                            invoice_invoice_status, invoice_invoice_date,
                                            invoice_store_id,invoice_store_type) 
                                            VALUES ('{invoice_number}', '{orderID}', 1, '{getIndianTime().date()}', 
                                            {order[0]['so_created_by_store']},{order[0]['so_created_by_store_type']}) """
                cursor.execute(create_invoice_query)

                subject = email_template_controller.get_order_completion_email_subject(order[0]['so_order_id'])
                body = email_template_controller.get_order_completion_email_body(order[0]['customer_name'],
                                                                                 order[0]['so_order_id'],
                                                                                 status_condition, getIndianTime())
                print(subject)
                print(body)
                send_notification_controller.send_email(subject, body, order[0]['customer_email'])

            if orderStatus == "7":
                subject = email_template_controller.get_order_cancelled_email_subject(order[0]['so_order_id'])
                body = email_template_controller.get_order_cancelled_email_body(order[0]['customer_name'],
                                                                                    order[0]['so_order_id'],
                                                                                    status_condition, getIndianTime())
                print(subject)
                print(body)
                email_resp = send_notification_controller.send_email(subject, body, order[0]['customer_email'])
                print(email_resp)

            else:
                subject = email_template_controller.get_order_status_change_email_subject(order[0]['so_order_id'])
                body = email_template_controller.get_order_status_change_email_body(order[0]['customer_name'],
                                                                                    order[0]['so_order_id'],
                                                                                    status_condition, getIndianTime())
                print(subject)
                print(body)
                email_resp = send_notification_controller.send_email(subject, body, order[0]['customer_email'])
                print(email_resp)

            return {
                "status": True,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def order_payment_status_change(order_data, store_id, created_by):
    status_conditions = {
        "2": "Completed",
        "3": "Refunded"
    }
    status_condition = status_conditions[order_data['order_payment_status']]
    try:
        with getConnection().cursor() as cursor:
            order_payment_status_change_query = f"""
                UPDATE sales_order 
                SET 
                    so_payment_status = {order_data['order_payment_status']}, so_updated_on = '{getIndianTime()}',
                    so_updated_by = {created_by},
                    so_amount_paid = 
                        CASE 
                            WHEN {order_data['order_payment_status']} = 2 THEN so_amount_paid + {order_data['order_payment_amount']}
                            ELSE so_amount_paid - {order_data['order_payment_amount']}
                        END
                WHERE so_order_id = '{order_data['order_id']}'
            """
            cursor.execute(order_payment_status_change_query)

            order_payment_track_query = f"""INSERT INTO sales_order_payment_track (sopt_order_id, sopt_payment_amount, 
                                            sopt_payment_mode, sopt_payment_type, sopt_created_by_store, 
                                            sopt_created_by_store_type, sopt_created_by_id, sopt_created_on )
                                            VALUES ('{order_data['order_id']}', {order_data['order_payment_amount']},
                                            {order_data['payment_mode']}, {order_data['order_payment_status']}, 
                                            {store_id}, 1, {created_by}, '{getIndianTime()}') """
            cursor.execute(order_payment_track_query)

            if order_data['order_payment_status'] == "3":
                order_status_change_query = f"""
                                UPDATE sales_order SET so_order_status = 7
                                WHERE so_order_id = '{order_data['order_id']}'
                                """
                cursor.execute(order_status_change_query)
                add_order_track_query = f""" 
                                            INSERT INTO order_track (order_id, status, created_on) 
                                            VALUES ('{order_data['order_id']}', {7}, '{getIndianTime()}' ) """
                cursor.execute(add_order_track_query)

            get_order_details_query = f"""
                                       SELECT 
                                           so.*, c.customer_name AS customer_name, c.customer_email AS customer_email
                                       FROM sales_order AS so
                                       LEFT JOIN customers AS c ON c.customer_customer_id = so.so_customer_id
                                       WHERE so.so_order_id = '{order_data['order_id']}' GROUP BY so.so_sale_item_id  
                                       """
            cursor.execute(get_order_details_query)
            order = cursor.fetchall()

            subject = email_template_controller.get_order_payment_status_change_email_subject(order[0]['so_order_id'])
            body = email_template_controller.get_order_payment_status_change_email_body(order[0]['customer_name'],
                                                                                        order[0]['so_order_id'],
                                                                                        status_condition,
                                                                                        getIndianTime())
            send_notification_controller.send_email(subject, body, order[0]['customer_email'])

            return {
                "status": True,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
