import datetime
import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.sales_resp_model import get_sales_orders

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)

def get_all_orders(status, pay_status):
    status_conditions = {
        "All": "LIKE '%'",
        "New": "= 1",
        "Processing": "= 2",
        "Ready": "= 3",
        "Dispatched": "= 4",
        "Completed": "= 5",
        "Cancelled": "= 6",
    }
    status_condition = status_conditions[status]
    payment_status_values = {
        "All": "LIKE '%'",
        "Pending": "= 1",
        "Completed": "= 2"
    }
    payment_status_value = payment_status_values[pay_status]
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
                WHERE so.order_status {status_condition} AND so.payment_status {payment_status_value}
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