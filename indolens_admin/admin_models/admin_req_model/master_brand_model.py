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


class MasterBrandModel:
    brand_id: Optional[str]
    brand_name: Optional[str]
    category_id: Optional[int]
    brand_description: Optional[str]
    status: Optional[int]
    created_on: Optional[str]
    created_by: Optional[int]
    last_updated_on: Optional[str]
    last_updated_by: Optional[int]

    def __init__(self, brand_id: Optional[str], brand_name: Optional[str], category_id: Optional[int], brand_description: Optional[str], status: Optional[int], created_on: Optional[str], created_by: Optional[int], last_updated_on: Optional[str], last_updated_by: Optional[int]) -> None:
        self.brand_id = brand_id
        self.brand_name = brand_name
        self.category_id = category_id
        self.brand_description = brand_description
        self.status = status
        self.created_on = created_on
        self.created_by = created_by
        self.last_updated_on = last_updated_on
        self.last_updated_by = last_updated_by

    @staticmethod
    def from_dict(obj: Any) -> 'MasterBrandModel':
        assert isinstance(obj, dict)
        brand_id = from_union([from_str, from_none], obj.get("brand_id"))
        brand_name = from_union([from_str, from_none], obj.get("brand_name"))
        category_id = from_union([from_str, from_none], obj.get("category_id"))
        brand_description = from_union([from_str, from_none], obj.get("brand_description"))
        status = from_union([from_int, from_none], obj.get("status"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        last_updated_on = from_union([from_str, from_none], obj.get("last_updated_on"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        return MasterBrandModel(brand_id, brand_name, category_id, brand_description, status, created_on, created_by, last_updated_on, last_updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.brand_id is not None:
            result["brand_id"] = from_union([from_str, from_none], self.brand_id)
        if self.brand_name is not None:
            result["brand_name"] = from_union([from_str, from_none], self.brand_name)
        if self.category_id is not None:
            result["category_id"] = from_union([from_int, from_none], self.category_id)
        if self.brand_description is not None:
            result["brand_description"] = from_union([from_str, from_none], self.brand_description)
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


def master_brand_model_from_dict(s: Any) -> MasterBrandModel:
    return MasterBrandModel.from_dict(s)


def master_brand_model_to_dict(x: MasterBrandModel) -> Any:
    return to_class(MasterBrandModel, x)
