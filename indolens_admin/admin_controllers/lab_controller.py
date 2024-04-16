import datetime
import json

import pymysql
import pytz
from indolens.db_connection import getConnection

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
        with getConnection().cursor() as cursor:
            create_lab_query = f"""
                INSERT INTO lab (
                    lab_name, lab_display_name, lab_phone, lab_gst, lab_email,
                    lab_city, lab_state, lab_zip, lab_lat, lab_lng, lab_address,
                    lab_status, lab_created_by, lab_created_on, lab_last_updated_by, lab_last_updated_on) 
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
        with getConnection().cursor() as cursor:
            get_lab_query = f""" SELECT l.*, creator.admin_name, updater.admin_name, lt.lt_name,
                                COUNT(DISTINCT CASE WHEN so.so_order_status IN (1, 2, 3) THEN so.so_order_id END) AS jobs_count
                                FROM lab AS l
                                LEFT JOIN lab_technician AS lt ON lt.lt_assigned_lab_id = l.lab_lab_id
                                LEFT JOIN admin AS creator ON l.lab_created_by = creator.admin_admin_id
                                LEFT JOIN admin AS updater ON l.lab_last_updated_by = updater.admin_admin_id
                                LEFT JOIN sales_order AS so ON l.lab_lab_id = so.so_assigned_lab
                                GROUP BY l.lab_lab_id
                                ORDER BY l.lab_lab_id DESC"""
            cursor.execute(get_lab_query)
            lab_data = cursor.fetchall()

            # get_lab_query = f"""
            # SELECT l.*, creator.admin_name, updater.admin_name, lt_id.lt_id, lt.lt_name,
            #        COUNT(DISTINCT CASE WHEN so.so_order_status IN (1, 2, 3) THEN so.so_order_id END) AS jobs_count
            # FROM lab AS l
            # LEFT JOIN (
            #     SELECT lt_assigned_lab_id, GROUP_CONCAT(lt_name) AS lt_name
            #     FROM lab_technician
            #     GROUP BY lt_assigned_lab_id
            # ) AS lt ON lt.lt_assigned_lab_id = l.lab_lab_id
            # LEFT JOIN (
            #     SELECT lt_lab_technician_id, GROUP_CONCAT(lt_lab_technician_id) AS lt_id
            #     FROM lab_technician
            #     GROUP BY lt_assigned_lab_id
            # ) AS lt_id ON lt.lt_assigned_lab_id = l.lab_lab_id
            # LEFT JOIN admin AS creator ON l.lab_created_by = creator.admin_admin_id
            # LEFT JOIN admin AS updater ON l.lab_last_updated_by = updater.admin_admin_id
            # LEFT JOIN sales_order AS so ON l.lab_lab_id = so.so_assigned_lab
            # GROUP BY l.lab_lab_id
            # ORDER BY l.lab_lab_id DESC
            # """
            # cursor.execute(get_lab_query)

            # lab_data = cursor.fetchall()
            # for lab in lab_data:
            #     if lab['lt_id'] is not None and lab['lt_name'] is not None:
            #         lab['id_name_pairs'] = list(zip(lab['lt_id'].split(','), lab['lt_name'].split(',')))
            #     else:
            #         lab['id_name_pairs'] = []

            return {
                "status": True,
                "lab_list": lab_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_all_active_labs():
    try:
        with getConnection().cursor() as cursor:
            get_lab_query = f""" SELECT l.*, creator.admin_name AS creator, updater.admin_name AS updater, 
                                lt.lt_name AS tech_name, 
                                COUNT(DISTINCT CASE WHEN so.so_order_status IN (1, 2, 3) THEN so.so_order_id END)
                                FROM lab AS l
                                LEFT JOIN lab_technician AS lt ON lt.lt_assigned_lab_id = l.lab_lab_id
                                LEFT JOIN admin AS creator ON l.lab_created_by = creator.admin_admin_id
                                LEFT JOIN admin AS updater ON l.lab_last_updated_by = updater.admin_admin_id
                                LEFT JOIN sales_order AS so ON l.lab_lab_id = so.so_assigned_lab
                                WHERE l.lab_status = 1
                                GROUP BY l.lab_lab_id
                                ORDER BY l.lab_lab_id DESC"""
            cursor.execute(get_lab_query)
            lab_data = cursor.fetchall()
            return {
                "status": True,
                "lab_list": lab_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_by_id(labid):
    try:
        with getConnection().cursor() as cursor:
            get_lab_query = f""" SELECT l.*, creator.admin_name AS creator_name, updater.admin_name As updater_name, 
                                lt.lt_name As lab_tech_name,  COUNT(DISTINCT so.so_order_id) AS order_count
                                FROM lab AS l
                                LEFT JOIN lab_technician AS lt ON lt.lt_assigned_lab_id = l.lab_lab_id
                                LEFT JOIN admin AS creator ON l.lab_created_by = creator.admin_admin_id
                                LEFT JOIN admin AS updater ON l.lab_last_updated_by = updater.admin_admin_id
                                LEFT JOIN sales_order AS so ON l.lab_lab_id = so.so_assigned_lab
                                WHERE lab_lab_id = '{labid}'"""
            cursor.execute(get_lab_query)
            lab_data = cursor.fetchone()

            return {
                "status": True,
                "lab_data": lab_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_lab(labid, status):
    try:
        with getConnection().cursor() as cursor:
            update_lab_query = f"""
                UPDATE lab
                SET
                    lab_status = {status}
                WHERE
                    lab_lab_id = {labid}
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
        with getConnection().cursor() as cursor:
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
                    lab_last_updated_on = '{getIndianTime()}',
                    lab_last_updated_by = {lab_obj.last_updated_by}
                WHERE lab_lab_id = {lab_obj.lab_id}
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
        with getConnection().cursor() as cursor:
            get_order_query = f"""
                            SELECT 
                                so.*, 
                                c.customer_name, 
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
                                END AS updater_name
                            FROM sales_order AS so
                            LEFT JOIN customers AS c ON c.customer_customer_id = so.so_customer_id
                            LEFT JOIN own_store os ON so.so_created_by_store = os.os_store_id AND so.so_created_by_store_type = 1
                            LEFT JOIN franchise_store fs ON so.so_created_by_store = fs.fs_store_id AND so.so_created_by_store_type = 2
                            LEFT JOIN own_store_employees creator_os ON so.so_created_by = creator_os.ose_employee_id AND so.so_created_by_store_type = 1
                            LEFT JOIN franchise_store_employees creator_fs ON so.so_created_by = creator_fs.fse_employee_id AND so.so_created_by_store_type = 2
                            LEFT JOIN own_store_employees updater_os ON so.so_updated_by = updater_os.ose_employee_id AND so.so_created_by_store_type = 1
                            LEFT JOIN franchise_store_employees updater_fs ON so.so_updated_by = updater_fs.fse_employee_id AND so.so_created_by_store_type = 2
                            WHERE so.so_assigned_lab = {labId}
                            GROUP BY so.so_order_id ORDER BY so.so_sale_item_id DESC         
                            """
            cursor.execute(get_order_query)
            orders_list = cursor.fetchall()

            return {
                       "status": True,
                       "orders_list": orders_list,
                       "all_jobs_list": orders_list
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_lab_stats(labId):
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

            get_active_job_details_query = f"""
                                                    SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                                    FROM (
                                                        SELECT COUNT(DISTINCT so_order_id) AS total_count
                                                        FROM sales_order
                                                        WHERE so_assigned_lab = {labId} AND so_order_status IN ( 2,3)
                                                        GROUP BY so_order_id
                                                    ) AS subquery
                                                    """
            cursor.execute(get_active_job_details_query)
            active_jobs = cursor.fetchone()

            get_completed_job_details_query = f"""
                                                    SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                                    FROM (
                                                        SELECT COUNT(DISTINCT so_order_id) AS total_count
                                                        FROM sales_order
                                                        WHERE so_assigned_lab = {labId} AND so_order_status IN (4,5,6,7)
                                                        GROUP BY so_order_id
                                                    ) AS subquery
                                                    """
            cursor.execute(get_completed_job_details_query)
            completed_jobs = cursor.fetchone()

            get_total_job_details_query = f"""
                                                    SELECT IFNULL(SUM(subquery.total_count), 0) AS total_count
                                                    FROM (
                                                        SELECT COUNT(DISTINCT so_order_id) AS total_count
                                                        FROM sales_order
                                                        WHERE so_assigned_lab = {labId}
                                                        GROUP BY so_order_id
                                                    ) AS subquery
                                                    """

            cursor.execute(get_total_job_details_query)
            total_jobs = cursor.fetchone()

            return {
                "status": True,
                "new_jobs": new_jobs['total_count'],
                "active_jobs": active_jobs['total_count'],
                "completed_jobs": completed_jobs['total_count'],
                "total_jobs": total_jobs['total_count'],
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_lab_job_authenticity_card(saleId):
    try:
        with getConnection().cursor() as cursor:
            get_order_details_query = f"""
                            SELECT 
                                so.*,
                                SUM(so.so_unit_sale_price * so.so_purchase_quantity) AS total_cost,
                                SUM(so.so_product_total_cost) AS discount_cost,
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
                            WHERE so.so_sale_item_id = '{saleId}'
                        """

            cursor.execute(get_order_details_query)
            sale_item_details = cursor.fetchone()

            sale_item_details['so_linked_item'] = json.loads(sale_item_details['so_linked_item']) if sale_item_details[
                'so_linked_item'] else []
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