from datetime import datetime

class StoreExpense:
    def __init__(self, values):
        (
            self.store_expense_id, self.store_id, self.store_type, self.expense_amount,
            self.expense_reason, self.expense_date, self.created_on, self.created_by, self.creator_name
        ) = values

    def to_dict(self):
        return {
            'store_expense_id': self.store_expense_id,
            'store_id': self.store_id,
            'store_type': self.store_type,
            'expense_amount': self.expense_amount,
            'expense_reason': self.expense_reason,
            'expense_date': self.expense_date.strftime('%Y-%m-%d') if isinstance(self.expense_date, datetime) else None,
            'created_on': self.created_on.strftime('%Y-%m-%d %H:%M:%S') if isinstance(self.created_on, datetime) else None,
            'created_by': self.created_by,
            'creator_name': self.creator_name,
        }

def get_store_expenses(response):
    store_expense_list = []
    for values in response:
        store_expense = StoreExpense(values)
        store_expense_list.append(store_expense.to_dict())
    return store_expense_list
