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
    id: Optional[int] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    confirm_password: Optional[str] = None
    complete_address: Optional[str] = None
    document1_type: Optional[str] = None
    document2_type: Optional[str] = None
    profile_pic_profile_pic: Optional[str] = None
    documents_document1: Optional[str] = None
    documents_document2: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SubAdminModel':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        full_name = from_union([from_str, from_none], obj.get("fullName"))
        email = from_union([from_str, from_none], obj.get("email"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        password = from_union([from_str, from_none], obj.get("password"))
        confirm_password = from_union([from_str, from_none], obj.get("confirmPassword"))
        complete_address = from_union([from_str, from_none], obj.get("completeAddress"))
        document1_type = from_union([from_str, from_none], obj.get("document1Type"))
        document2_type = from_union([from_str, from_none], obj.get("document2Type"))
        profile_pic_profile_pic = from_union([from_str, from_none], obj.get("profile_pic_profilePic"))
        documents_document1 = from_union([from_str, from_none], obj.get("documents_document1"))
        documents_document2 = from_union([from_str, from_none], obj.get("documents_document2"))
        return SubAdminModel(id, full_name, email, phone, password, confirm_password, complete_address, document1_type, document2_type, profile_pic_profile_pic, documents_document1, documents_document2)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.id is not None:
            result["id"] = from_union([from_int, from_none], self.id)
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
        if self.document1_type is not None:
            result["document1Type"] = from_union([from_str, from_none], self.document1_type)
        if self.document2_type is not None:
            result["document2Type"] = from_union([from_str, from_none], self.document2_type)
        if self.profile_pic_profile_pic is not None:
            result["profile_pic_profilePic"] = from_union([from_str, from_none], self.profile_pic_profile_pic)
        if self.documents_document1 is not None:
            result["documents_document1"] = from_union([from_str, from_none], self.documents_document1)
        if self.documents_document2 is not None:
            result["documents_document2"] = from_union([from_str, from_none], self.documents_document2)
        return result


def sub_admin_model_from_dict(s: Any) -> SubAdminModel:
    return SubAdminModel.from_dict(s)


def sub_admin_model_to_dict(x: SubAdminModel) -> Any:
    return to_class(SubAdminModel, x)
