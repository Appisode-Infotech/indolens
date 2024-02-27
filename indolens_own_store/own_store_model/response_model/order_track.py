from datetime import datetime


class OrderTrack:
    def __init__(self, values):
        (
            self.track_id, self.order_id, self.status, self.created_on
        ) = values

    def to_dict(self):
        return {
            'track_id': self.track_id,
            'order_id': self.order_id,
            'status': self.status,
            'created_on': self.created_on.strftime('%d/%m/%Y %I:%M %p') if isinstance(self.created_on,
                                                                             datetime) else None,
        }


def order_track(response):
    order_track_list = []
    for values in response:
        order = OrderTrack(values)
        order_track_list.append(order.to_dict())
    return order_track_list
