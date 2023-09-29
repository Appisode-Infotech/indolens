from datetime import datetime
import json

class LabTechnician:
    def __init__(self, values):
        (
            self.lab_technician_id, self.name, self.email, self.phone, self.password,
            self.profile_pic, self.assigned_lab_id, self.address, self.document_1_type,
            document_1_urls, self.document_2_type, document_2_urls, self.status,
            self.created_by, self.created_on, self.last_updated_by, self.last_updated_on,
            self.creator_name, self.updater_name, self.lab_name
        ) = values

        # Parse document URLs from JSON strings to lists
        self.document_1_url = json.loads(document_1_urls) if document_1_urls else []
        self.document_2_url = json.loads(document_2_urls) if document_2_urls else []

    def to_dict(self):
        return {
            'lab_technician_id': self.lab_technician_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'profile_pic': self.profile_pic,
            'assigned_lab_id': self.assigned_lab_id,
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
            'lab_name': self.lab_name
        }

def get_lab_technicians(response):
    lab_technician_list = []
    for values in response:
        lab_technician = LabTechnician(values)
        lab_technician_list.append(lab_technician.to_dict())
    return lab_technician_list
