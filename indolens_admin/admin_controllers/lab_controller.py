import datetime

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.lab_resp_model import get_labs
from indolens_admin.admin_models.admin_resp_model.sales_detail_resp_model import get_order_detail
from indolens_admin.admin_models.admin_resp_model.sales_resp_model import get_sales_orders

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def create_lab(lab_obj):
    cleaned_str = lab_obj.lab_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    lab_lat, lab_lng = map(float, cleaned_str.split(', '))
    try:
        with connection.cursor() as cursor:
            create_lab_query = f"""
                                    INSERT INTO lab (
                                        lab_name, lab_display_name, lab_phone, lab_gst, lab_email,
                                        lab_city, lab_state, lab_zip, lab_lat, lab_lng, lab_address,
                                        status, created_by, created_on, last_updated_by, last_updated_on) 
                                    VALUES ('{lab_obj.lab_name}', '{lab_obj.lab_display_name}', 
                                            '{lab_obj.lab_phone}', '{lab_obj.lab_gstin}', 
                                            '{lab_obj.lab_email}', '{lab_obj.lab_city}', 
                                            '{lab_obj.lab_state}', '{lab_obj.lab_zip_code}', '{lab_lat}',
                                            '{lab_lng}', '{lab_obj.complete_address}', 1, {lab_obj.created_by}, 
                                            '{getIndianTime()}', {lab_obj.last_updated_by}, '{getIndianTime()}')"""

            cursor.execute(create_lab_query)
            lab_id = cursor.lastrowid
            return {
                "status": True,
                "message": "lab added",
                "labId": lab_id
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_labs():
    try:
        with connection.cursor() as cursor:
            get_lab_query = f""" SELECT l.*, creator.name, updater.name, lt.name, 
                                COUNT(DISTINCT CASE WHEN so.order_status IN (1, 2, 3) THEN so.order_id END)
                                FROM lab AS l
                                LEFT JOIN lab_technician AS lt ON lt.assigned_lab_id = l.lab_id
                                LEFT JOIN admin AS creator ON l.created_by = creator.admin_id
                                LEFT JOIN admin AS updater ON l.last_updated_by = updater.admin_id
                                LEFT JOIN sales_order AS so ON l.lab_id = so.assigned_lab
                                GROUP BY l.lab_id
                                ORDER BY l.lab_id DESC"""
            cursor.execute(get_lab_query)
            lab_data = cursor.fetchall()
            return {
                "status": True,
                "lab_list": get_labs(lab_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_all_active_labs():
    try:
        with connection.cursor() as cursor:
            get_lab_query = f""" SELECT l.*, creator.name, updater.name, lt.name, 
                                COUNT(DISTINCT CASE WHEN so.order_status IN (1, 2, 3) THEN so.order_id END)
                                FROM lab AS l
                                LEFT JOIN lab_technician AS lt ON lt.assigned_lab_id = l.lab_id
                                LEFT JOIN admin AS creator ON l.created_by = creator.admin_id
                                LEFT JOIN admin AS updater ON l.last_updated_by = updater.admin_id
                                LEFT JOIN sales_order AS so ON l.lab_id = so.assigned_lab
                                WHERE l.status = 1
                                GROUP BY l.lab_id
                                ORDER BY l.lab_id DESC"""
            cursor.execute(get_lab_query)
            lab_data = cursor.fetchall()
            return {
                "status": True,
                "lab_list": get_labs(lab_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_by_id(labid):
    try:
        with connection.cursor() as cursor:
            get_lab_query = f""" SELECT l.*, creator.name, updater.name, lt.name,  COUNT(DISTINCT so.order_id) AS order_count
                                FROM lab AS l
                                LEFT JOIN lab_technician AS lt ON lt.assigned_lab_id = l.lab_id
                                LEFT JOIN admin AS creator ON l.created_by = creator.admin_id
                                LEFT JOIN admin AS updater ON l.last_updated_by = updater.admin_id
                                LEFT JOIN sales_order AS so ON l.lab_id = so.assigned_lab
                                WHERE lab_id = '{labid}'"""
            cursor.execute(get_lab_query)
            lab_data = cursor.fetchall()
            return {
                "status": True,
                "lab_data": get_labs(lab_data)
            }, 200

    except pymysql.Error as e:
        print(e)
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        print(e)
        return {"status": False, "message": str(e)}, 301


def enable_disable_lab(labid, status):
    try:
        with connection.cursor() as cursor:
            update_lab_query = f"""
                UPDATE lab
                SET
                    status = {status}
                WHERE
                    lab_id = {labid}
            """

            # Execute the update query using your cursor
            cursor.execute(update_lab_query)

            return {
                "status": True,
                "message": "Lab updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_lab_by_id(lab_obj):
    cleaned_str = lab_obj.lab_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    lab_lat, lab_lng = map(float, cleaned_str.split(', '))
    try:
        with connection.cursor() as cursor:
            update_lab_query = f"""
                UPDATE lab
                SET 
                    lab_name = '{lab_obj.lab_name}',
                    lab_display_name = '{lab_obj.lab_display_name}',
                    lab_phone = '{lab_obj.lab_phone}',
                    lab_gst = '{lab_obj.lab_gstin}',
                    lab_email = '{lab_obj.lab_email}',
                    lab_city = '{lab_obj.lab_city}',
                    lab_state = '{lab_obj.lab_state}',
                    lab_zip = '{lab_obj.lab_zip_code}',
                    lab_lat = '{lab_lat}',
                    lab_lng = '{lab_lng}',
                    lab_address = '{lab_obj.complete_address}',
                    last_updated_on = '{getIndianTime()}',
                    last_updated_by = {lab_obj.last_updated_by}
                WHERE lab_id = {lab_obj.lab_id}
            """
            cursor.execute(update_lab_query)

            return {
                "status": True,
                "message": "Lab updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_job(labId):
    try:
        with connection.cursor() as cursor:
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
                WHERE so.assigned_lab = {labId}
                GROUP BY so.order_id ORDER BY so.sale_item_id DESC         
                """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                       "status": True,
                       "orders_list": get_sales_orders(orders_list),
                       "all_jobs_list": get_sales_orders(orders_list)
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_lab_stats(labId):
    try:
        with connection.cursor() as cursor:
            get_new_job_details_query = f"""
                                                    SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                                    FROM (
                                                        SELECT COUNT(DISTINCT order_id) AS total_count
                                                        FROM sales_order
                                                        WHERE assigned_lab = {labId} AND order_status = 1
                                                        GROUP BY order_id
                                                    ) AS subquery
                                                    """

            cursor.execute(get_new_job_details_query)
            new_jobs = cursor.fetchone()

            get_active_job_details_query = f"""
                                                    SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                                    FROM (
                                                        SELECT COUNT(DISTINCT order_id) AS total_count
                                                        FROM sales_order
                                                        WHERE assigned_lab = {labId} AND order_status IN ( 2,3)
                                                        GROUP BY order_id
                                                    ) AS subquery
                                                    """
            cursor.execute(get_active_job_details_query)
            active_jobs = cursor.fetchone()

            get_completed_job_details_query = f"""
                                                    SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                                    FROM (
                                                        SELECT COUNT(DISTINCT order_id) AS total_count
                                                        FROM sales_order
                                                        WHERE assigned_lab = {labId} AND order_status IN (4,5,6,7)
                                                        GROUP BY order_id
                                                    ) AS subquery
                                                    """
            cursor.execute(get_completed_job_details_query)
            completed_jobs = cursor.fetchone()

            get_total_job_details_query = f"""
                                                    SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                                    FROM (
                                                        SELECT COUNT(DISTINCT order_id) AS total_count
                                                        FROM sales_order
                                                        WHERE assigned_lab = {labId}
                                                        GROUP BY order_id
                                                    ) AS subquery
                                                    """

            cursor.execute(get_total_job_details_query)
            total_jobs = cursor.fetchone()

            return {
                "status": True,
                "new_jobs": new_jobs[0],
                "active_jobs": active_jobs[0],
                "completed_jobs": completed_jobs[0],
                "total_jobs": total_jobs[0],
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_job_authenticity_card(saleId):
    try:
        with connection.cursor() as cursor:
            get_order_details_query = f"""
                SELECT 
                    so.*,
                    (SELECT SUM(unit_sale_price*purchase_quantity) AS total_cost FROM sales_order WHERE sale_item_id = '{saleId}'), 
                    (SELECT SUM(product_total_cost) AS discount_cost FROM sales_order WHERE sale_item_id = '{saleId}' ), 
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
                    c.*, ci.*, pc.category_name, pm.material_name,
                    ft.frame_type_name, fsh.shape_name,co.color_name, u.unit_name, b.brand_name
                FROM sales_order AS so
                LEFT JOIN customers AS c ON c.customer_id = so.customer_id
                LEFT JOIN central_inventory AS ci ON ci.product_id = so.product_id
                LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                LEFT JOIN frame_shapes AS fsh ON ci.frame_shape_id = fsh.shape_id
                LEFT JOIN product_colors AS co ON ci.color_id = co.color_id
                LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                LEFT JOIN brands AS b ON ci.brand_id = b.brand_id
                LEFT JOIN own_store os ON so.created_by_store = os.store_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store fs ON so.created_by_store = fs.store_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees creator_os ON so.created_by = creator_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees creator_fs ON so.created_by = creator_fs.employee_id AND so.created_by_store_type = 2
                LEFT JOIN own_store_employees updater_os ON so.updated_by = updater_os.employee_id AND so.created_by_store_type = 1
                LEFT JOIN franchise_store_employees updater_fs ON so.updated_by = updater_fs.employee_id AND so.created_by_store_type = 2
                WHERE so.sale_item_id = '{saleId}'
                """
            cursor.execute(get_order_details_query)
            orders_details = cursor.fetchall()

            sale_item_details = get_order_detail(orders_details)

            all_frame_details = []

            if sale_item_details[0]['linked_item'] != 0:
                for product_id in sale_item_details[0]['linked_item']:
                    get_frame_details_query = f"""
                                    SELECT product_id, product_name
                                    FROM central_inventory
                                    WHERE product_id = {product_id}
                                """

                    cursor.execute(get_frame_details_query)
                    frame_details = cursor.fetchone()
                    all_frame_details.append(frame_details)

            frames_list = [{"frame_id": frame_id, "frame_name": frame_name} for frame_id, frame_name in
                           all_frame_details]
            return {
                "status": True,
                "orders_details": get_order_detail(orders_details),
                "frame_list": frames_list
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301