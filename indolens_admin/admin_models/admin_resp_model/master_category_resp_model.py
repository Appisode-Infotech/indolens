from datetime import datetime

class ProductCategory:
    def __init__(self, values):
        (
            self.category_id, self.category_name, self.category_prefix, self.category_description,
            self.status, self.created_on, self.created_by, self.last_updated_on, self.last_updated_by,
            self.creator_name, self.updater_name
        ) = values

    def to_dict(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'category_prefix': self.category_prefix,
            'category_description': self.category_description,
            'status': self.status,
            'created_on': self.created_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.created_on, datetime) else None,
            'created_by': self.created_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name
        }

def get_product_categories(response):
    category_list = []
    for values in response:
        category = ProductCategory(values)
        category_list.append(category.to_dict())
    return category_list
