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


class MasterMaterialModel:
    material_id: Optional[str]
    material_name: Optional[str]
    material_description: Optional[str]
    status: Optional[int]
    created_on: Optional[str]
    created_by: Optional[int]
    last_updated_on: Optional[str]
    last_updated_by: Optional[int]

    def __init__(self, material_id: Optional[str], material_name: Optional[str], material_description: Optional[str], status: Optional[int], created_on: Optional[str], created_by: Optional[int], last_updated_on: Optional[str], last_updated_by: Optional[int]) -> None:
        self.material_id = material_id
        self.material_name = material_name
        self.material_description = material_description
        self.status = status
        self.created_on = created_on
        self.created_by = created_by
        self.last_updated_on = last_updated_on
        self.last_updated_by = last_updated_by

    @staticmethod
    def from_dict(obj: Any) -> 'MasterMaterialModel':
        assert isinstance(obj, dict)
        material_id = from_union([from_str, from_none], obj.get("material_id"))
        material_name = from_union([from_str, from_none], obj.get("material_name"))
        material_description = from_union([from_str, from_none], obj.get("material_description"))
        status = from_union([from_int, from_none], obj.get("status"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        last_updated_on = from_union([from_str, from_none], obj.get("last_updated_on"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        return MasterMaterialModel(material_id, material_name, material_description, status, created_on, created_by, last_updated_on, last_updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.material_id is not None:
            result["material_id"] = from_union([from_str, from_none], self.material_id)
        if self.material_name is not None:
            result["material_name"] = from_union([from_str, from_none], self.material_name)
        if self.material_description is not None:
            result["material_description"] = from_union([from_str, from_none], self.material_description)
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


def master_material_model_from_dict(s: Any) -> MasterMaterialModel:
    return MasterMaterialModel.from_dict(s)


def master_material_model_to_dict(x: MasterMaterialModel) -> Any:
    return to_class(MasterMaterialModel, x)
