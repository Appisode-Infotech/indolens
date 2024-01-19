from datetime import datetime


class ProductColor:
    def __init__(self, values):
        (
            self.color_id, self.color_code, self.color_name, self.color_description, self.status,
            self.created_on, self.created_by, self.last_updated_on, self.last_updated_by,
            self.creator_name, self.updater_name
        ) = values

    def to_dict(self):
        return {
            'color_id': self.color_id,
            'color_code': self.color_code,
            'color_name': self.color_name,
            'color_description': self.color_description,
            'status': self.status,
            'created_on': self.created_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.created_on, datetime) else None,
            'created_by': self.created_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name
        }

def get_product_colors(response):
    color_list = []
    for values in response:
        color = ProductColor(values)
        color_list.append(color.to_dict())
    return color_list
