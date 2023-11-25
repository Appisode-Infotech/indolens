from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x

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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class StoreCreateStockRequestModel:
    product_id: Optional[int]
    product_quantity: Optional[int]
    request_to_store_id: Optional[int]
    request_from_store_id: Optional[int]
    created_by: Optional[int]
    store_type: Optional[int]
    comments: Optional[str]

    def __init__(self, product_id: Optional[int], product_quantity: Optional[int], request_to_store_id: Optional[int], request_from_store_id: Optional[int], created_by: Optional[int], store_type: Optional[int], comments: Optional[str]) -> None:
        self.product_id = product_id
        self.product_quantity = product_quantity
        self.request_to_store_id = request_to_store_id
        self.request_from_store_id = request_from_store_id
        self.created_by = created_by
        self.store_type = store_type
        self.comments = comments

    @staticmethod
    def from_dict(obj: Any) -> 'StoreCreateStockRequestModel':
        assert isinstance(obj, dict)
        product_id = from_union([from_str, from_none], obj.get("product_id"))
        product_quantity = from_union([from_str, from_none], obj.get("product_quantity"))
        request_to_store_id = from_union([from_str, from_none], obj.get("request_to_store_id"))
        request_from_store_id = from_union([from_str, from_none], obj.get("request_from_store_id"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        store_type = from_union([from_str, from_none], obj.get("store_type"))
        comments = from_union([from_str, from_none], obj.get("comments"))
        return StoreCreateStockRequestModel(product_id, product_quantity, request_to_store_id, request_from_store_id, created_by, store_type, comments)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.product_id is not None:
            result["product_id"] = from_union([from_int, from_none], self.product_id)
        if self.product_quantity is not None:
            result["product_quantity"] = from_union([from_int, from_none], self.product_quantity)
        if self.request_to_store_id is not None:
            result["request_to_store_id"] = from_union([from_int, from_none], self.request_to_store_id)
        if self.request_from_store_id is not None:
            result["request_from_store_id"] = from_union([from_int, from_none], self.request_from_store_id)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        if self.store_type is not None:
            result["store_type"] = from_union([from_int, from_none], self.store_type)
        if self.comments is not None:
            result["comments"] = from_union([from_int, from_none], self.comments)
        return result


def store_create_stock_request_model_from_dict(s: Any) -> StoreCreateStockRequestModel:
    return StoreCreateStockRequestModel.from_dict(s)


def store_create_stock_request_model_to_dict(x: StoreCreateStockRequestModel) -> Any:
    return to_class(StoreCreateStockRequestModel, x)
