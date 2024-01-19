from datetime import datetime


class MasterUnit:
    def __init__(self, values):
        (
            self.unit_id, self.unit_name, self.status, self.created_on, self.created_by,
            self.last_updated_on, self.last_updated_by,
            self.creator_name, self.updater_name
        ) = values

    def to_dict(self):
        return {
            'unit_id': self.unit_id,
            'unit_name': self.unit_name,
            'status': self.status,
            'created_on': self.created_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.created_on, datetime) else None,
            'created_by': self.created_by,
            'last_updated_on': self.last_updated_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.last_updated_on,
                                                                                                datetime) else None,
            'last_updated_by': self.last_updated_by,
            'creator_name': self.creator_name,
            'updater_name': self.updater_name,
        }


def get_master_units(response):
    master_units_list = []
    for values in response:
        master_unit = MasterUnit(values)
        master_units_list.append(master_unit.to_dict())
    return master_units_list
