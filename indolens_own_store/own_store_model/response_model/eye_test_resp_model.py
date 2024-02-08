import json
from datetime import datetime

class EyeTest:
    def __init__(self, values):
        (
            self.eye_test_id, self.customer_id, power_attributes, self.created_by_store_id, self.created_by_store_type,
            self.created_by, self.created_on, self.updated_by, self.updated_on, self.customer_name, self.customer_phone,
            self.creator_name,
            self.updater_name
        ) = values

        # Parse document URLs from JSON strings to lists
        self.power_attributes = json.loads(power_attributes) if power_attributes else []

    def to_dict(self):
        return {
            'eye_test_id': self.eye_test_id,
            'customer_id': self.customer_id,
            'power_attributes': self.power_attributes,
            'created_by_store_id': self.created_by_store_id,
            'created_by_store_type': self.created_by_store_type,
            'created_by': self.created_by,
            'created_on': self.created_on,
            'updated_by': self.updated_by,
            'updated_on': self.updated_on,
            'customer_name': self.customer_name,
            'customer_phone': self.customer_phone,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,
        }

def get_eye_test_resp(response):
    eye_test_list = []
    for values in response:
        eye_test = EyeTest(values)
        eye_test_list.append(eye_test.to_dict())
    return eye_test_list
