import json
from datetime import datetime

class OwnStoreEmployee:
    def __init__(self, values):
        (
            self.employee_id, self.name, self.email, self.phone, self.password,
            self.profile_pic, self.assigned_store_id, self.address, self.document_1_type,
            document_1_url, self.document_2_type, document_2_url, self.status,
            self.role, self.created_by, self.created_on, self.last_updated_by, self.last_updated_on, certificates,
            self.store_name, self.creator_name, self.updater_name
        ) = values

        # Parse document URLs from JSON strings to lists
        self.document_1_url = json.loads(document_1_url) if document_1_url else []
        self.document_2_url = json.loads(document_2_url) if document_2_url else []
        self.certificates = json.loads(certificates) if certificates else []

    def to_dict(self):
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'profile_pic': self.profile_pic,
            'assigned_store_id': self.assigned_store_id,
            'address': self.address,
            'document_1_type': self.document_1_type,
            'document_1_url': self.document_1_url,
            'document_2_type': self.document_2_type,
            'document_2_url': self.document_2_url,
            'status': self.status,
            'role': self.role,
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%d/%m/%Y %I:%M %p') if isinstance(self.created_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'last_updated_on': self.last_updated_on.strftime('%d/%m/%Y %I:%M %p') if isinstance(self.last_updated_on, datetime) else None,
            'certificates': self.certificates,
            'store_name': self.store_name,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,
        }

def get_franchise_store_employees(response):
    own_store_employee_list = []
    for values in response:
        own_store_employee = OwnStoreEmployee(values)
        own_store_employee_list.append(own_store_employee.to_dict())
    return own_store_employee_list
