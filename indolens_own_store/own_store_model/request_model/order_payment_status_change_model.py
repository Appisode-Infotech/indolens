from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class OrderPaymentStatusChangeModel:
    order_id: Optional[str] = None
    order_payment_status: Optional[int] = None
    order_payment_amount: Optional[int] = None
    payment_mode: Optional[int] = None

    def get_attribute(self, attribute_name: str) -> Optional[Any]:
        return getattr(self, attribute_name, None)

    @staticmethod
    def from_dict(obj: Any) -> 'OrderPaymentStatusChangeModel':
        assert isinstance(obj, dict)
        order_id = from_union([from_str, from_none], obj.get("orderId"))
        order_payment_status = from_union([from_str, from_none], obj.get("orderPaymentStatus"))
        order_payment_amount = from_union([from_str, from_none], obj.get("orderPaymentAmount"))
        payment_mode = from_union([from_str, from_none], obj.get("payment_mode"))
        return OrderPaymentStatusChangeModel(order_id, order_payment_status, order_payment_amount, payment_mode)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.order_id is not None:
            result["orderId"] = from_union([from_str, from_none], self.order_id)
        if self.order_payment_status is not None:
            result["orderPaymentStatus"] = from_union([from_int, from_none], self.order_payment_status)
        if self.order_payment_amount is not None:
            result["orderPaymentAmount"] = from_union([from_int, from_none], self.order_payment_amount)
        if self.payment_mode is not None:
            result["payment_mode"] = from_union([from_int, from_none], self.payment_mode)
        return result


def order_payment_status_change_model_from_dict(s: Any) -> OrderPaymentStatusChangeModel:
    return OrderPaymentStatusChangeModel.from_dict(s)


def order_payment_status_change_model_to_dict(x: OrderPaymentStatusChangeModel) -> Any:
    return to_class(OrderPaymentStatusChangeModel, x)
