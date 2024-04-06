import datetime

import pymysql
import pytz
from indolens.db_connection import getConnection

from indolens_admin.admin_models.admin_resp_model.franchise_store_resp_model import get_franchise_store
from indolens_admin.admin_models.admin_resp_model.store_inventory_resp_model import get_store_inventory

ist = pytz.timezone('Asia/Kolkata')


def getIndianTime():
    today = datetime.datetime.now(ist)
    return today


def create_franchise_store(franchise_obj):
    cleaned_str = franchise_obj.store_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    store_lat, store_lng = map(float, cleaned_str.split(', '))
    try:
        with getConnection().cursor() as cursor:
            create_franchise_store_query = f"""
                INSERT INTO franchise_store (
                    fs_store_zip, fs_store_name, fs_store_display_name, fs_store_phone, fs_store_gst, fs_store_email,
                    fs_store_city, fs_store_state, fs_store_lat, fs_store_lng, fs_store_address,
                    fs_status, fs_created_by, fs_created_on, fs_last_updated_by, fs_last_updated_on ) 
                VALUES ('{franchise_obj.store_zip_code}', '{franchise_obj.store_name}', 
                        '{franchise_obj.store_display_name}', '{franchise_obj.store_phone}', 
                        '{franchise_obj.store_gstin}', '{franchise_obj.store_email}', 
                        '{franchise_obj.store_city}', '{franchise_obj.store_state}', '{store_lat}',
                        '{store_lng}', '{franchise_obj.complete_address}', 1, {franchise_obj.created_by}, 
                        '{getIndianTime()}', {franchise_obj.last_updated_by}, '{getIndianTime()}')"""

            cursor.execute(create_franchise_store_query)
            storeId = cursor.lastrowid
            return {
                "status": True,
                "message": "franchise store added",
                "storeId": storeId
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_franchise_stores(status):
    status_conditions = {
        "All": "LIKE '%'",
        "Active": "= 1",
        "Inactive": "= 0"
    }
    status_condition = status_conditions[status]
    try:
        with getConnection().cursor() as cursor:
            get_franchise_stores_query = f""" SELECT DISTINCT franchise_store.*, franchise_store_employees.fse_name, franchise_store_employees.fse_employee_id,
                                        creator.admin_name, updater.admin_name
                                        FROM franchise_store
                                        LEFT JOIN admin AS creator ON franchise_store.fs_created_by = creator.admin_admin_id
                                        LEFT JOIN admin AS updater ON franchise_store.fs_last_updated_by = updater.admin_admin_id
                                        LEFT JOIN franchise_store_employees ON franchise_store.fs_store_id = franchise_store_employees.fse_assigned_store_id AND franchise_store_employees.fse_role = 1
                                        WHERE franchise_store.fs_status {status_condition}
                                        ORDER BY franchise_store.fs_store_id DESC
                                        """
            cursor.execute(get_franchise_stores_query)
            stores_data = cursor.fetchall()
            return {
                "status": True,
                "franchise_store": stores_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_stores_count():
    try:
        with getConnection().cursor() as cursor:
            get_franchise_stores_query = f""" SELECT count(*)
                                        FROM franchise_store"""
            cursor.execute(get_franchise_stores_query)
            stores_data = cursor.fetchone()
            return {
                "status": True,
                "franchise_store": stores_data['count(*)']
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_store_by_id(fid):
    try:
        with getConnection().cursor() as cursor:
            get_franchise_stores_query = f""" SELECT franchise_store.*, franchise_store_employees.fse_name, 
                                        franchise_store_employees.fse_employee_id,
                                        creator.admin_name AS creator, updater.admin_name AS Updater FROM franchise_store
                                        LEFT JOIN admin AS creator ON franchise_store.fs_created_by = creator.admin_admin_id
                                        LEFT JOIN admin AS updater ON franchise_store.fs_last_updated_by = updater.admin_admin_id
                                        LEFT JOIN franchise_store_employees ON 
                                        franchise_store.fs_store_id = franchise_store_employees.fse_assigned_store_id AND 
                                        franchise_store_employees.fse_role = 1 WHERE franchise_store.fs_store_id = '{fid}'
                                        GROUP BY franchise_store.fs_store_id"""
            cursor.execute(get_franchise_stores_query)
            stores_data = cursor.fetchone()
            return {
                "status": True,
                "franchise_store": stores_data
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_franchise_store_by_id(franchise_obj):
    cleaned_str = franchise_obj.store_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    store_lat, store_lng = map(float, cleaned_str.split(', '))
    try:
        with getConnection().cursor() as cursor:
            update_franchise_store_query = f"""
                UPDATE franchise_store
                SET 
                    fs_store_zip = '{franchise_obj.store_zip_code}',
                    fs_store_name = '{franchise_obj.store_name}',
                    fs_store_display_name = '{franchise_obj.store_display_name}',
                    fs_store_phone = '{franchise_obj.store_phone}',
                    fs_store_gst = '{franchise_obj.store_gstin}',
                    fs_store_email = '{franchise_obj.store_email}',
                    fs_store_city = '{franchise_obj.store_city}',
                    fs_store_state = '{franchise_obj.store_state}',
                    fs_store_lat = '{store_lat}',
                    fs_store_lng = '{store_lng}',
                    fs_store_address = '{franchise_obj.complete_address}',
                    fs_last_updated_on = '{getIndianTime()}',
                    fs_last_updated_by = {franchise_obj.last_updated_by}
                WHERE fs_store_id = {franchise_obj.store_id}
            """
            cursor.execute(update_franchise_store_query)

            return {
                "status": True,
                "message": "Own store updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def enable_disable_franchise_store(fid, status):
    try:
        with getConnection().cursor() as cursor:
            update_franchise_store_query = f"""
                UPDATE franchise_store
                SET
                    fs_status = {status}
                WHERE
                    fs_store_id = {fid}
            """

            cursor.execute(update_franchise_store_query)

            return {
                "status": True,
                "message": "Franchise Store updated"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_products_for_franchise_store(store_id):
    try:
        with getConnection().cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT si.*, ci.*, creator.admin_name, updater.admin_name, 
                                                pc.pc_category_name, pm.pm_material_name,
                                                ft.ftype_name, fs.fshape_name,c.pcol_color_name, u.unit_name, b.brand_name,
                                                os.os_store_name
                                                FROM store_inventory As si
                                                LEFT JOIN central_inventory AS ci ON ci.ci_product_id = si.si_product_id
                                                LEFT JOIN admin AS creator ON si.si_created_by = creator.admin_admin_id
                                                LEFT JOIN admin AS updater ON si.si_last_updated_by = updater.admin_admin_id
                                                LEFT JOIN product_categories AS pc ON ci.ci_category_id = pc.pc_category_id
                                                LEFT JOIN product_materials AS pm ON ci.ci_material_id = pm.pm_material_id
                                                LEFT JOIN frame_types AS ft ON ci.ci_frame_type_id = ft.ftype_frame_id
                                                LEFT JOIN frame_shapes AS fs ON ci.ci_frame_shape_id = fs.fshape_shape_id
                                                LEFT JOIN product_colors AS c ON ci.ci_color_id = c.pcol_color_id
                                                LEFT JOIN units AS u ON ci.ci_unit_id = u.unit_unit_id
                                                LEFT JOIN brands AS b ON ci.ci_brand_id = b.brand_brand_id
                                                LEFT JOIN own_store AS os ON os.os_store_id = '{store_id}' 
                                                WHERE si.si_store_id = {store_id} AND si.si_store_type = 2 """

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "products_list": product_list
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_store_stats(ownStoreId):
    try:
        with getConnection().cursor() as cursor:
            employee_count_sql_query = f"""SELECT COUNT(*) FROM franchise_store_employees 
                                            WHERE fse_assigned_store_id = {ownStoreId} AND fse_status = 1"""
            cursor.execute(employee_count_sql_query)
            total_employee_count = cursor.fetchone()['COUNT(*)']

            customer_count_sql_query = f"""SELECT COUNT(*) FROM customers WHERE customer_created_by_store_id = {ownStoreId} AND 
                                                customer_created_by_store_type = 2 """
            cursor.execute(customer_count_sql_query)
            total_customer_count = cursor.fetchone()['COUNT(*)']

            return {
                "status": True,
                "total_employee_count": total_employee_count,
                "total_customer_count": total_customer_count
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
