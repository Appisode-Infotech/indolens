from datetime import datetime


class SalesOrderPaymentTrack:
    def __init__(self, values):
        (
            self.id, self.order_id, self.payment_amount, self.payment_mode,
            self.payment_type, self.created_by_store, self.created_by_store_type,
            self.created_by_id, self.created_on, self.created_by_name
        ) = values

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'payment_amount': self.payment_amount,
            'payment_mode': self.payment_mode,
            'payment_type': self.payment_type,
            'created_by_store': self.created_by_store,
            'created_by_store_type': self.created_by_store_type,
            'created_by_id': self.created_by_id,
            'created_on': self.created_on.strftime('%d-%m-%Y') if isinstance(self.created_on, datetime) else None,
            'created_by_name': self.created_by_name
        }


def sales_order_payment_track_response(response):
    sales_order_payment_track_list = []
    for values in response:
        sales_order_payment_track = SalesOrderPaymentTrack(values)
        sales_order_payment_track_list.append(sales_order_payment_track.to_dict())
    return sales_order_payment_track_list
