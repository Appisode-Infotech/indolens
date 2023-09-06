from datetime import datetime

class AdminUser:
    def __init__(self, values):
        self.admin_id = values[0]
        self.name = values[1]
        self.email = values[2]
        self.phone = values[3]
        self.password = values[4]
        self.sales_executive = values[5]
        self.profile_pic = values[6]
        self.address = values[7]
        self.document_1_type = values[8]
        self.document_1_url = values[9]
        self.document_2_type = values[10]
        self.document_2_url = values[11]
        self.status = values[12]
        self.created_by = values[13]
        self.created_on = values[14]
        self.last_updated_by = values[15]
        self.last_updated_on = values[16]

    def to_dict(self):
        return {
            'admin_id': self.admin_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'sales_executive': self.sales_executive,
            'profile_pic': self.profile_pic,
            'address': self.address,
            'document_1_type': self.document_1_type,
            'document_1_url': self.document_1_url,
            'document_2_type': self.document_2_type,
            'document_2_url': self.document_2_url,
            'status': self.status,
            'created_by': self.created_by,
            'created_on': self.created_on,
            'last_updated_by': self.last_updated_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on, datetime) else None
        }

def get_admin_user(response):
    values = response  # Replace this with your actual response data
    admin_user = AdminUser(values)
    return admin_user.to_dict()

# Example usage:

admin_user_data = get_admin_user(response)
