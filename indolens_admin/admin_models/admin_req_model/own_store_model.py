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
class OwnStoreModel:
    store_zip_code: Optional[int] = None
    store_id: Optional[int] = None
    store_name: Optional[str] = None
    store_display_name: Optional[str] = None
    store_phone: Optional[str] = None
    store_gstin: Optional[str] = None
    store_email: Optional[str] = None
    store_city: Optional[str] = None
    store_state: Optional[str] = None
    store_lat_lng: Optional[str] = None
    complete_address: Optional[str] = None
    status: Optional[int] = None
    created_by: Optional[str] = None
    last_updated_by: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OwnStoreModel':
        assert isinstance(obj, dict)
        store_zip_code = from_union([from_none, lambda x: int(from_str(x))], obj.get("storeZipCode"))
        store_id = from_union([from_int, from_none], obj.get("store_id"))
        store_name = from_union([from_str, from_none], obj.get("storeName"))
        store_display_name = from_union([from_str, from_none], obj.get("storeDisplayName"))
        store_phone = from_union([from_str, from_none], obj.get("storePhone"))
        store_gstin = from_union([from_str, from_none], obj.get("storeGSTIN"))
        store_email = from_union([from_str, from_none], obj.get("storeEmail"))
        store_city = from_union([from_str, from_none], obj.get("storeCity"))
        store_state = from_union([from_str, from_none], obj.get("storeState"))
        store_lat_lng = from_union([from_str, from_none], obj.get("storeLatLng"))
        complete_address = from_union([from_str, from_none], obj.get("completeAddress"))
        status = from_union([from_int, from_none], obj.get("status"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        last_updated_by = from_union([from_str, from_none], obj.get("last_updated_by"))
        return OwnStoreModel(store_zip_code, store_id, store_name, store_display_name, store_phone, store_gstin, store_email, store_city, store_state, store_lat_lng, complete_address, status, created_by, last_updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.store_zip_code is not None:
            result["storeZipCode"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.store_zip_code)
        if self.store_id is not None:
            result["store_id"] = from_union([from_int, from_none], self.store_id)
        if self.store_name is not None:
            result["storeName"] = from_union([from_str, from_none], self.store_name)
        if self.store_display_name is not None:
            result["storeDisplayName"] = from_union([from_str, from_none], self.store_display_name)
        if self.store_phone is not None:
            result["storePhone"] = from_union([from_str, from_none], self.store_phone)
        if self.store_gstin is not None:
            result["storeGSTIN"] = from_union([from_str, from_none], self.store_gstin)
        if self.store_email is not None:
            result["storeEmail"] = from_union([from_str, from_none], self.store_email)
        if self.store_city is not None:
            result["storeCity"] = from_union([from_str, from_none], self.store_city)
        if self.store_state is not None:
            result["storeState"] = from_union([from_str, from_none], self.store_state)
        if self.store_lat_lng is not None:
            result["storeLatLng"] = from_union([from_str, from_none], self.store_lat_lng)
        if self.complete_address is not None:
            result["completeAddress"] = from_union([from_str, from_none], self.complete_address)
        if self.status is not None:
            result["status"] = from_union([from_int, from_none], self.status)
        if self.created_by is not None:
            result["created_by"] = from_union([from_str, from_none], self.created_by)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([from_str, from_none], self.last_updated_by)
        return result


def own_store_model_from_dict(s: Any) -> OwnStoreModel:
    return OwnStoreModel.from_dict(s)


def own_store_model_to_dict(x: OwnStoreModel) -> Any:
    return to_class(OwnStoreModel, x)
