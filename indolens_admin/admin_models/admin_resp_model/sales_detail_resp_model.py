from datetime import datetime
import json


class SalesOrder:
    def __init__(self, values):
        (
            self.sale_item_id, self.order_id, self.product_id, self.hsn,
            self.unit_sale_price, self.unit_type, self.purchase_quantity,
            self.product_total_cost, self.discount_percentage,
            self.is_discount_applied, self.power_attribute, self.assigned_lab,
            self.customer_id, self.order_status, self.payment_status,
            self.delivery_status, self.payment_mode, self.amount_paid,
            self.estimated_delivery_date, self.linked_item, self.sales_note, self.created_by_store,
            self.created_by_store_type, self.created_by, self.created_on,
            self.updated_by, self.updated_on, self.total_cost, self.discount_cost,
            self.store_name, self.creator_name,
            self.updater_name,
            # Customer Fields
            self.customer_id, self.customer_name, self.gender, self.age, self.phone,
            self.email, self.language, self.city, self.address,
            self.created_by_employee_id, self.created_by_store_id,
            self.cust_created_by_store_type, self.created_on_customer,
            self.updated_by_employee_id, self.updated_by_store_id,
            self.updated_by_store_type, self.updated_on_customer,
            # Product Fields
            self.product_id, self.product_name, self.product_description,
            self.product_images, self.product_qr_code, self.category_id,
            self.brand_id, self.material_id, self.frame_type_id,
            self.frame_shape_id, self.color_id, self.unit_id,
            self.origin, self.cost_price, self.sale_price,
            self.model_number, self.hsn_product, self.power_attribute_product,
            self.franchise_sale_price, self.product_quantity,
            self.product_gst, self.status, self.discount_product,
            self.created_on_product, self.created_by_product,
            self.last_updated_on_product, self.last_updated_by_product, self.category_name, self.material_name,
            self.frame_type_name, self.shape_name, self.color_name, self.unit_name, self.brand_name,
        ) = values

        # Parse product images from JSON string to a list
        self.product_images = json.loads(self.product_images) if self.product_images else []
        self.power_attribute = json.loads(self.power_attribute) if self.power_attribute else []

    def to_dict(self):
        return {
            'sale_item_id': self.sale_item_id,
            'order_id': self.order_id,
            'product': self.product_id,
            'hsn': self.hsn,
            'unit_sale_price': self.unit_sale_price,
            'unit_type': self.unit_type,
            'purchase_quantity': self.purchase_quantity,
            'product_total_cost': self.product_total_cost,
            'discount_percentage': self.discount_percentage,
            'is_discount_applied': self.is_discount_applied,
            'power_attribute': self.power_attribute,
            'assigned_lab': self.assigned_lab,
            'customer': self.customer_id,
            'order_status': self.order_status,
            'payment_status': self.payment_status,
            'delivery_status': self.delivery_status,
            'payment_mode': self.payment_mode,
            'amount_paid': self.amount_paid,
            'estimated_delivery_date': self.estimated_delivery_date.strftime('%d-%m-%Y %I:%M %p') if isinstance(
                self.created_on, datetime) else None,
            'linked_item': self.linked_item,
            'sales_note': self.sales_note,
            'created_by_store': self.created_by_store,
            'created_by_store_type': self.created_by_store_type,
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%d-%m-%Y %I:%M %p') if isinstance(self.created_on,
                                                                                      datetime) else None,
            'updated_by': self.updated_by,
            'updated_on': self.updated_on.strftime('%d-%m-%Y %I:%M %p') if isinstance(self.updated_on,
                                                                                      datetime) else None,
            'total_cost': self.total_cost,
            'discount_cost': self.discount_cost,
            'store_name': self.store_name,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,

            # customer fields
            'customer_name': self.customer_name,
            'customer_id': self.customer_id,
            'gender': self.gender,
            'age': self.age,
            'phone': self.phone,
            'email': self.email,
            'language': self.language,
            'city': self.city,
            'address': self.address,
            'created_by_employee_id': self.created_by_employee_id,
            'created_by_store_id': self.created_by_store_id,

            # Product Fields
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_description': self.product_description,
            'product_images': self.product_images,
            'product_qr_code': self.product_qr_code,
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
            'hsn_product': self.hsn_product,
            'power_attribute_product': self.power_attribute_product,
            'franchise_sale_price': self.franchise_sale_price,
            'product_quantity': self.product_quantity,
            'product_gst': self.product_gst,
            'status': self.status,
            'discount_product': self.discount_product,
            'created_on_product': self.created_on_product.strftime('%d-%m-%Y %I:%M %p') if isinstance(
                self.created_on_product, datetime) else None,
            'created_by_product': self.created_by_product,
            'last_updated_on_product': self.last_updated_on_product.strftime('%d-%m-%Y %I:%M %p') if isinstance(
                self.last_updated_on_product, datetime) else None,
            'last_updated_by_product': self.last_updated_by_product,
            'category_name': self.category_name,
            'material_name': self.material_name,
            'frame_type_name': self.frame_type_name,
            'shape_name': self.shape_name,
            'color_name': self.color_name,
            'unit_name': self.unit_name,
            'brand_name': self.brand_name,
        }


def get_order_detail(response):
    sales_order_list = []
    for values in response:
        sales_order = SalesOrder(values)
        sales_order_list.append(sales_order.to_dict())
    return sales_order_list
