import datetime
import pymysql
import pytz
from indolens.db_connection import connection

from indolens_admin.admin_models.admin_resp_model.store_inventory_resp_model import get_store_inventory

ist = pytz.timezone('Asia/Kolkata')
def getIndianTime():
    today = datetime.datetime.now(ist)
    return today

def get_all_products_for_own_store(store_id):
    try:
        with connection.cursor() as cursor:
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
                                    WHERE si.si_store_id = {store_id} AND si.si_store_type = 1 """

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
