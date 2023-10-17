import datetime

import pymysql
import pytz
from django.db import connection

from indolens_admin.admin_models.admin_resp_model.master_brand_resp_model import get_brands
from indolens_admin.admin_models.admin_resp_model.master_category_resp_model import get_product_categories
from indolens_admin.admin_models.admin_resp_model.master_color_resp_model import get_product_colors
from indolens_admin.admin_models.admin_resp_model.master_frame_type_resp_model import get_frame_types
from indolens_admin.admin_models.admin_resp_model.master_material_resp_model import get_product_materials
from indolens_admin.admin_models.admin_resp_model.master_shapes_resp_model import get_frame_shapes
from indolens_admin.admin_models.admin_resp_model.master_units_resp_model import get_master_units

ist = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(ist)


def get_all_active_types():
    try:
        with connection.cursor() as cursor:
            get_product_category_query = f""" SELECT pc.* , creator.name, updater.name
                       FROM product_categories AS pc 
                       LEFT JOIN admin AS creator ON pc.created_by = creator.admin_id
                       LEFT JOIN admin AS updater ON pc.last_updated_by = updater.admin_id
                       WHERE pc.status = 1
                       """
            get_product_brand_query = f""" SELECT br.* , creator.name, updater.name, category.category_name
                       FROM brands AS br 
                       LEFT JOIN admin AS creator ON br.created_by = creator.admin_id
                       LEFT JOIN admin AS updater ON br.last_updated_by = updater.admin_id
                       LEFT JOIN product_categories AS category ON br.category_id = category.category_id
                       WHERE br.status = 1
                       """
            get_material_query = f""" SELECT pm.* , creator.name, updater.name
                        FROM product_materials AS pm
                        LEFT JOIN admin AS creator ON pm.created_by = creator.admin_id
                        LEFT JOIN admin AS updater ON pm.last_updated_by = updater.admin_id
                        WHERE pm.status = 1
                        """
            get_frame_types_query = f""" SELECT ft.* , creator.name, updater.name
                        FROM frame_types AS ft
                        LEFT JOIN admin AS creator ON ft.created_by = creator.admin_id
                        LEFT JOIN admin AS updater ON ft.last_updated_by = updater.admin_id
                        WHERE ft.status = 1 
                        """
            get_product_shape_query = f""" SELECT fs.* , creator.name, updater.name
                       FROM frame_shapes AS fs 
                       LEFT JOIN admin AS creator ON fs.created_by = creator.admin_id
                       LEFT JOIN admin AS updater ON fs.last_updated_by = updater.admin_id
                       WHERE fs.status = 1
                       """
            get_frame_color_query = f""" SELECT pc.* , creator.name, updater.name
                        FROM product_colors AS pc
                        LEFT JOIN admin AS creator ON pc.created_by = creator.admin_id
                        LEFT JOIN admin AS updater ON pc.last_updated_by = updater.admin_id
                        WHERE pc.status = 1
                        """
            get_units_query = f""" SELECT u.*, creator.name, updater.name 
                                                       FROM units AS u
                                                        LEFT JOIN admin AS creator ON u.created_by = creator.admin_id
                                                        LEFT JOIN admin AS updater ON u.last_updated_by = updater.admin_id
                                                        WHERE u.status = 1
                                                        """
            cursor.execute(get_product_category_query)
            product_categories = get_product_categories(cursor.fetchall())
            cursor.execute(get_product_brand_query)
            product_brands = get_brands(cursor.fetchall())
            cursor.execute(get_material_query)
            product_materials = get_product_materials(cursor.fetchall())
            cursor.execute(get_frame_types_query)
            frame_types = get_frame_types(cursor.fetchall())
            cursor.execute(get_product_shape_query)
            frame_shapes = get_frame_shapes(cursor.fetchall())
            cursor.execute(get_frame_color_query)
            colors = get_product_colors(cursor.fetchall())
            cursor.execute(get_units_query)
            master_units = get_master_units(cursor.fetchall())
            return {
                       "status": True,
                       "product_categories": product_categories,
                       "product_brands": product_brands,
                       "product_materials": product_materials,
                       "frame_types": frame_types,
                       "frame_shapes": frame_shapes,
                       "colors": colors,
                       "master_units": master_units,
                   }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301
