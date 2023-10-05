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
class AdminAuthModel:
    admin_id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    sales_executive: Optional[str] = None
    profile_pic: Optional[str] = None
    address: Optional[str] = None
    document_1__type: Optional[str] = None
    document_1__url: Optional[str] = None
    document_2__type: Optional[str] = None
    document_2__url: Optional[str] = None
    status: Optional[int] = None
    created_by: Optional[int] = None
    last_updated_by: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminAuthModel':
        assert isinstance(obj, dict)
        admin_id = from_union([from_int, from_none], obj.get("admin_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        email = from_union([from_str, from_none], obj.get("email"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        password = from_union([from_str, from_none], obj.get("password"))
        sales_executive = from_union([from_str, from_none], obj.get("sales_executive"))
        profile_pic = from_union([from_str, from_none], obj.get("profile_pic"))
        address = from_union([from_str, from_none], obj.get("address"))
        document_1__type = from_union([from_str, from_none], obj.get("document_1_type"))
        document_1__url = from_union([from_str, from_none], obj.get("document_1_url"))
        document_2__type = from_union([from_str, from_none], obj.get("document_2_type"))
        document_2__url = from_union([from_str, from_none], obj.get("document_2_url"))
        status = from_union([from_int, from_none], obj.get("status"))
        created_by = from_union([from_int, from_none], obj.get("created_by"))
        last_updated_by = from_union([from_int, from_none], obj.get("last_updated_by"))
        return AdminAuthModel(admin_id, name, email, phone, password, sales_executive, profile_pic, address,
                              document_1__type, document_1__url, document_2__type, document_2__url, status, created_by,
                              last_updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.admin_id is not None:
            result["admin_id"] = from_union([from_int, from_none], self.admin_id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.phone is not None:
            result["phone"] = from_union([from_str, from_none], self.phone)
        if self.password is not None:
            result["password"] = from_union([from_str, from_none], self.password)
        if self.sales_executive is not None:
            result["sales_executive"] = from_union([from_str, from_none], self.sales_executive)
        if self.profile_pic is not None:
            result["profile_pic"] = from_union([from_str, from_none], self.profile_pic)
        if self.address is not None:
            result["address"] = from_union([from_str, from_none], self.address)
        if self.document_1__type is not None:
            result["document_1_type"] = from_union([from_str, from_none], self.document_1__type)
        if self.document_1__url is not None:
            result["document_1_url"] = from_union([from_str, from_none], self.document_1__url)
        if self.document_2__type is not None:
            result["document_2_type"] = from_union([from_str, from_none], self.document_2__type)
        if self.document_2__url is not None:
            result["document_2_url"] = from_union([from_str, from_none], self.document_2__url)
        if self.status is not None:
            result["status"] = from_union([from_int, from_none], self.status)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([from_int, from_none], self.last_updated_by)
        return result


def admin_auth_model_from_dict(s: Any) -> AdminAuthModel:
    return AdminAuthModel.from_dict(s)


def admin_auth_model_to_dict(x: AdminAuthModel) -> Any:
    return to_class(AdminAuthModel, x)
