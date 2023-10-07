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


class StoreEmployee:
    employee_id: Optional[int]
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    password: Optional[str]
    profile_pic: Optional[str]
    assigned_store_id: Optional[int]
    address: Optional[str]
    document_1_type: Optional[str]
    document_1_url: Optional[str]
    document_2_type: Optional[str]
    document_2_url: Optional[str]
    status: Optional[int]
    role: Optional[int]
    created_by: Optional[int]
    created_on: Optional[str]
    last_updated_by: Optional[int]
    last_updated_on: Optional[str]

    def __init__(self, employee_id: Optional[int], name: Optional[str], email: Optional[str], phone: Optional[str], password: Optional[str], profile_pic: Optional[str], assigned_store_id: Optional[int], address: Optional[str], document_1_type: Optional[str], document_1_url: Optional[str], document_2_type: Optional[str], document_2_url: Optional[str], status: Optional[int], role: Optional[int], created_by: Optional[int], created_on: Optional[str], last_updated_by: Optional[int], last_updated_on: Optional[str]) -> None:
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.profile_pic = profile_pic
        self.assigned_store_id = assigned_store_id
        self.address = address
        self.document_1_type = document_1_type
        self.document_1_url = document_1_url
        self.document_2_type = document_2_type
        self.document_2_url = document_2_url
        self.status = status
        self.role = role
        self.created_by = created_by
        self.created_on = created_on
        self.last_updated_by = last_updated_by
        self.last_updated_on = last_updated_on

    @staticmethod
    def from_dict(obj: Any) -> 'StoreEmployee':
        assert isinstance(obj, dict)
        employee_id = from_union([from_int, from_none], obj.get("employee_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        email = from_union([from_str, from_none], obj.get("email"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        password = from_union([from_str, from_none], obj.get("password"))
        profile_pic = from_union([from_str, from_none], obj.get("profile_pic"))
        assigned_store_id = from_union([from_int, from_none], obj.get("assigned_store_id"))
        address = from_union([from_str, from_none], obj.get("address"))
        document_1_type = from_union([from_str, from_none], obj.get("document_1_type"))
        document_1_url = from_union([from_str, from_none], obj.get("document_1_url"))
        document_2_type = from_union([from_str, from_none], obj.get("document_2_type"))
        document_2_url = from_union([from_str, from_none], obj.get("document_2_url"))
        status = from_union([from_int, from_none], obj.get("status"))
        role = from_union([from_int, from_none], obj.get("role"))
        created_by = from_union([from_int, from_none], obj.get("created_by"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        last_updated_by = from_union([from_int, from_none], obj.get("last_updated_by"))
        last_updated_on = from_union([from_str, from_none], obj.get("last_updated_on"))
        return StoreEmployee(employee_id, name, email, phone, password, profile_pic, assigned_store_id, address, document_1_type, document_1_url, document_2_type, document_2_url, status, role, created_by, created_on, last_updated_by, last_updated_on)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.employee_id is not None:
            result["employee_id"] = from_union([from_int, from_none], self.employee_id)
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
        if self.assigned_store_id is not None:
            result["assigned_store_id"] = from_union([from_int, from_none], self.assigned_store_id)
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
            result["status"] = from_union([from_int, from_none], self.status)
        if self.role is not None:
            result["role"] = from_union([from_int, from_none], self.role)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        if self.created_on is not None:
            result["created_on"] = from_union([from_str, from_none], self.created_on)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([from_int, from_none], self.last_updated_by)
        if self.last_updated_on is not None:
            result["last_updated_on"] = from_union([from_str, from_none], self.last_updated_on)
        return result


def store_employee_from_dict(s: Any) -> StoreEmployee:
    return StoreEmployee.from_dict(s)


def store_employee_to_dict(x: StoreEmployee) -> Any:
    return to_class(StoreEmployee, x)
