from dataclasses import dataclass
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


@dataclass
class LabTechnicianModel:
    lab_technician_id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    profile_pic: Optional[str] = None
    assigned_lab_id: Optional[int] = None
    address: Optional[str] = None
    document_1_type: Optional[str] = None
    document_1_url: Optional[str] = None
    document_2_type: Optional[str] = None
    document_2_url: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[int] = None
    created_on: Optional[str] = None
    last_updated_by: Optional[int] = None
    last_updated_on: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LabTechnicianModel':
        assert isinstance(obj, dict)
        lab_technician_id = from_union([from_int, from_none], obj.get("lab_technician_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        email = from_union([from_str, from_none], obj.get("email"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        password = from_union([from_str, from_none], obj.get("password"))
        profile_pic = from_union([from_str, from_none], obj.get("profile_pic"))
        assigned_lab_id = from_union([from_int, from_none], obj.get("assigned_lab_id"))
        address = from_union([from_str, from_none], obj.get("address"))
        document_1_type = from_union([from_str, from_none], obj.get("document_1_type"))
        document_1_url = from_union([from_str, from_none], obj.get("document_1_url"))
        document_2_type = from_union([from_str, from_none], obj.get("document_2_type"))
        document_2_url = from_union([from_str, from_none], obj.get("document_2_url"))
        status = from_union([from_str, from_none], obj.get("status"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        last_updated_on = from_union([from_str, from_none], obj.get("last_updated_on"))
        return LabTechnicianModel(lab_technician_id, name, email, phone, password, profile_pic, assigned_lab_id, address, document_1_type, document_1_url, document_2_type, document_2_url, status, created_by, created_on, last_updated_by, last_updated_on)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.lab_technician_id is not None:
            result["lab_technician_id"] = from_union([from_int, from_none], self.lab_technician_id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.phone is not None:
            result["phone"] = from_union([from_str, from_none], self.phone)
        if self.password is not None:
            result["password"] = from_union([from_str, from_none], self.password)
        if self.profile_pic is not None:
            result["profile_pic"] = from_union([from_str, from_none], self.profile_pic)
        if self.assigned_lab_id is not None:
            result["assigned_lab_id"] = from_union([from_int, from_none], self.assigned_lab_id)
        if self.address is not None:
            result["address"] = from_union([from_str, from_none], self.address)
        if self.document_1_type is not None:
            result["document_1_type"] = from_union([from_str, from_none], self.document_1_type)
        if self.document_1_url is not None:
            result["document_1_url"] = from_union([from_str, from_none], self.document_1_url)
        if self.document_2_type is not None:
            result["document_2_type"] = from_union([from_str, from_none], self.document_2_type)
        if self.document_2_url is not None:
            result["document_2_url"] = from_union([from_str, from_none], self.document_2_url)
        if self.status is not None:
            result["status"] = from_union([from_str, from_none], self.status)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        if self.created_on is not None:
            result["created_on"] = from_union([from_str, from_none], self.created_on)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([from_int, from_none], self.last_updated_by)
        if self.last_updated_on is not None:
            result["last_updated_on"] = from_union([from_str, from_none], self.last_updated_on)
        return result


def lab_technician_model_from_dict(s: Any) -> LabTechnicianModel:
    return LabTechnicianModel.from_dict(s)


def lab_technician_model_to_dict(x: LabTechnicianModel) -> Any:
    return to_class(LabTechnicianModel, x)
