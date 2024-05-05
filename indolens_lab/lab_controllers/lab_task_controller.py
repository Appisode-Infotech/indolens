import datetime
import json

import pymysql
import pytz
from indolens.db_connection import getConnection
from indolens_admin.admin_controllers import email_template_controller, send_notification_controller


def getIndianTime():
    ist = pytz.timezone('Asia/Kolkata')
    today = datetime.datetime.now(ist)
    return today

def get_lab_jobs(labId, status):
    status_conditions = {
        "All": "IN (1,2,3,4,5,6,7)",
        "New": "= 1",
        "Processing": "= 2",
        "Ready": "= 3",
        "Dispatched": "IN (4,5,6,7)",
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_order_details_query = f"""
                            SELECT 
                                so.*,
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
                                c.*, ci.*, pc.pc_category_name, pm.pm_material_name,
                                ft.ftype_name, fsh.fshape_name,co.pcol_color_name, u.unit_name, b.brand_name
                                
                            FROM 
                                sales_order AS so
                            LEFT JOIN 
                                customers AS c ON c.customer_customer_id = so.so_customer_id
                            LEFT JOIN 
                                lab AS l ON so.so_assigned_lab = l.lab_lab_id
                            LEFT JOIN 
                                central_inventory AS ci ON ci.ci_product_id = so.so_product_id
                            LEFT JOIN 
                                product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                            LEFT JOIN 
                                product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                            LEFT JOIN 
                                frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                            LEFT JOIN 
                                frame_shapes AS fsh ON ci.ci_frame_shape_id = fsh.fshape_shape_id
                            LEFT JOIN 
                                product_colors AS co ON ci.ci_color_id = co.pcol_color_id
                            LEFT JOIN 
                                units AS u ON ci.ci_unit_id = u.unit_unit_id
                            LEFT JOIN 
                                brands AS b ON ci.ci_brand_id = b.brand_brand_id
                            LEFT JOIN 
                                own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                            LEFT JOIN 
                                franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                            LEFT JOIN 
                                own_store_employees creator_os ON so.so_created_by = creator_os.ose_employee_id AND so.so_created_by_store_type = 1
                            LEFT JOIN 
                                franchise_store_employees creator_fs ON so.so_created_by = creator_fs.fse_employee_id AND so.so_created_by_store_type = 2
                            LEFT JOIN 
                                own_store_employees updater_os ON so.so_updated_by = updater_os.ose_employee_id AND so.so_created_by_store_type = 1
                            LEFT JOIN 
                                franchise_store_employees updater_fs ON so.so_updated_by = updater_fs.fse_employee_id AND so.so_created_by_store_type = 2
                            WHERE so.so_assigned_lab = {labId} AND so.so_order_status {status_condition}
                            GROUP BY so.so_order_id ORDER BY so.so_sale_item_id DESC 
                        """
            cursor.execute(get_order_details_query)
            jobs_details = cursor.fetchall()

            return {
                "status": True,
                "task_list": jobs_details,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_job_details(orderId, assigned_lab):
    try:
        with getConnection().cursor() as cursor:
            get_order_details_query = f"""
                            SELECT 
                                so.*,
                                (SELECT SUM(so_unit_sale_price * so_purchase_quantity)  FROM sales_order 
                                WHERE so_order_id = '{orderId}' GROUP BY so_order_id) AS total_cost ,
                                (SELECT SUM(so_product_total_cost)  FROM sales_order 
                                WHERE so_order_id = '{orderId}' GROUP BY so_order_id) AS discount_cost,
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
                                c.*, ci.*, pc.pc_category_name, pm.pm_material_name,
                                ft.ftype_name, fsh.fshape_name,co.pcol_color_name, u.unit_name, b.brand_name,
                                ROUND((ci.ci_product_gst / 2), 2) AS product_gst_half, l.lab_name,
                                ROUND(((100 * so.so_unit_sale_price / (100 + ci.ci_product_gst)) - (so.so_discount_percentage / 100) * (100 * so.so_unit_sale_price / (100 + ci.ci_product_gst))), 2) AS discounted_total_cost
                            FROM 
                                sales_order AS so
                            LEFT JOIN 
                                customers AS c ON c.customer_customer_id = so.so_customer_id
                            LEFT JOIN 
                                lab AS l ON so.so_assigned_lab = l.lab_lab_id
                            LEFT JOIN 
                                central_inventory AS ci ON ci.ci_product_id = so.so_product_id
                            LEFT JOIN 
                                product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                            LEFT JOIN 
                                product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                            LEFT JOIN 
                                frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                            LEFT JOIN 
                                frame_shapes AS fsh ON ci.ci_frame_shape_id = fsh.fshape_shape_id
                            LEFT JOIN 
                                product_colors AS co ON ci.ci_color_id = co.pcol_color_id
                            LEFT JOIN 
                                units AS u ON ci.ci_unit_id = u.unit_unit_id
                            LEFT JOIN 
                                brands AS b ON ci.ci_brand_id = b.brand_brand_id
                            LEFT JOIN 
                                own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                            LEFT JOIN 
                                franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                            LEFT JOIN 
                                own_store_employees creator_os ON so.so_created_by = creator_os.ose_employee_id AND so.so_created_by_store_type = 1
                            LEFT JOIN 
                                franchise_store_employees creator_fs ON so.so_created_by = creator_fs.fse_employee_id AND so.so_created_by_store_type = 2
                            LEFT JOIN 
                                own_store_employees updater_os ON so.so_updated_by = updater_os.ose_employee_id AND so.so_created_by_store_type = 1
                            LEFT JOIN 
                                franchise_store_employees updater_fs ON so.so_updated_by = updater_fs.fse_employee_id AND so.so_created_by_store_type = 2
                               WHERE so.so_order_id = '{orderId}' AND so.so_assigned_lab = {assigned_lab} 
                        """
            cursor.execute(get_order_details_query)
            orders_details = cursor.fetchall()

            return {
                "status": True,
                "orders_details": orders_details,
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_sale_item_details(saleId, assigned_lab):
    try:
        with getConnection().cursor() as cursor:
            get_sale_item_details_query = f"""
                                        SELECT 
                                            so.*,
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
                                            c.*, ci.*, pc.pc_category_name, pm.pm_material_name,
                                            ft.ftype_name, fsh.fshape_name,co.pcol_color_name, u.unit_name, b.brand_name,
                                            ROUND((ci.ci_product_gst / 2), 2) AS product_gst_half, l.lab_name,
                                            ROUND(((100 * so.so_unit_sale_price / (100 + ci.ci_product_gst)) - (so.so_discount_percentage / 100) * (100 * so.so_unit_sale_price / (100 + ci.ci_product_gst))), 2) AS discounted_total_cost
                                        FROM 
                                            sales_order AS so
                                        LEFT JOIN 
                                            customers AS c ON c.customer_customer_id = so.so_customer_id
                                        LEFT JOIN 
                                            lab AS l ON so.so_assigned_lab = l.lab_lab_id
                                        LEFT JOIN 
                                            central_inventory AS ci ON ci.ci_product_id = so.so_product_id
                                        LEFT JOIN 
                                            product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                                        LEFT JOIN 
                                            product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                                        LEFT JOIN 
                                            frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                                        LEFT JOIN 
                                            frame_shapes AS fsh ON ci.ci_frame_shape_id = fsh.fshape_shape_id
                                        LEFT JOIN 
                                            product_colors AS co ON ci.ci_color_id = co.pcol_color_id
                                        LEFT JOIN 
                                            units AS u ON ci.ci_unit_id = u.unit_unit_id
                                        LEFT JOIN 
                                            brands AS b ON ci.ci_brand_id = b.brand_brand_id
                                        LEFT JOIN 
                                            own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                                        LEFT JOIN 
                                            franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                                        LEFT JOIN 
                                            own_store_employees creator_os ON so.so_created_by = creator_os.ose_employee_id AND so.so_created_by_store_type = 1
                                        LEFT JOIN 
                                            franchise_store_employees creator_fs ON so.so_created_by = creator_fs.fse_employee_id AND so.so_created_by_store_type = 2
                                        LEFT JOIN 
                                            own_store_employees updater_os ON so.so_updated_by = updater_os.ose_employee_id AND so.so_created_by_store_type = 1
                                        LEFT JOIN 
                                            franchise_store_employees updater_fs ON so.so_updated_by = updater_fs.fse_employee_id AND so.so_created_by_store_type = 2
                                        WHERE so.so_sale_item_id = '{saleId}' AND so.so_assigned_lab = {assigned_lab}
                                    """

            cursor.execute(get_sale_item_details_query)

            sale_item_details = cursor.fetchone()

            sale_item_details['so_linked_item'] = json.loads(sale_item_details['so_linked_item']) if sale_item_details[
                'so_linked_item'] else []
            sale_item_details['so_power_attribute'] = json.loads(sale_item_details['so_power_attribute']) if \
            sale_item_details[
                'so_power_attribute'] else []
            sale_item_details['ci_power_attribute'] = json.loads(sale_item_details['ci_power_attribute']) if \
            sale_item_details[
                'ci_power_attribute'] else []
            all_frame_details = []

            if sale_item_details['so_linked_item'] != 0:
                for product_id in sale_item_details['so_linked_item']:
                    get_frame_details_query = f"""
                                                SELECT ci_product_id, ci_product_name
                                                FROM central_inventory
                                                WHERE ci_product_id = {product_id}
                                            """

                    cursor.execute(get_frame_details_query)
                    frame_details = cursor.fetchone()
                    all_frame_details.append(frame_details)

            return {
                "status": True,
                "orders_details": sale_item_details,
                "frame_list": all_frame_details
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_job_stats(labId):
    try:
        with getConnection().cursor() as cursor:
            get_new_job_details_query = f"""
                                        SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                        FROM (
                                            SELECT COUNT(DISTINCT so_order_id) AS total_count
                                            FROM sales_order
                                            WHERE so_assigned_lab = {labId} AND so_order_status = 1
                                            GROUP BY so_order_id
                                        ) AS subquery
                                        """

            cursor.execute(get_new_job_details_query)
            new_jobs = cursor.fetchone()

            get_processing_job_details_query = f"""
                                        SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                        FROM (
                                            SELECT COUNT(DISTINCT so_order_id) AS total_count
                                            FROM sales_order
                                            WHERE so_assigned_lab = {labId} AND so_order_status = 2
                                            GROUP BY so_order_id
                                        ) AS subquery
                                        """
            cursor.execute(get_processing_job_details_query)
            processing_jobs = cursor.fetchone()

            get_ready_job_details_query = f"""
                                        SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                        FROM (
                                            SELECT COUNT(DISTINCT so_order_id) AS total_count
                                            FROM sales_order
                                            WHERE so_assigned_lab = {labId} AND so_order_status = 3
                                            GROUP BY so_order_id
                                        ) AS subquery
                                        """
            cursor.execute(get_ready_job_details_query)
            ready_jobs = cursor.fetchone()

            get_dispatched_job_details_query = f"""
                                        SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                        FROM (
                                            SELECT COUNT(DISTINCT so_order_id) AS total_count
                                            FROM sales_order
                                            WHERE so_assigned_lab = {labId} AND so_order_status IN (4,5,6,7)
                                            GROUP BY so_order_id
                                        ) AS subquery
                                        """

            cursor.execute(get_dispatched_job_details_query)
            dispatched_jobs = cursor.fetchone()

            return {
                "status": True,
                "new_jobs": new_jobs['total_count'],
                "processing_jobs": processing_jobs['total_count'],
                "ready_jobs": ready_jobs['total_count'],
                "dispatched_jobs": dispatched_jobs['total_count'],
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def task_status_change(orderID, orderStatus):
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
                UPDATE sales_order SET so_order_status = {orderStatus}
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
