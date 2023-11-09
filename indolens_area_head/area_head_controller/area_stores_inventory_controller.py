import datetime
import json

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_controllers.master_category_controller import get_all_central_inventory_category
from indolens_admin.admin_models.admin_resp_model.central_inventory_product_resp_model import get_products
from indolens_own_store.own_store_model.response_model.store_inventory_product_resp_model import \
    get_store_inventory_stocks

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_all_out_of_stock_products_for_stores(quantity, store_id):
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
                                    LEFT JOIN own_store AS os ON si.store_id = os.store_id
                                    WHERE si.product_quantity <= {quantity} AND si.store_id IN {tuple(store_id)} AND si.store_type = 1 """

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "stocks_list": get_store_inventory_stocks(product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
