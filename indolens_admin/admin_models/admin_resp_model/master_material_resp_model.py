from datetime import datetime

class ProductMaterial:
    def __init__(self, values):
        (
            self.material_id, self.material_name, self.material_description, self.status,
            self.created_on, self.created_by, self.last_updated_on, self.last_updated_by,
            self.creator_name, self.updater_name
        ) = values

    def to_dict(self):
        return {
            'material_id': self.material_id,
            'material_name': self.material_name,
            'material_description': self.material_description,
            'status': self.status,
            'created_on': self.created_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.created_on, datetime) else None,
            'created_by': self.created_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name
        }

def get_product_materials(response):
    material_list = []
    for values in response:
        material = ProductMaterial(values)
        material_list.append(material.to_dict())
    return material_list
