from datetime import datetime
import json

class AdminSetting:
    def __init__(self, values):
        self.setting_id = values[0]
        self.emailjs_attribute = json.loads(values[1]) if values[1] else {}
        self.base_url = values[2]
        self.created_by = values[3]
        self.created_on = values[4]
        self.updated_by = values[5]
        self.updated_on = values[6]

    def to_dict(self):
        return {
            'setting_id': self.setting_id,
            'emailjs_attribute': self.emailjs_attribute,
            'base_url': self.base_url,
            'created_by': self.created_by,
            'created_on': self.created_on,
            'updated_by': self.updated_by,
            'updated_on': self.updated_on.strftime('%d/%m/%Y %I:%M %p') if isinstance(self.updated_on, datetime) else None
        }

def admin_setting_response(response):
    admin_setting = AdminSetting(response)
    return admin_setting.to_dict()
