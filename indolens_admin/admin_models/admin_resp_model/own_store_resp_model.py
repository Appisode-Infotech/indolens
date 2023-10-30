from datetime import datetime


class Store:
    def __init__(self, values):
        (
            self.store_id, self.store_name, self.store_display_name, self.store_phone, self.store_gst,
            self.store_email, self.store_city, self.store_state, self.store_zip, self.store_lat, self.store_lng,
            self.store_address, self.status, self.created_by, self.created_on, self.last_updated_by,
            self.last_updated_on, self.manager_name, self.employee_id
        ) = values

    def to_dict(self):
        return {
            'store_id': self.store_id,
            'store_name': self.store_name,
            'store_display_name': self.store_display_name,
            'store_phone': self.store_phone,
            'store_gst': self.store_gst,
            'store_email': self.store_email,
            'store_city': self.store_city,
            'store_state': self.store_state,
            'store_zip': self.store_zip,
            'store_lat': self.store_lat,
            'store_lng': self.store_lng,
            'store_address': self.store_address,
            'status': self.status,
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%Y-%m-%d') if isinstance(self.created_on,
                                                                             datetime) else None,
            'last_updated_by': self.last_updated_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on,
                                                                                                datetime) else None,
            'manager_name': self.manager_name,
            'employee_id': self.employee_id,
        }


def get_own_store(response):
    store_list = []
    for values in response:
        store = Store(values)
        store_list.append(store.to_dict())
    return store_list
