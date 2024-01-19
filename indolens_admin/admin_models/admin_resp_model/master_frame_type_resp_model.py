from datetime import datetime

class FrameType:
    def __init__(self, values):
        (
            self.frame_id, self.frame_type_name, self.frame_type_description, self.status,
            self.created_on, self.created_by, self.last_updated_on, self.last_updated_by,
            self.creator_name, self.updater_name
        ) = values

    def to_dict(self):
        return {
            'frame_id': self.frame_id,
            'frame_type_name': self.frame_type_name,
            'frame_type_description': self.frame_type_description,
            'status': self.status,
            'created_on': self.created_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.created_on, datetime) else None,
            'created_by': self.created_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name
        }

def get_frame_types(response):
    frame_type_list = []
    for values in response:
        frame_type = FrameType(values)
        frame_type_list.append(frame_type.to_dict())
    return frame_type_list
