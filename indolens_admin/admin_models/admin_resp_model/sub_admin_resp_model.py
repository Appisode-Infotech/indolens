import json
from datetime import datetime


class User:
    def __init__(self, values):
        (
            self.admin_id, self.name, self.email, self.phone, self.password, self.role,
            self.profile_pic, self.address, self.document_1_type, document_1_url,
            self.document_2_type, document_2_url, self.status, self.created_by,
            self.created_on, self.last_updated_by, self.last_updated_on, self.creator_name,
            self.updater_name
        ) = values

        # Parse document URLs from JSON strings to lists
        self.document_1_url = json.loads(document_1_url) if document_1_url else []
        self.document_2_url = json.loads(document_2_url) if document_2_url else []

    def to_dict(self):
        return {
            'admin_id': self.admin_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'role': self.role,
            'profile_pic': self.profile_pic,
            'address': self.address,
            'document_1_type': self.document_1_type,
            'document_1_url': self.document_1_url,
            'document_2_type': self.document_2_type,
            'document_2_url': self.document_2_url,
            'status': self.status,
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%d-%m-%Y %I:%M %p') if isinstance(self.created_on,
                                                                                      datetime) else None,
            'last_updated_by': self.last_updated_by,
            'last_updated_on': self.last_updated_on.strftime('%d-%m-%Y %I:%M %p') if isinstance(self.last_updated_on,
                                                                                                datetime) else None,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,
        }


def get_sub_admin(response):
    user_list = []
    for values in response:
        user = User(values)
        user_list.append(user.to_dict())
    return user_list
