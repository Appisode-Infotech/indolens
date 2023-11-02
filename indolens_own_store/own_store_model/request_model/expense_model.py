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


class ExpenseModel:
    expense_id: Optional[int]
    expense_amount: Optional[int]
    expense_reason: Optional[str]
    expense_date: Optional[str]

    def __init__(self, expense_id: Optional[int], expense_amount: Optional[int], expense_reason: Optional[str], expense_date: Optional[str]) -> None:
        self.expense_id = expense_id
        self.expense_amount = expense_amount
        self.expense_reason = expense_reason
        self.expense_date = expense_date

    @staticmethod
    def from_dict(obj: Any) -> 'ExpenseModel':
        assert isinstance(obj, dict)
        expense_id = from_union([from_int, from_none], obj.get("expense_id"))
        expense_amount = from_union([from_int, from_none], obj.get("expense_amount"))
        expense_reason = from_union([from_str, from_none], obj.get("expense_reason"))
        expense_date = from_union([from_str, from_none], obj.get("expense_date"))
        return ExpenseModel(expense_id, expense_amount, expense_reason, expense_date)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.expense_id is not None:
            result["expense_id"] = from_union([from_int, from_none], self.expense_id)
        if self.expense_amount is not None:
            result["expense_amount"] = from_union([from_int, from_none], self.expense_amount)
        if self.expense_reason is not None:
            result["expense_reason"] = from_union([from_str, from_none], self.expense_reason)
        if self.expense_date is not None:
            result["expense_date"] = from_union([from_str, from_none], self.expense_date)
        return result


def expense_model_from_dict(s: Any) -> ExpenseModel:
    return ExpenseModel.from_dict(s)


def expense_model_to_dict(x: ExpenseModel) -> Any:
    return to_class(ExpenseModel, x)
