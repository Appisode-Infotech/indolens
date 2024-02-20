import json
from datetime import datetime

class StoreCustomer:
    def __init__(self, values):
        (
            self.customer_id, self.name, self.gender, self.age, self.phone, self.email,
            self.language, self.city, self.address, self.created_by_employee_id, self.created_by_store_id,
            self.created_by_store_type, self.created_on, self.updated_by_employee_id, self.updated_by_store_id,
            self.updated_by_store_type, self.updated_on, self.store_name, self.creator_name, self.updater_name,
            self.total_spend, self.total_order_counts
        ) = values


    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'phone': self.phone,
            'email': self.email,
            'language': self.language,
            'city': self.city,
            'address': self.address,
            'created_by_employee_id': self.created_by_employee_id,
            'created_by_store_id': self.created_by_store_id,
            'created_by_store_type': self.created_by_store_type,
            'created_on': self.created_on.strftime('%d/%m/%Y %I:%M %p') if self.created_on else None,
            'updated_by_employee_id': self.updated_by_employee_id,
            'updated_by_store_id': self.updated_by_store_id,
            'updated_by_store_type': self.updated_by_store_type,
            'updated_on': self.updated_on.strftime('%d/%m/%Y %I:%M %p') if self.updated_on else None,
            'store_name': self.store_name,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,
            'total_spend': self.total_spend,
            'total_order_counts': self.total_order_counts,
        }

def get_customers(response):
    store_customer_list = []
    for values in response:
        store_customer = StoreCustomer(values)
        store_customer_list.append(store_customer.to_dict())
    return store_customer_list
