from datetime import datetime

class Invoice:
    def __init__(self, values):
        (
            self.invoice_id, self.invoice_number, self.order_id, self.store_id,
            self.store_type, self.invoice_status, self.invoice_date
        ) = values

    def to_dict(self):
        return {
            'invoice_id': self.invoice_id,
            'invoice_number': self.invoice_number,
            'order_id': self.order_id,
            'store_id': self.store_id,
            'store_type': self.store_type,
            'invoice_status': self.invoice_status,
            'invoice_date': self.invoice_date,
        }


def get_invoice_detail(values):
    if values is not None:
        invoice = Invoice(values)
        return invoice.to_dict()
    else:
        return {}
