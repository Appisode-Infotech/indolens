from datetime import datetime

class Brand:
    def __init__(self, values):
        (
            self.brand_id, self.brand_name, self.category_id, self.brand_description,
            self.status, self.created_on, self.created_by, self.last_updated_on, self.last_updated_by,
            self.creator_name, self.updater_name
        ) = values

    def to_dict(self):
        return {
            'brand_id': self.brand_id,
            'brand_name': self.brand_name,
            'category_id': self.category_id,
            'brand_description': self.brand_description,
            'status': self.status,
            'created_on': self.created_on.strftime('%Y-%m-%d') if isinstance(self.created_on, datetime) else None,
            'created_by': self.created_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name
        }

def get_brands(response):
    brand_list = []
    for values in response:
        brand = Brand(values)
        brand_list.append(brand.to_dict())
    return brand_list
