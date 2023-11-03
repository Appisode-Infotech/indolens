import json
from datetime import datetime

class StoreCustomer:
    def __init__(self, values):
        (
            self.customer_id, self.name, self.gender, self.age, self.phone, self.email,
            self.language, self.address, self.created_by_employee_id, self.created_by_store_id,
            self.created_by_store_type, created_on, self.updated_by_employee_id, self.updated_by_store_id,
            self.updated_by_store_type, updated_on, self.store_name, self.creator_name, self.updater_name
        ) = values

        # Parse created_on and updated_on fields to datetime
        self.created_on = datetime.strptime(created_on, '%Y-%m-%d %H:%M:%S') if created_on else None
        self.updated_on = datetime.strptime(updated_on, '%Y-%m-%d %H:%M:%S') if updated_on else None

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'phone': self.phone,
            'email': self.email,
            'language': self.language,
            'address': self.address,
            'created_by_employee_id': self.created_by_employee_id,
            'created_by_store_id': self.created_by_store_id,
            'created_by_store_type': self.created_by_store_type,
            'created_on': self.created_on.strftime('%Y-%m-%d') if self.created_on else None,
            'updated_by_employee_id': self.updated_by_employee_id,
            'updated_by_store_id': self.updated_by_store_id,
            'updated_by_store_type': self.updated_by_store_type,
            'updated_on': self.updated_on.strftime('%Y-%m-%d %H:%M:%S') if self.updated_on else None,
            'store_name': self.store_name,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,
        }

def get_store_customers(response):
    store_customer_list = []
    for values in response:
        store_customer = StoreCustomer(values)
        store_customer_list.append(store_customer.to_dict())
    return store_customer_list
