import pymysql
from django.db import connection
import datetime
import pytz

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def create_master_brand(brand_obj):
    try:
        with connection.cursor() as cursor:
            create_brand_query = f"""
                INSERT INTO brands (
                    brand_id, brand_name, category_id, brand_description, 
                    status, created_on, created_by, last_updated_on, last_updated_by
                ) 
                VALUES (
                    '{brand_obj.brand_id}', '{brand_obj.brand_name}',
                    '{brand_obj.category_id}', '{brand_obj.brand_description}',
                    '{brand_obj.status}', '{today}',
                    '{brand_obj.created_by}', '{today}',
                    '{brand_obj.last_updated_by}'
                )
            """

            cursor.execute(create_brand_query)
            return {
                "status": True,
                "message": "Brand added"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
