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
class MarketingHeadModel:
    marketing_head_id: Optional[int] = None
    fullName: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    profile_pic: Optional[str] = None
    assigned_area_head: Optional[int] = None
    completeAddress: Optional[str] = None
    document_1_type: Optional[str] = None
    document_1_url: Optional[str] = None
    document_2_type: Optional[str] = None
    document_2_url: Optional[str] = None
    status: Optional[int] = None
    created_by: Optional[int] = None
    created_on: Optional[str] = None
    last_updated_by: Optional[int] = None
    last_updated_on: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MarketingHeadModel':
        assert isinstance(obj, dict)
        marketing_head_id = from_union([from_int, from_none], obj.get("marketing_head_id"))
        fullName = from_union([from_str, from_none], obj.get("fullName"))
        email = from_union([from_str, from_none], obj.get("email"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        password = from_union([from_str, from_none], obj.get("password"))
        profile_pic = from_union([from_str, from_none], obj.get("profile_pic"))
        assigned_area_head = from_union([from_int, from_none], obj.get("assigned_area_head"))
        completeAddress = from_union([from_str, from_none], obj.get("completeAddress"))
        document_1_type = from_union([from_str, from_none], obj.get("document1Type"))
        document_1_url = from_union([from_str, from_none], obj.get("document_1_url"))
        document_2_type = from_union([from_str, from_none], obj.get("document2Type"))
        document_2_url = from_union([from_str, from_none], obj.get("document_2_url"))
        status = from_union([from_int, from_none], obj.get("status"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        last_updated_on = from_union([from_str, from_none], obj.get("last_updated_on"))
        return MarketingHeadModel(marketing_head_id, fullName, email, phone, password, profile_pic, assigned_area_head,
                                  completeAddress, document_1_type, document_1_url, document_2_type, document_2_url,
                                  status, created_by, created_on, last_updated_by, last_updated_on)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.marketing_head_id is not None:
            result["marketing_head_id"] = from_union([from_int, from_none], self.marketing_head_id)
        if self.fullName is not None:
            result["fullName"] = from_union([from_str, from_none], self.fullName)
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.phone is not None:
            result["phone"] = from_union([from_str, from_none], self.phone)
        if self.password is not None:
            result["password"] = from_union([from_str, from_none], self.password)
        if self.profile_pic is not None:
            result["profile_pic"] = from_union([from_str, from_none], self.profile_pic)
        if self.assigned_area_head is not None:
            result["assigned_area_head"] = from_union([from_int, from_none], self.assigned_area_head)
        if self.completeAddress is not None:
            result["completeAddress"] = from_union([from_str, from_none], self.completeAddress)
        if self.document_1_type is not None:
            result["document1Type"] = from_union([from_str, from_none], self.document_1_type)
        if self.document_1_url is not None:
            result["document_1_url"] = from_union([from_str, from_none], self.document_1_url)
        if self.document_2_type is not None:
            result["document2Type"] = from_union([from_str, from_none], self.document_2_type)
        if self.document_2_url is not None:
            result["document_2_url"] = from_union([from_str, from_none], self.document_2_url)
        if self.status is not None:
            result["status"] = from_union([from_int, from_none], self.status)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        if self.created_on is not None:
            result["created_on"] = from_union([from_str, from_none], self.created_on)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([from_int, from_none], self.last_updated_by)
        if self.last_updated_on is not None:
            result["last_updated_on"] = from_union([from_str, from_none], self.last_updated_on)
        return result


def marketing_head_model_from_dict(s: Any) -> MarketingHeadModel:
    return MarketingHeadModel.from_dict(s)


def marketing_head_model_to_dict(x: MarketingHeadModel) -> Any:
    return to_class(MarketingHeadModel, x)
