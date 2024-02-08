import datetime

import pymysql
import pytz
from django.db import connection

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
        with connection.cursor() as cursor:
            create_franchise_store_query = f"""
                                        INSERT INTO franchise_store (
                                            store_zip, store_name, store_display_name, store_phone, store_gst, store_email,
                                            store_city, store_state, store_lat, store_lng, store_address,
                                            status, created_by, created_on, last_updated_by, last_updated_on ) 
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
        with connection.cursor() as cursor:
            get_franchise_stores_query = f""" SELECT DISTINCT franchise_store.*, franchise_store_employees.name, franchise_store_employees.employee_id,
                                        creator.name, updater.name
                                        FROM franchise_store
                                        LEFT JOIN admin AS creator ON franchise_store.created_by = creator.admin_id
                                        LEFT JOIN admin AS updater ON franchise_store.last_updated_by = updater.admin_id
                                        LEFT JOIN franchise_store_employees ON franchise_store.store_id = franchise_store_employees.assigned_store_id AND franchise_store_employees.role = 1
                                        WHERE franchise_store.status {status_condition}
                                        ORDER BY franchise_store_employees.employee_id DESC
                                        """
            cursor.execute(get_franchise_stores_query)
            stores_data = cursor.fetchall()
            return {
                "status": True,
                "franchise_store": get_franchise_store(stores_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_store_by_id(fid):
    try:
        with connection.cursor() as cursor:
            get_franchise_stores_query = f""" SELECT franchise_store.*, franchise_store_employees.name, 
                                        franchise_store_employees.employee_id,
                                        creator.name, updater.name FROM franchise_store
                                        LEFT JOIN admin AS creator ON franchise_store.created_by = creator.admin_id
                                        LEFT JOIN admin AS updater ON franchise_store.last_updated_by = updater.admin_id
                                        LEFT JOIN franchise_store_employees ON 
                                        franchise_store.store_id = franchise_store_employees.assigned_store_id AND 
                                        franchise_store_employees.role = 1 WHERE franchise_store.store_id = '{fid}'
                                        GROUP BY franchise_store.store_id"""
            cursor.execute(get_franchise_stores_query)
            stores_data = cursor.fetchall()
            return {
                "status": True,
                "franchise_store": get_franchise_store(stores_data)
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def edit_franchise_store_by_id(franchise_obj):
    cleaned_str = franchise_obj.store_lat_lng.replace('Latitude: ', '').replace('Longitude: ', '')
    store_lat, store_lng = map(float, cleaned_str.split(', '))
    try:
        with connection.cursor() as cursor:
            update_franchise_store_query = f"""
                    UPDATE franchise_store
                    SET 
                        store_zip = '{franchise_obj.store_zip_code}',
                        store_name = '{franchise_obj.store_name}',
                        store_display_name = '{franchise_obj.store_display_name}',
                        store_phone = '{franchise_obj.store_phone}',
                        store_gst = '{franchise_obj.store_gstin}',
                        store_email = '{franchise_obj.store_email}',
                        store_city = '{franchise_obj.store_city}',
                        store_state = '{franchise_obj.store_state}',
                        store_lat = '{store_lat}',
                        store_lng = '{store_lng}',
                        store_address = '{franchise_obj.complete_address}',
                        last_updated_on = '{getIndianTime()}',
                        last_updated_by = {franchise_obj.last_updated_by}
                    WHERE store_id = {franchise_obj.store_id}
                """

            cursor.execute(update_franchise_store_query)
            connection.commit()  # Commit the transaction after executing the update query

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
        with connection.cursor() as cursor:
            update_franchise_store_query = f"""
                UPDATE franchise_store
                SET
                    status = {status}
                WHERE
                    store_id = {fid}
            """

            # Execute the update query using your cursor
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
        with connection.cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT si.*, ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name,
                                    os.store_name
                                    FROM store_inventory As si
                                    LEFT JOIN central_inventory AS ci ON ci.product_id = si.product_id
                                    LEFT JOIN admin AS creator ON si.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON si.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id
                                    LEFT JOIN franchise_store AS os ON os.store_id = '{store_id}' 
                                    WHERE si.store_id = {store_id} AND si.store_type = 2 """

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "products_list": get_store_inventory(product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_franchise_store_stats(ownStoreId):
    try:
        with connection.cursor() as cursor:
            employee_count_sql_query = f"""SELECT COUNT(*) FROM franchise_store_employees 
                                            WHERE assigned_store_id = {ownStoreId} AND status = 1"""
            cursor.execute(employee_count_sql_query)
            total_employee_count = cursor.fetchone()[0]

            customer_count_sql_query = f"""SELECT COUNT(*) FROM customers WHERE created_by_store_id = {ownStoreId} AND 
                                                created_by_store_type = 2 """
            cursor.execute(customer_count_sql_query)
            total_customer_count = cursor.fetchone()[0]

            return {
                       "status": True,
                       "total_employee_count": total_employee_count,
                       "total_customer_count": total_customer_count
                   }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
