import json
from datetime import datetime


class Product:
    def __init__(self, values):
        (
            self.product_id, self.product_name, self.product_description, self.product_images,
            self.category_id, self.brand_id, self.material_id, self.frame_type_id, self.frame_shape_id,
            self.color_id, self.unit_id, self.origin, self.cost_price, self.sale_price, self.model_number,
            self.hsn,  self.power_attribute, self.franchise_sale_price, self.product_quantity, self.product_gst, self.status, self.discount, self.created_on, self.created_by, self.last_updated_on,
            self.last_updated_by, self.creator_name, self.updater_name, self.category_name, self.material_name,
            self.frame_type_name, self.shape_name, self.color_name, self.unit_name, self.brand_name, self.store_quantity
        ) = values

        # Parse product images from JSON string to a list
        self.product_images = json.loads(self.product_images) if self.product_images else []
        self.power_attribute = json.loads(self.power_attribute) if self.power_attribute else []

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_description': self.product_description,
            'product_images': self.product_images,
            'category_id': self.category_id,
            'brand_id': self.brand_id,
            'material_id': self.material_id,
            'frame_type_id': self.frame_type_id,
            'frame_shape_id': self.frame_shape_id,
            'color_id': self.color_id,
            'unit_id': self.unit_id,
            'origin': self.origin,
            'cost_price': self.cost_price,
            'sale_price': self.sale_price,
            'model_number': self.model_number,
            'hsn': self.hsn,
            'power_attribute': self.power_attribute,
            'franchise_sale_price': self.franchise_sale_price,
            'product_quantity': self.product_quantity,
            'product_gst': self.product_gst,
            'status': self.status,
            'discount': self.discount,
            'created_on': self.created_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.created_on, datetime) else None,
            'created_by': self.created_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on,
                                                                                                datetime) else None,
            'last_updated_by': self.last_updated_by,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,
            'category_name': self.category_name,
            'material_name': self.material_name,
            'frame_type_name': self.frame_type_name,
            'shape_name': self.shape_name,
            'color_name': self.color_name,
            'unit_name': self.unit_name,
            'brand_name': self.brand_name,
            'store_quantity': self.store_quantity,
        }


def get_products(response):
    product_list = []
    for values in response:
        product = Product(values)
        product_list.append(product.to_dict())
    return product_list
