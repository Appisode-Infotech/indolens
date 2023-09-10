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


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AreaHeadModel:
    created_by: Optional[int] = None
    last_updated_by: Optional[int] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    confirm_password: Optional[str] = None
    complete_address: Optional[str] = None
    document1_type: Optional[str] = None
    document2_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AreaHeadModel':
        assert isinstance(obj, dict)
        created_by = from_union([from_none, lambda x: int(from_str(x))], obj.get("created_by"))
        last_updated_by = from_union([from_none, lambda x: int(from_str(x))], obj.get("last_updated_by"))
        full_name = from_union([from_str, from_none], obj.get("fullName"))
        email = from_union([from_str, from_none], obj.get("email"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        password = from_union([from_str, from_none], obj.get("password"))
        confirm_password = from_union([from_str, from_none], obj.get("confirmPassword"))
        complete_address = from_union([from_str, from_none], obj.get("completeAddress"))
        document1_type = from_union([from_str, from_none], obj.get("document1Type"))
        document2_type = from_union([from_str, from_none], obj.get("document2Type"))
        return AreaHeadModel(created_by, last_updated_by, full_name, email, phone, password, confirm_password, complete_address, document1_type, document2_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.created_by is not None:
            result["created_by"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.created_by)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.last_updated_by)
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
        return result


def area_head_model_from_dict(s: Any) -> AreaHeadModel:
    return AreaHeadModel.from_dict(s)


def area_head_model_to_dict(x: AreaHeadModel) -> Any:
    return to_class(AreaHeadModel, x)
