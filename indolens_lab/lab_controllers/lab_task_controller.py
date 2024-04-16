import datetime
import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_models.admin_resp_model.sales_detail_resp_model import get_order_detail
from indolens_lab.lab_models.response_model.lab_job_resp_model import get_lab_jobs_list


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
                WHERE so.sale_item_id = '{saleId}' AND so.assigned_lab = {assigned_lab}
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

            frames_list = [{"frame_id": frame_id, "frame_name": frame_name} for frame_id, frame_name in all_frame_details]
            print(frames_list)
            return {
                "status": True,
                "orders_details": get_order_detail(orders_details),
                "frame_list": frames_list
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
