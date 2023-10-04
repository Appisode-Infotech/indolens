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


class MasterFrameTypeModel:
    frame_id: Optional[str]
    frame_type_name: Optional[str]
    frame_type_description: Optional[str]
    status: Optional[int]
    created_on: Optional[str]
    created_by: Optional[int]
    last_updated_on: Optional[str]
    last_updated_by: Optional[int]

    def __init__(self, frame_id: Optional[str], frame_type_name: Optional[str], frame_type_description: Optional[str], status: Optional[int], created_on: Optional[str], created_by: Optional[int], last_updated_on: Optional[str], last_updated_by: Optional[int]) -> None:
        self.frame_id = frame_id
        self.frame_type_name = frame_type_name
        self.frame_type_description = frame_type_description
        self.status = status
        self.created_on = created_on
        self.created_by = created_by
        self.last_updated_on = last_updated_on
        self.last_updated_by = last_updated_by

    @staticmethod
    def from_dict(obj: Any) -> 'MasterFrameTypeModel':
        assert isinstance(obj, dict)
        frame_id = from_union([from_str, from_none], obj.get("frame_id"))
        frame_type_name = from_union([from_str, from_none], obj.get("frame_type_name"))
        frame_type_description = from_union([from_str, from_none], obj.get("frame_type_description"))
        status = from_union([from_int, from_none], obj.get("status"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        last_updated_on = from_union([from_str, from_none], obj.get("last_updated_on"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        return MasterFrameTypeModel(frame_id, frame_type_name, frame_type_description, status, created_on, created_by, last_updated_on, last_updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.frame_id is not None:
            result["frame_id"] = from_union([from_str, from_none], self.frame_id)
        if self.frame_type_name is not None:
            result["frame_type_name"] = from_union([from_str, from_none], self.frame_type_name)
        if self.frame_type_description is not None:
            result["frame_type_description"] = from_union([from_str, from_none], self.frame_type_description)
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


def master_frame_type_model_from_dict(s: Any) -> MasterFrameTypeModel:
    return MasterFrameTypeModel.from_dict(s)


def master_frame_type_model_to_dict(x: MasterFrameTypeModel) -> Any:
    return to_class(MasterFrameTypeModel, x)
