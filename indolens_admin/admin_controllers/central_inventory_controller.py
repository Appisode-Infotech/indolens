import datetime
import json

import pymysql
import pytz
from PIL import ImageFont
from django.db import connection

from indolens_admin.admin_controllers.master_category_controller import get_all_central_inventory_category
from indolens_admin.admin_models.admin_resp_model.central_inventory_product_resp_model import get_products
from indolens_admin.admin_models.admin_resp_model.master_brand_resp_model import get_brands
from indolens_admin.admin_models.admin_resp_model.master_category_resp_model import get_product_categories
from indolens_admin.admin_models.admin_resp_model.master_color_resp_model import get_product_colors
from indolens_admin.admin_models.admin_resp_model.master_frame_type_resp_model import get_frame_types
from indolens_admin.admin_models.admin_resp_model.master_material_resp_model import get_product_materials
from indolens_admin.admin_models.admin_resp_model.master_shapes_resp_model import get_frame_shapes
from indolens_admin.admin_models.admin_resp_model.master_units_resp_model import get_master_units
from indolens_admin.admin_models.admin_resp_model.product_request_list_resp_model import get_request_product_list
from indolens_admin.admin_models.admin_resp_model.stockMovementInvoice_resp_model import get_stock_movement_invoice
from indolens_admin.admin_models.admin_resp_model.store_inventory_product_resp_model import get_store_stocks
from indolens_own_store.own_store_model.response_model.store_inventory_product_resp_model import \
    get_store_inventory_stocks

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
            get_product_brand_query = f""" SELECT br.* , creator.name, updater.name
                           FROM brands AS br 
                           LEFT JOIN admin AS creator ON br.created_by = creator.admin_id
                           LEFT JOIN admin AS updater ON br.last_updated_by = updater.admin_id
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


def add_central_inventory_products(product_obj, file, power_attributes):
    power_attributes_json = json.dumps(power_attributes)
    frame_type_id_value = product_obj.frame_type_id if product_obj.frame_type_id != '' else 0
    frame_shape_id_value = product_obj.frame_shape_id if product_obj.frame_shape_id != '' else 0
    try:
        with connection.cursor() as cursor:
            add_product_query = f""" INSERT INTO central_inventory 
                                                (product_name, product_description, product_images, 
                                                category_id, brand_id, material_id, frame_type_id, frame_shape_id, 
                                                color_id, unit_id, origin, cost_price, sale_price, model_number, hsn, 
                                                created_on, created_by, last_updated_on, last_updated_by, 
                                                product_quantity, product_gst, discount, franchise_sale_price, power_attribute, status) 
                                                VALUES ('{product_obj.product_title}','{product_obj.product_description}',
                                                '{json.dumps(file.product_img)}','{product_obj.category_id}',
                                                '{product_obj.brand_id}','{product_obj.material_id}',
                                                '{frame_type_id_value}','{frame_shape_id_value}',
                                                '{product_obj.color_id}','{product_obj.unit_id}','{product_obj.origin}',
                                                '{product_obj.cost_price}','{product_obj.sale_price}', 
                                                '{product_obj.model_number}', '{product_obj.hsn_number}',
                                                '{today}','{product_obj.created_by}','{today}',
                                                '{product_obj.last_updated_by}', '{product_obj.product_quantity}', 
                                                '{product_obj.product_gstin}', {product_obj.discount}, 
                                                {product_obj.franchise_sale_price}, '{power_attributes_json}', 0) """

            cursor.execute(add_product_query)

            import os
            import qrcode
            from PIL import Image, ImageDraw, ImageOps
            from django.conf import settings

            productId = cursor.lastrowid

            logo_path = "media/logo/logo.png"
            logo = Image.open(logo_path)

            # Convert the logo to RGBA mode
            logo = logo.convert("RGBA")

            # Create a white background image with the same size as the logo
            background = Image.new("RGBA", logo.size, (255, 255, 255, 255))

            # Composite the logo onto the white background
            logo_with_white_background = Image.alpha_composite(background, logo)

            basewidth = 100

            # adjust image size
            wpercent = basewidth / float(logo_with_white_background.size[0])
            hsize = int(float(logo_with_white_background.size[1]) * float(wpercent))

            logo_resized = logo_with_white_background.resize(
                (basewidth, hsize), Image.ANTIALIAS)

            QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            QRcode.add_data(productId)
            QRcode.make()
            QRcolor = '#000000'

            # adding color to QR code
            QRimg = QRcode.make_image(
                fill_color=QRcolor, back_color="white").convert('RGB')

            # set size of QR code
            pos = ((QRimg.size[0] - logo_resized.size[0]) // 2,
                   (QRimg.size[1] - logo_resized.size[1]) // 2)
            QRimg.paste(logo_resized, pos, mask=logo_resized)

            # Annotate the QR image with productId below the QR code
            draw = ImageDraw.Draw(QRimg)
            font = ImageFont.load_default()
            text = f"Product ID: {productId}"
            text_width, text_height = draw.textsize(text, font)
            text_position = (
            (QRimg.width - text_width) // 2, QRimg.height - text_height - 10)
            draw.text(text_position, text, fill="#000000", font=font)

            # Construct the path to save the image in the media directory
            media_dir = os.path.join(settings.MEDIA_ROOT, 'product_qr_codes')
            os.makedirs(media_dir, exist_ok=True)
            image_path = os.path.join(media_dir, f"{productId}.png")

            QRimg.save(image_path, format='JPEG', quality=100)

            image_url = f"product_qr_codes/{productId}.png"
            update_qr_sql = f"UPDATE central_inventory SET product_qr_code = '{image_url}' WHERE product_id = {productId}"
            cursor.execute(update_qr_sql)

            return {
                "status": True,
                "productId": productId
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def update_central_inventory_products(product_obj, productId, power_attribute):
    power_attributes_json = json.dumps(power_attribute)
    print(power_attributes_json)
    try:
        with connection.cursor() as cursor:
            update_product_query = f"""
                UPDATE central_inventory 
                SET product_name = '{product_obj.product_title}',
                    product_description = '{product_obj.product_description}',
                    category_id = '{product_obj.category_id}',
                    brand_id = '{product_obj.brand_id}',
                    material_id = '{product_obj.material_id}',
                    frame_type_id = '{product_obj.frame_type_id}',
                    frame_shape_id = '{product_obj.frame_shape_id}',
                    color_id = '{product_obj.color_id}',
                    unit_id = '{product_obj.unit_id}',
                    origin = '{product_obj.origin}',
                    cost_price = '{product_obj.cost_price}',
                    sale_price = '{product_obj.sale_price}',
                    model_number = '{product_obj.model_number}',
                    hsn = '{product_obj.hsn_number}',
                    last_updated_on = '{today}',
                    last_updated_by = '{product_obj.last_updated_by}',
                    product_quantity = '{product_obj.product_quantity}',
                    product_gst = '{product_obj.product_gstin}',
                    discount = '{product_obj.discount}',
                    power_attribute = '{power_attributes_json}'
                WHERE product_id = '{productId}'
            """

            cursor.execute(update_product_query)
            productId = cursor.lastrowid
            return {
                "status": True,
                "productId": productId
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def restock_central_inventory_products(productId, product_quantity):
    try:
        with connection.cursor() as cursor:
            restock_product_query = f"""
                UPDATE central_inventory 
                SET product_quantity = product_quantity + {product_quantity}
                WHERE product_id = '{productId}'
            """

            cursor.execute(restock_product_query)
            return {
                "status": True
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_central_inventory_products(status):
    try:
        status_conditions = {
            "All": "LIKE '%'",
            "Active": "= 1",
            "Inactive": "= 0"
        }
        status_condition = status_conditions[status]
        with connection.cursor() as cursor:
            get_all_product_query = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name
                                    FROM central_inventory As ci
                                    LEFT JOIN admin AS creator ON ci.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON ci.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id
                                    WHERE ci.status {status_condition} ORDER BY ci.product_id DESC """

            cursor.execute(get_all_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "product_list": get_products(product_list),
                "categoriesList": get_all_central_inventory_category()[0]['product_category']
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

def get_central_inventory_products_to_move(status):
    try:
        status_conditions = {
            "All": "LIKE '%'",
            "Active": "= 1",
            "Inactive": "= 0"
        }
        status_condition = status_conditions[status]
        with connection.cursor() as cursor:
            get_all_product_query = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name
                                    FROM central_inventory As ci
                                    LEFT JOIN admin AS creator ON ci.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON ci.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id
                                    WHERE ci.category_id <> 2 AND ci.category_id <> 3 AND ci.status {status_condition} """

            cursor.execute(get_all_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "product_list": get_products(product_list),
                "categoriesList": get_all_central_inventory_category()[0]['product_category']
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_central_inventory_product_single(productId):
    with connection.cursor() as cursor:
        try:
            get_all_product_query = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                            ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name
                                            FROM central_inventory As ci
                                            LEFT JOIN admin AS creator ON ci.created_by = creator.admin_id
                                            LEFT JOIN admin AS updater ON ci.last_updated_by = updater.admin_id
                                            LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                            LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                            LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                            LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                            LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                            LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                            LEFT JOIN brands AS b ON ci.brand_id = b.brand_id
                                            WHERE ci.product_id= {productId} """
            cursor.execute(get_all_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "product_data": get_products(product_list)[0],
            }, 200
        except pymysql.Error as e:
            return {"status": False, "message": str(e)}, 301
        except Exception as e:
            return {"status": False, "message": str(e)}, 301


def get_all_out_of_stock_central_inventory_products(quantity):
    try:
        with connection.cursor() as cursor:
            get_all_product_query = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name
                                    FROM central_inventory As ci
                                    LEFT JOIN admin AS creator ON ci.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON ci.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id
                                    WHERE ci.product_quantity <= '{quantity}'
                                    ORDER BY ci.product_id DESC"""

            cursor.execute(get_all_product_query)
            stocks_list = cursor.fetchall()
            return {
                "status": True,
                "stocks_list": get_products(stocks_list),
                "categories_list": get_all_central_inventory_category()[0]['product_category']
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e), "stocks_list": []}, 301
    except Exception as e:
        return {"status": False, "message": str(e), "stocks_list": []}, 301


def get_all_out_of_stock_products_for_store(quantity):
    try:
        with connection.cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT si.*, ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name,
                                    CASE
                                        WHEN si.store_type = 1 THEN os.store_name
                                        ELSE fstore.store_name
                                    END AS store_name
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
                                    LEFT JOIN own_store os ON si.store_id = os.store_id AND si.store_type = 1
                                    LEFT JOIN franchise_store fstore ON si.store_id = fstore.store_id AND si.store_type = 2;
                                    WHERE si.product_quantity <= '{quantity}'"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "stocks_list": get_store_stocks(product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_moved_stocks_list(status):
    try:
        with connection.cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT rp.*, ci.*, creator.name, updater.name, pc.category_name, 
                                    pm.material_name, ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name,
                                    CASE
                                        WHEN rp.store_type = 1 THEN os.store_name
                                        ELSE fstore.store_name
                                    END AS store_name,
                                    from_store.store_name
                                    FROM request_products As rp
                                    LEFT JOIN central_inventory AS ci ON ci.product_id = rp.product_id
                                    LEFT JOIN admin AS creator ON rp.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON rp.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id 
                                    LEFT JOIN own_store os ON rp.store_id = os.store_id AND rp.store_type = 1
                                    LEFT JOIN own_store AS from_store ON rp.request_to_store_id = from_store.store_id
                                    LEFT JOIN franchise_store fstore ON rp.store_id = fstore.store_id AND rp.store_type = 2
                                    WHERE rp.request_status LIKE '{status}' """

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "stocks_request_list": get_request_product_list(product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_all_stock_requests(status):
    try:
        with connection.cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT rp.*, ci.*, creator.name, updater.name, pc.category_name, 
                                    pm.material_name, ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name,
                                    CASE
                                        WHEN rp.store_type = 1 THEN os.store_name
                                        ELSE fstore.store_name
                                    END AS store_name,
                                    from_store.store_name
                                    FROM request_products As rp
                                    LEFT JOIN central_inventory AS ci ON ci.product_id = rp.product_id
                                    LEFT JOIN admin AS creator ON rp.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON rp.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id 
                                    LEFT JOIN own_store os ON rp.store_id = os.store_id AND rp.store_type = 1
                                    LEFT JOIN own_store AS from_store ON rp.request_to_store_id = from_store.store_id
                                    LEFT JOIN franchise_store fstore ON rp.store_id = fstore.store_id AND rp.store_type = 2
                                    WHERE rp.request_status LIKE '{status}' AND is_requested = 1
                                    ORDER BY rp.request_products_id DESC"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchall()
            return {
                "status": True,
                "stocks_request_list": get_request_product_list(product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_stock_requests_by_id(requestId):
    try:
        with connection.cursor() as cursor:
            get_all_out_of_stock_product_query = f""" SELECT rp.*, ci.*, creator.name, updater.name, pc.category_name, 
                                    pm.material_name, ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name,
                                    CASE
                                        WHEN rp.store_type = 1 THEN os.store_name
                                        ELSE fstore.store_name
                                    END AS store_name,
                                    CASE
                                        WHEN rp.store_type = 1 THEN os.store_email
                                        ELSE fstore.store_email
                                    END AS store_email,
                                    CASE
                                        WHEN rp.store_type = 1 THEN os.store_phone
                                        ELSE fstore.store_phone
                                    END AS store_phone,
                                    CASE
                                        WHEN rp.store_type = 1 THEN os.store_address
                                        ELSE fstore.store_address
                                    END AS store_address,
                                    from_store.store_name,
                                    (SELECT SUM(product_quantity * unit_cost) AS billing_amount FROM request_products 
                                    WHERE request_products_id = {requestId})
                                    FROM request_products As rp
                                    LEFT JOIN central_inventory AS ci ON ci.product_id = rp.product_id
                                    LEFT JOIN admin AS creator ON rp.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON rp.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id 
                                    LEFT JOIN own_store os ON rp.store_id = os.store_id AND rp.store_type = 1
                                    LEFT JOIN own_store AS from_store ON rp.request_to_store_id = from_store.store_id
                                    LEFT JOIN franchise_store fstore ON rp.store_id = fstore.store_id AND rp.store_type = 2
                                    WHERE rp.request_status = 1 AND rp.request_products_id = {requestId}
                                    ORDER BY rp.request_products_id DESC"""

            cursor.execute(get_all_out_of_stock_product_query)
            product_list = cursor.fetchone()
            return {
                "status": True,
                "stocks_request_list": get_stock_movement_invoice(product_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def change_stock_request_status(requestId, status, updator):
    try:
        with connection.cursor() as cursor:
            fetch_req_product_query = f"""SELECT * FROM request_products 
                        WHERE request_products_id = '{requestId}'"""
            cursor.execute(fetch_req_product_query)
            product_details = cursor.fetchone()
            quantity = product_details[4]
            dispenser_inventory = product_details[9]

            # requested products from centre inventory
            if dispenser_inventory == 0:
                fetch_inventory_product_query = f"""SELECT product_quantity FROM central_inventory 
                            WHERE product_id = {product_details[3]} """
                cursor.execute(fetch_inventory_product_query)
                available_quantity = cursor.fetchone()[0]

                if status == 1:
                    if available_quantity >= quantity:
                        update_stock_request_query = f"""UPDATE request_products SET request_status = '{status}', 
                        last_updated_on = '{today}', last_updated_by = '{updator}', delivery_status = 1
                        WHERE request_products_id = '{requestId}' """
                        cursor.execute(update_stock_request_query)

                        update_central_Inventory = f"""UPDATE central_inventory SET product_quantity = product_quantity - {quantity} 
                                                                            WHERE product_id = {product_details[3]}"""
                        cursor.execute(update_central_Inventory)



                        return {
                            "status": True,
                            "message": "Status Changed"
                        }, 200

                    else:
                        return {
                            "status": False,
                            "message": f"The requested quantity is {quantity} and available quantity is {available_quantity} in inventory"
                        }, 200
                else:
                    update_stock_request_query = f"""UPDATE request_products SET request_status = '{status}',
                                        last_updated_on = '{today}', last_updated_by = '{updator}', delivery_status = 3
                                        WHERE request_products_id = '{requestId}' """
                    cursor.execute(update_stock_request_query)
                    return {
                        "status": True,
                        "message": "Status Changed"
                    }, 200


            else:
                fetch_inventory_product_query = f"""SELECT product_quantity FROM store_inventory 
                                            WHERE product_id = {product_details[3]} AND store_id = {dispenser_inventory} 
                                            AND store_type = 1 """
                cursor.execute(fetch_inventory_product_query)
                available_quantity = cursor.fetchone()[0]

                if status == 1:
                    if available_quantity >= quantity:
                        update_stock_request_query = f"""UPDATE request_products SET request_status = '{status}',
                                        last_updated_on = '{today}', last_updated_by = '{updator}', delivery_status = 1
                                        WHERE request_products_id = '{requestId}' """
                        cursor.execute(update_stock_request_query)

                        update_central_Inventory = f"""UPDATE store_inventory SET 
                                                        product_quantity = product_quantity - {quantity} 
                                                        WHERE product_id = {product_details[3]} AND 
                                                        store_id = {dispenser_inventory} AND store_type = 1"""
                        cursor.execute(update_central_Inventory)

                        return {
                            "status": True,
                            "message": "Status Changed"
                        }, 200

                    else:
                        print("yes7")
                        return {
                            "status": False,
                            "message": f"The requested quantity is {quantity} and available quantity is {available_quantity} in inventory"
                        }, 200
                else:
                    update_stock_request_query = f"""UPDATE request_products SET request_status = '{status}'
                                                        last_updated_on = '{today}', last_updated_by = '{updator}', delivery_status = 3
                                                        WHERE request_products_id = '{requestId}' """
                    cursor.execute(update_stock_request_query)
                    return {
                        "status": True,
                        "message": "Status Changed"
                    }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def change_product_status(productId, status):
    try:
        with connection.cursor() as cursor:
            update_stock_request_query = f"""UPDATE central_inventory SET status = '{status}' 
            WHERE product_id = '{productId}' """
            cursor.execute(update_stock_request_query)
        return {
            "status": True,
            "message": "updated stock status"
        }


    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def create_store_stock_request(stock_obj, store_id):
    try:
        with connection.cursor() as cursor:
            stock_req_query = """INSERT INTO request_products ( 
                               store_id, 
                               store_type, 
                               product_id, 
                               product_quantity, 
                               request_status, 
                               delivery_status, 
                               is_requested,
                               request_to_store_id,
                               payment_status,
                               created_on, 
                               created_by, 
                               last_updated_on, 
                               last_updated_by,
                               comment
                           ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            cursor.execute(stock_req_query, (
                store_id, stock_obj.store_type, stock_obj.product_id, stock_obj.product_quantity,
                1, 1, 0, 0, 0, today, stock_obj.created_by, today, stock_obj.created_by, stock_obj.comments))

            update_central_Inventory = f"""UPDATE central_inventory SET product_quantity = product_quantity - {stock_obj.product_quantity} 
                                                                                    WHERE product_id = {stock_obj.product_id}"""
            cursor.execute(update_central_Inventory)

            return {
                "status": True,
                "message": "success"
            }, 200

    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301


def get_central_inventory_lens(store_id):
    try:
        with connection.cursor() as cursor:
            get_all_lens_from_central_ionventory = f""" SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                    ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name
                                    FROM central_inventory As ci
                                    LEFT JOIN admin AS creator ON ci.created_by = creator.admin_id
                                    LEFT JOIN admin AS updater ON ci.last_updated_by = updater.admin_id
                                    LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                    LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                    LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                    LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                    LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                    LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                    LEFT JOIN brands AS b ON ci.brand_id = b.brand_id  
                                    WHERE ci.category_id = 2 AND ci.status = 1 """

            cursor.execute(get_all_lens_from_central_ionventory)
            lens_list = cursor.fetchall()

            get_all_contact_lens_from_central_inventory = f""" 
                                                SELECT ci.*, creator.name, updater.name, pc.category_name, pm.material_name,
                                                ft.frame_type_name, fs.shape_name,c.color_name, u.unit_name, b.brand_name
                                                FROM central_inventory As ci
                                                LEFT JOIN admin AS creator ON ci.created_by = creator.admin_id
                                                LEFT JOIN admin AS updater ON ci.last_updated_by = updater.admin_id
                                                LEFT JOIN product_categories AS pc ON ci.category_id = pc.category_id
                                                LEFT JOIN product_materials AS pm ON ci.material_id = pm.material_id
                                                LEFT JOIN frame_types AS ft ON ci.frame_type_id = ft.frame_id
                                                LEFT JOIN frame_shapes AS fs ON ci.frame_shape_id = fs.shape_id
                                                LEFT JOIN product_colors AS c ON ci.color_id = c.color_id
                                                LEFT JOIN units AS u ON ci.unit_id = u.unit_id
                                                LEFT JOIN brands AS b ON ci.brand_id = b.brand_id  
                                                WHERE ci.category_id = 3 AND ci.status = 1 """
            cursor.execute(get_all_contact_lens_from_central_inventory)
            contact_lens_list = cursor.fetchall()
            return {
                "status": True,
                "lens_list": get_products(lens_list),
                "contact_lens_list": get_products(contact_lens_list)
            }, 200
    except pymysql.Error as e:
        return {"status": False, "message": str(e)}, 301
    except Exception as e:
        return {"status": False, "message": str(e)}, 301

