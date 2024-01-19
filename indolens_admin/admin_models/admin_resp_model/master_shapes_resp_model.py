from datetime import datetime


class FrameShape:
    def __init__(self, values):
        (
            self.shape_id, self.shape_name, self.shape_description, self.status,
            self.created_on, self.created_by, self.last_updated_on, self.last_updated_by,
            self.creator_name, self.updater_name
        ) = values

    def to_dict(self):
        return {
            'shape_id': self.shape_id,
            'shape_name': self.shape_name,
            'shape_description': self.shape_description,
            'status': self.status,
            'created_on': self.created_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.created_on, datetime) else None,
            'created_by': self.created_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name
        }

def get_frame_shapes(response):
    shape_list = []
    for values in response:
        shape = FrameShape(values)
        shape_list.append(shape.to_dict())
    return shape_list
