from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast

T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class LabModel:
    lab_zip_code: Optional[int] = None
    lab_id: Optional[int] = None
    status: Optional[int] = None
    created_by: Optional[int] = None
    last_updated_by: Optional[int] = None
    created_on: Optional[str] = None
    last_updated_on: Optional[str] = None
    lab_name: Optional[str] = None
    lab_display_name: Optional[str] = None
    lab_phone: Optional[str] = None
    lab_gstin: Optional[str] = None
    lab_email: Optional[str] = None
    lab_city: Optional[str] = None
    lab_state: Optional[str] = None
    complete_address: Optional[str] = None
    lab_lat_lng: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LabModel':
        assert isinstance(obj, dict)
        lab_zip_code = from_union([from_none, lambda x: int(from_str(x))], obj.get("labZipCode"))
        lab_id = from_union([from_str, from_none], obj.get("labId"))
        status = from_union([from_int, from_none], obj.get("status"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        last_updated_on = from_union([from_str, from_none], obj.get("last_updated_on"))
        lab_name = from_union([from_str, from_none], obj.get("labName"))
        lab_display_name = from_union([from_str, from_none], obj.get("labDisplayName"))
        lab_phone = from_union([from_str, from_none], obj.get("labPhone"))
        lab_gstin = from_union([from_str, from_none], obj.get("labGSTIN"))
        lab_email = from_union([from_str, from_none], obj.get("labEmail"))
        lab_city = from_union([from_str, from_none], obj.get("labCity"))
        lab_state = from_union([from_str, from_none], obj.get("labState"))
        complete_address = from_union([from_str, from_none], obj.get("completeAddress"))
        lab_lat_lng = from_union([from_str, from_none], obj.get("lab_lat_lng"))
        return LabModel(lab_zip_code, lab_id, status, created_by, last_updated_by, created_on, last_updated_on,
                        lab_name, lab_display_name, lab_phone, lab_gstin, lab_email, lab_city, lab_state,
                        complete_address, lab_lat_lng)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.lab_zip_code is not None:
            result["labZipCode"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)),
                                               lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))],
                                              self.lab_zip_code)
        if self.lab_id is not None:
            result["labId"] = from_union([from_int, from_none], self.lab_id)
        if self.status is not None:
            result["status"] = from_union([from_int, from_none], self.status)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([from_int, from_none], self.last_updated_by)
        if self.created_on is not None:
            result["created_on"] = from_union([from_str, from_none], self.created_on)
        if self.last_updated_on is not None:
            result["last_updated_on"] = from_union([from_str, from_none], self.last_updated_on)
        if self.lab_name is not None:
            result["labName"] = from_union([from_str, from_none], self.lab_name)
        if self.lab_display_name is not None:
            result["labDisplayName"] = from_union([from_str, from_none], self.lab_display_name)
        if self.lab_phone is not None:
            result["labPhone"] = from_union([from_str, from_none], self.lab_phone)
        if self.lab_gstin is not None:
            result["labGSTIN"] = from_union([from_str, from_none], self.lab_gstin)
        if self.lab_email is not None:
            result["labEmail"] = from_union([from_str, from_none], self.lab_email)
        if self.lab_city is not None:
            result["labCity"] = from_union([from_str, from_none], self.lab_city)
        if self.lab_state is not None:
            result["labState"] = from_union([from_str, from_none], self.lab_state)
        if self.complete_address is not None:
            result["completeAddress"] = from_union([from_str, from_none], self.complete_address)
        if self.lab_lat_lng is not None:
            result["lab_lat_lng"] = from_union([from_str, from_none], self.lab_lat_lng)
        return result


def lab_model_from_dict(s: Any) -> LabModel:
    return LabModel.from_dict(s)


def lab_model_to_dict(x: LabModel) -> Any:
    return to_class(LabModel, x)
