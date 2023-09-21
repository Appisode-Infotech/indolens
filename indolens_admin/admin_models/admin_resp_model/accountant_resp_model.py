from datetime import datetime
import json

class Accountant:
    def __init__(self, values):
        (
            self.accountant_id, self.name, self.email, self.phone, self.password,
            self.profile_pic, self.address, self.document_1_type,
            document_1_url, self.document_2_type, document_2_url, self.status,
            self.created_by, self.created_on, self.last_updated_by, self.last_updated_on,
            self.creator_name, self.updater_name
        ) = values

        # Parse document URLs from JSON strings to lists
        self.document_1_url = json.loads(document_1_url) if document_1_url else []
        self.document_2_url = json.loads(document_2_url) if document_2_url else []

    def to_dict(self):
        return {
            'accountant_id': self.accountant_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'profile_pic': self.profile_pic,
            'address': self.address,
            'document_1_type': self.document_1_type,
            'document_1_url': self.document_1_url,
            'document_2_type': self.document_2_type,
            'document_2_url': self.document_2_url,
            'status': self.status,
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%Y-%m-%d') if isinstance(self.created_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on, datetime) else None,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,
        }

def get_accountants(response):
    accountant_list = []
    for values in response:
        accountant = Accountant(values)
        accountant_list.append(accountant.to_dict())
    return accountant_list
