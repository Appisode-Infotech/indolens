from datetime import datetime

class StoreManager:
    def __init__(self, values):
        (
            self.store_manager_id, self.name, self.email, self.phone, self.password,
            self.profile_pic, self.assigned_store_id, self.address, self.document_1_type,
            self.document_1_url, self.document_2_type, self.document_2_url, self.status,
            self.created_by, self.created_on, self.last_updated_by, self.last_updated_on,
            self.store_name, self.creator_name, self.updater_name
        ) = values

    def to_dict(self):
        return {
            'store_manager_id': self.store_manager_id,
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
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.created_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on, datetime) else None,
            'store_name': self.store_name,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name
        }

def get_store_managers(response):
    store_manager_list = []
    for values in response:
        store_manager = StoreManager(values)
        store_manager_list.append(store_manager.to_dict())
    return store_manager_list

