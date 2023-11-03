from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class StoreExpenseModel:
    store_expense_id: Optional[int]
    store_id: Optional[int]
    store_type: Optional[int]
    expense_amount: Optional[int]
    expense_reason: Optional[str]
    expense_date: Optional[str]
    created_on: Optional[str]
    created_by: Optional[int]

    def __init__(self, store_expense_id: Optional[int], store_id: Optional[int], store_type: Optional[int], expense_amount: Optional[int], expense_reason: Optional[str], expense_date: Optional[str], created_on: Optional[str], created_by: Optional[int]) -> None:
        self.store_expense_id = store_expense_id
        self.store_id = store_id
        self.store_type = store_type
        self.expense_amount = expense_amount
        self.expense_reason = expense_reason
        self.expense_date = expense_date
        self.created_on = created_on
        self.created_by = created_by

    @staticmethod
    def from_dict(obj: Any) -> 'StoreExpenseModel':
        assert isinstance(obj, dict)
        store_expense_id = from_union([from_str, from_none], obj.get("store_expense_id"))
        store_id = from_union([from_str, from_none], obj.get("store_id"))
        store_type = from_union([from_str, from_none], obj.get("store_type"))
        expense_amount = from_union([from_str, from_none], obj.get("expense_amount"))
        expense_reason = from_union([from_str, from_none], obj.get("expense_reason"))
        expense_date = from_union([from_str, from_none], obj.get("expense_date"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        return StoreExpenseModel(store_expense_id, store_id, store_type, expense_amount, expense_reason, expense_date, created_on, created_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.store_expense_id is not None:
            result["store_expense_id"] = from_union([from_int, from_none], self.store_expense_id)
        if self.store_id is not None:
            result["store_id"] = from_union([from_int, from_none], self.store_id)
        if self.store_type is not None:
            result["store_type"] = from_union([from_int, from_none], self.store_type)
        if self.expense_amount is not None:
            result["expense_amount"] = from_union([from_int, from_none], self.expense_amount)
        if self.expense_reason is not None:
            result["expense_reason"] = from_union([from_str, from_none], self.expense_reason)
        if self.expense_date is not None:
            result["expense_date"] = from_union([from_str, from_none], self.expense_date)
        if self.created_on is not None:
            result["created_on"] = from_union([from_str, from_none], self.created_on)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        return result


def store_expense_model_from_dict(s: Any) -> StoreExpenseModel:
    return StoreExpenseModel.from_dict(s)


def store_expense_model_to_dict(x: StoreExpenseModel) -> Any:
    return to_class(StoreExpenseModel, x)
