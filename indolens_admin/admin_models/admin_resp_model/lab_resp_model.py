from datetime import datetime


class Lab:
    def __init__(self, values):
        (
            self.lab_id, self.lab_name, self.lab_display_name, self.lab_phone,
            self.lab_gst, self.lab_email, self.lab_city, self.lab_state,
            self.lab_zip, self.lab_lat, self.lab_lng, self.lab_address,
            self.status, self.created_by, self.created_on, self.last_updated_by,
            self.last_updated_on, self.creator_name, self.updater_name,
            self.lab_technician_name,self.job_count,
        ) = values

    def to_dict(self):
        return {
            'lab_id': self.lab_id,
            'lab_name': self.lab_name,
            'lab_display_name': self.lab_display_name,
            'lab_phone': self.lab_phone,
            'lab_gst': self.lab_gst,
            'lab_email': self.lab_email,
            'lab_city': self.lab_city,
            'lab_state': self.lab_state,
            'lab_zip': self.lab_zip,
            'lab_lat': self.lab_lat,
            'lab_lng': self.lab_lng,
            'lab_address': self.lab_address,
            'status': self.status,
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%d/%m/%Y %I:%M %p') if isinstance(self.created_on, datetime) else None,
            'last_updated_by': self.last_updated_by,
            'last_updated_on': self.last_updated_on.strftime('%d/%m/%Y %I:%M %p') if isinstance(self.last_updated_on,
                                                                                                datetime) else None,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,
            'lab_technician_name': self.lab_technician_name,
            'job_count': self.job_count,
        }


def get_labs(response):
    lab_list = []
    for values in response:
        lab = Lab(values)
        lab_list.append(lab.to_dict())
    return lab_list
