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
class SubAdminModel:
    admin_id: Optional[int] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    confirm_password: Optional[str] = None
    complete_address: Optional[str] = None
    document_1_type: Optional[str] = None
    document_2_type: Optional[str] = None
    profile_pic: Optional[str] = None
    document1: Optional[str] = None
    document2: Optional[str] = None
    created_by: Optional[int] = None
    last_updated_by: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SubAdminModel':
        assert isinstance(obj, dict)
        admin_id = from_union([from_int, from_none], obj.get("admin_id"))
        full_name = from_union([from_str, from_none], obj.get("fullName"))
        email = from_union([from_str, from_none], obj.get("email"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        password = from_union([from_str, from_none], obj.get("password"))
        confirm_password = from_union([from_str, from_none], obj.get("confirmPassword"))
        complete_address = from_union([from_str, from_none], obj.get("completeAddress"))
        document_1_type = from_union([from_str, from_none], obj.get("document1Type"))
        document_2_type = from_union([from_str, from_none], obj.get("document2Type"))
        profile_pic = from_union([from_str, from_none], obj.get("profilePic"))
        document1 = from_union([from_str, from_none], obj.get("document1"))
        document2 = from_union([from_str, from_none], obj.get("document2"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        return SubAdminModel(admin_id, full_name, email, phone, password, confirm_password, complete_address, document_1_type, document_2_type, profile_pic, document1, document2, created_by, last_updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.admin_id is not None:
            result["admin_id"] = from_union([from_int, from_none], self.admin_id)
        if self.full_name is not None:
            result["fullName"] = from_union([from_str, from_none], self.full_name)
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.phone is not None:
            result["phone"] = from_union([from_str, from_none], self.phone)
        if self.password is not None:
            result["password"] = from_union([from_str, from_none], self.password)
        if self.confirm_password is not None:
            result["confirmPassword"] = from_union([from_str, from_none], self.confirm_password)
        if self.complete_address is not None:
            result["completeAddress"] = from_union([from_str, from_none], self.complete_address)
        if self.document_1_type is not None:
            result["document1Type"] = from_union([from_str, from_none], self.document_1_type)
        if self.document_2_type is not None:
            result["document2Type"] = from_union([from_str, from_none], self.document_2_type)
        if self.profile_pic is not None:
            result["profilePic"] = from_union([from_str, from_none], self.profile_pic)
        if self.document1 is not None:
            result["document1"] = from_union([from_str, from_none], self.document1)
        if self.document2 is not None:
            result["document2"] = from_union([from_str, from_none], self.document2)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([from_int, from_none], self.last_updated_by)
        return result


def sub_admin_model_from_dict(s: Any) -> SubAdminModel:
    return SubAdminModel.from_dict(s)


def sub_admin_model_to_dict(x: SubAdminModel) -> Any:
    return to_class(SubAdminModel, x)
