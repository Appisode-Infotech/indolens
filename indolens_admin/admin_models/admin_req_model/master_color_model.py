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


class MasterColorModel:
    color_id: Optional[str]
    color_code: Optional[str]
    color_name: Optional[str]
    color_description: Optional[str]
    status: Optional[int]
    created_on: Optional[str]
    created_by: Optional[int]
    last_updated_on: Optional[str]
    last_updated_by: Optional[int]

    def __init__(self, color_id: Optional[str], color_code: Optional[str], color_name: Optional[str], color_description: Optional[str], status: Optional[int], created_on: Optional[str], created_by: Optional[int], last_updated_on: Optional[str], last_updated_by: Optional[int]) -> None:
        self.color_id = color_id
        self.color_code = color_code
        self.color_name = color_name
        self.color_description = color_description
        self.status = status
        self.created_on = created_on
        self.created_by = created_by
        self.last_updated_on = last_updated_on
        self.last_updated_by = last_updated_by

    @staticmethod
    def from_dict(obj: Any) -> 'MasterColorModel':
        assert isinstance(obj, dict)
        color_id = from_union([from_str, from_none], obj.get("color_id"))
        color_code = from_union([from_str, from_none], obj.get("color_code"))
        color_name = from_union([from_str, from_none], obj.get("color_name"))
        color_description = from_union([from_str, from_none], obj.get("color_description"))
        status = from_union([from_int, from_none], obj.get("status"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        last_updated_on = from_union([from_str, from_none], obj.get("last_updated_on"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        return MasterColorModel(color_id, color_code, color_name, color_description, status, created_on, created_by, last_updated_on, last_updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.color_id is not None:
            result["color_id"] = from_union([from_str, from_none], self.color_id)
        if self.color_code is not None:
            result["color_code"] = from_union([from_str, from_none], self.color_code)
        if self.color_name is not None:
            result["color_name"] = from_union([from_str, from_none], self.color_name)
        if self.color_description is not None:
            result["color_description"] = from_union([from_str, from_none], self.color_description)
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


def master_color_model_from_dict(s: Any) -> MasterColorModel:
    return MasterColorModel.from_dict(s)


def master_color_model_to_dict(x: MasterColorModel) -> Any:
    return to_class(MasterColorModel, x)
