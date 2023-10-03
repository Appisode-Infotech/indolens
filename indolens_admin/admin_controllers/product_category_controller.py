import pymysql
from django.db import connection
import datetime
import pytz

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def add_product_category(product_cat_obj):
    try:
        with connection.cursor() as cursor:
            create_category_query = f"""
                INSERT INTO product_categories (
                    category_id, category_name, category_prefix, category_description, 
                    status, created_on, created_by, last_updated_on, last_updated_by
                ) 
                VALUES (
                    '{product_cat_obj.category_id}', '{product_cat_obj.category_name}',
                    '{product_cat_obj.category_prefix}', '{product_cat_obj.category_description}',
                    '{product_cat_obj.status}', '{today}',
                    '{product_cat_obj.created_by}', '{today}',
                    '{product_cat_obj.last_updated_by}'
                )
            """

            cursor.execute(create_category_query)
            return {
                "status": True,
                "message": "Product category added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)},

# def manage_central_inventory_category():
#     try:
#         with connection.cursor() as cursor:
#             get_product_category_query = f""" SELECT * FROM product_categories """
#             cursor.execute(get_product_category_query)
#             stores_data = cursor.fetchall()
#             return {
#                 "status": True,
#                 "product_category": get_own_store(stores_data)
#             }, 200
#
#     except pymysql.Error as e:
#         return {"status": False, "message": str(e)}, 301
#     except Exception as e:
#         return {"status": False, "message": str(e)}, 301
