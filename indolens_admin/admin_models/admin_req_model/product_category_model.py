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


class ProductCategoryModel:
    category_id: Optional[str]
    category_name: Optional[str]
    category_prefix: Optional[str]
    category_description: Optional[str]
    status: Optional[int]
    created_on: Optional[str]
    created_by: Optional[int]
    last_updated_on: Optional[str]
    last_updated_by: Optional[int]

    def __init__(self, category_id: Optional[str], category_name: Optional[str], category_prefix: Optional[str],
                 category_description: Optional[str], status: Optional[int], created_on: Optional[str],
                 created_by: Optional[int], last_updated_on: Optional[str], last_updated_by: Optional[int]) -> None:
        self.category_id = category_id
        self.category_name = category_name
        self.category_prefix = category_prefix
        self.category_description = category_description
        self.status = status
        self.created_on = created_on
        self.created_by = created_by
        self.last_updated_on = last_updated_on
        self.last_updated_by = last_updated_by

    @staticmethod
    def from_dict(obj: Any) -> 'ProductCategoryModel':
        assert isinstance(obj, dict)
        category_id = from_union([from_str, from_none], obj.get("category_id"))
        category_name = from_union([from_str, from_none], obj.get("category_name"))
        category_prefix = from_union([from_str, from_none], obj.get("category_prefix"))
        category_description = from_union([from_str, from_none], obj.get("category_description"))
        status = from_union([from_int, from_none], obj.get("status"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        last_updated_on = from_union([from_str, from_none], obj.get("last_updated_on"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        return ProductCategoryModel(category_id, category_name, category_prefix, category_description, status,
                                    created_on, created_by, last_updated_on, last_updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.category_id is not None:
            result["category_id"] = from_union([from_str, from_none], self.category_id)
        if self.category_name is not None:
            result["category_name"] = from_union([from_str, from_none], self.category_name)
        if self.category_prefix is not None:
            result["category_prefix"] = from_union([from_str, from_none], self.category_prefix)
        if self.category_description is not None:
            result["category_description"] = from_union([from_str, from_none], self.category_description)
        if self.status is not None:
            result["status"] = from_union([from_int, from_none], self.status)
        if self.created_on is not None:
            result["created_on"] = from_union([from_str, from_none], self.created_on)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        if self.last_updated_on is not None:
            result["last_updated_on"] = from_union([from_str, from_none], self.last_updated_on)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([from_int, from_none], self.last_updated_by)
        return result


def product_category_model_from_dict(s: Any) -> ProductCategoryModel:
    return ProductCategoryModel.from_dict(s)


def product_category_model_to_dict(x: ProductCategoryModel) -> Any:
    return to_class(ProductCategoryModel, x)
