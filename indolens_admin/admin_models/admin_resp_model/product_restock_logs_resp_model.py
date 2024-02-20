from datetime import datetime

class CentralInventoryRestockLog:
    def __init__(self, values):
        (
            self.restock_id, self.product_id, self.quantity, self.created_by,
            self.created_on, self.product_name, self.creator_name

        ) = values

    def to_dict(self):
        return {
            'restock_id': self.restock_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'created_by': self.created_by,
            'created_on': self.created_on.strftime('%d-%m-%Y %I:%M %p') if isinstance(self.created_on, datetime) else None,
            'product_name': self.product_name,
            'creator_name': self.creator_name,
        }


def get_restock_logs(response):
    restock_log_list = []
    for values in response:
        restock_log = CentralInventoryRestockLog(values)
        restock_log_list.append(restock_log.to_dict())
    return restock_log_list
