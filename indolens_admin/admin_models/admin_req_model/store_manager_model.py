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
class StoreManagerModel:
    store_manager_id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None
    assigned_store_id: Optional[str] = None
    address: Optional[str] = None
    document_1_type: Optional[str] = None
    document_2_type: Optional[str] = None
    status: Optional[int] = None
    created_by: Optional[int] = None
    last_updated_by: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StoreManagerModel':
        assert isinstance(obj, dict)
        store_manager_id = from_union([from_int, from_none], obj.get("store_manager_id"))
        name = from_union([from_str, from_none], obj.get("fullName"))
        email = from_union([from_str, from_none], obj.get("email"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        password = from_union([from_str, from_none], obj.get("password"))
        assigned_store_id = from_union([from_str, from_none], obj.get("assigned_store_id"))
        address = from_union([from_str, from_none], obj.get("completeAddress"))
        document_1_type = from_union([from_str, from_none], obj.get("document1Type"))
        document_2_type = from_union([from_str, from_none], obj.get("document2Type"))
        status = from_union([from_int, from_none], obj.get("status"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        return StoreManagerModel(store_manager_id, name, email, phone, password, assigned_store_id, address, document_1_type, document_2_type, status, created_by, last_updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.store_manager_id is not None:
            result["store_manager_id"] = from_union([from_int, from_none], self.store_manager_id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.email is not None:
            result["email"] = from_union([from_str, from_none], self.email)
        if self.phone is not None:
            result["phone"] = from_union([from_str, from_none], self.phone)
        if self.password is not None:
            result["password"] = from_union([from_str, from_none], self.password)
        if self.assigned_store_id is not None:
            result["assigned_store_id"] = from_union([from_str, from_none], self.assigned_store_id)
        if self.address is not None:
            result["address"] = from_union([from_str, from_none], self.address)
        if self.document_1_type is not None:
            result["document_1_type"] = from_union([from_str, from_none], self.document_1_type)
        if self.document_2_type is not None:
            result["document_2_type"] = from_union([from_str, from_none], self.document_2_type)
        if self.status is not None:
            result["status"] = from_union([from_int, from_none], self.status)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([from_int, from_none], self.last_updated_by)
        return result


def store_manager_model_from_dict(s: Any) -> StoreManagerModel:
    return StoreManagerModel.from_dict(s)


def store_manager_model_to_dict(x: StoreManagerModel) -> Any:
    return to_class(StoreManagerModel, x)
