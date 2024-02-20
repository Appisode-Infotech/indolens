import json
from datetime import datetime


class AreaHead:
    def __init__(self, values):
        (
            self.area_head_id, self.name, self.email, self.phone, self.password,
            self.profile_pic, assigned_stores, self.address, self.document_1_type,
            document_1_urls, self.document_2_type, document_2_urls, self.status,
            self.created_by, self.created_on, self.last_updated_by, self.last_updated_on
        ) = values

        self.assigned_stores = [int(store) for store in assigned_stores.split(',')] if assigned_stores else []

        self.document_1_url = json.loads(document_1_urls) if document_1_urls else []
        self.document_2_url = json.loads(document_2_urls) if document_2_urls else []

    def to_dict(self):
        return {
            'area_head_id': self.area_head_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'profile_pic': self.profile_pic,
            'assigned_stores': self.assigned_stores,
            'address': self.address,
            'document_1_type': self.document_1_type,
            'document_1_url': self.document_1_url,
            'document_2_type': self.document_2_type,
            'document_2_url': self.document_2_url,
            'status': self.status,
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%d/%m/%Y %I:%M %p') if isinstance(self.created_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'last_updated_on': self.last_updated_on.strftime('%d/%m/%Y %I:%M %p') if isinstance(self.last_updated_on,
                                                                                                datetime) else None
        }


def get_area_heads(response):
    area_head_list = []
    for values in response:
        area_head = AreaHead(values)
        area_head_list.append(area_head.to_dict())
    return area_head_list
