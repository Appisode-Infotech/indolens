import datetime
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.sales_detail_resp_model import get_order_detail
from indolens_lab.lab_models.response_model.lab_job_resp_model import get_lab_jobs_list


def get_lab_jobs(labId, status):
    status_conditions = {
        "All": "IN (1,2,3,4)",
        "New": "= 1",
        "Processing": "= 2",
        "Ready": "= 3",
        "Dispatched": "= 4",
    }
    status_condition = status_conditions[status]
    try:
        with connection.cursor() as cursor:
            get_job_details_query = f"""
                SELECT 
                    so.*,
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
                WHERE so.assigned_lab = {labId} AND so.order_status {status_condition}
                GROUP BY so.order_id ORDER BY so.sale_item_id DESC  
                """
            cursor.execute(get_job_details_query)
            jobs_details = cursor.fetchall()

            return {
                "status": True,
                "task_list": get_lab_jobs_list(jobs_details),
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_job_details(orderId, assigned_lab):
    try:
        with connection.cursor() as cursor:
            get_order_details_query = f"""
                SELECT 
                    so.*,
                    (SELECT SUM(unit_sale_price*purchase_quantity) AS total_cost FROM sales_order WHERE order_id = '{orderId}' 
                    GROUP BY order_id ), 
                    (SELECT SUM(product_total_cost) AS discount_cost FROM sales_order WHERE order_id = '{orderId}' 
                    GROUP BY order_id ), 
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
                WHERE so.order_id = '{orderId}' AND so.assigned_lab = {assigned_lab} 
                GROUP BY so.sale_item_id  
                """
            cursor.execute(get_order_details_query)
            orders_details = cursor.fetchall()

            return {
                "status": True,
                "orders_details": get_order_detail(orders_details),
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_job_stats(labId):
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

            get_processing_job_details_query = f"""
                                        SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                        FROM (
                                            SELECT COUNT(DISTINCT order_id) AS total_count
                                            FROM sales_order
                                            WHERE assigned_lab = {labId} AND order_status = 2
                                            GROUP BY order_id
                                        ) AS subquery
                                        """
            cursor.execute(get_processing_job_details_query)
            processing_jobs = cursor.fetchone()

            get_ready_job_details_query = f"""
                                        SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                        FROM (
                                            SELECT COUNT(DISTINCT order_id) AS total_count
                                            FROM sales_order
                                            WHERE assigned_lab = {labId} AND order_status = 3
                                            GROUP BY order_id
                                        ) AS subquery
                                        """
            cursor.execute(get_ready_job_details_query)
            ready_jobs = cursor.fetchone()

            get_dispatched_job_details_query = f"""
                                        SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                        FROM (
                                            SELECT COUNT(DISTINCT order_id) AS total_count
                                            FROM sales_order
                                            WHERE assigned_lab = {labId} AND order_status = 4
                                            GROUP BY order_id
                                        ) AS subquery
                                        """

            cursor.execute(get_dispatched_job_details_query)
            dispatched_jobs = cursor.fetchone()

            return {
                "status": True,
                "new_jobs": new_jobs[0],
                "processing_jobs": processing_jobs[0],
                "ready_jobs": ready_jobs[0],
                "dispatched_jobs": dispatched_jobs[0],
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
