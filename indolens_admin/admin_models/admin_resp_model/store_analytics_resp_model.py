from datetime import datetime

class StoreAnalytics:
    def __init__(self, values):
        (
            self.store_id, self.store_name, self.total_sale, self.total_expense,
            self.net_profit
        ) = values

    def to_dict(self):
        return {
            'store_id': self.store_id,
            'store_name': self.store_name,
            'total_sale': self.total_sale,
            'total_expense': self.total_expense,
            'net_profit': self.net_profit,
        }


def store_analytics(response):
    store_analytics_list = []
    for values in response:
        store_analytics = StoreAnalytics(values)
        store_analytics_list.append(store_analytics.to_dict())
    return store_analytics_list
