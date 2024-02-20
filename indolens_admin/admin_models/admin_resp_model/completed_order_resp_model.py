from datetime import datetime

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
            self.updated_by, self.updated_on, self.customer_name,
            self.total_cost, self.store_name, self.creator_name,
            self.updater_name, self.invoice_number
        ) = values

    def to_dict(self):
        return {
            'sale_item_id': self.sale_item_id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'hsn': self.hsn,
            'unit_sale_price': self.unit_sale_price,
            'unit_type': self.unit_type,
            'purchase_quantity': self.purchase_quantity,
            'product_total_cost': self.product_total_cost,
            'discount_percentage': self.discount_percentage,
            'is_discount_applied': self.is_discount_applied,
            'power_attribute': self.power_attribute,
            'assigned_lab': self.assigned_lab,
            'customer_id': self.customer_id,
            'order_status': self.order_status,
            'payment_status': self.payment_status,
            'delivery_status': self.delivery_status,
            'payment_mode': self.payment_mode,
            'amount_paid': self.amount_paid,
            'estimated_delivery_date': self.estimated_delivery_date,
            'linked_item': self.linked_item,
            'sales_note': self.sales_note,
            'created_by_store': self.created_by_store,
            'created_by_store_type': self.created_by_store_type,
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%d/%m/%Y %I:%M %p') if isinstance(self.created_on, datetime) else None,
            'updated_by': self.updated_by,
            'updated_on': self.updated_on.strftime('%d/%m/%Y %I:%M %p') if isinstance(self.updated_on, datetime) else None,
            'customer_name': self.customer_name,
            'total_cost': self.total_cost,
            'store_name': self.store_name,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,
            'invoice_number': self.invoice_number
        }

def get_completed_sales_orders(response):
    sales_order_list = []
    for values in response:
        sales_order = SalesOrder(values)
        sales_order_list.append(sales_order.to_dict())
    return sales_order_list
