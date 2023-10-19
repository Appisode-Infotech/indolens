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


class InventoryAddProducts:
    product_id: Optional[int]
    product_title: Optional[str]
    product_description: Optional[str]
    product_images: Optional[str]
    category_id: Optional[int]
    brand_id: Optional[int]
    material_id: Optional[int]
    frame_type_id: Optional[int]
    frame_shape_id: Optional[int]
    color_id: Optional[int]
    unit_id: Optional[int]
    origin: Optional[str]
    cost_price: Optional[int]
    sale_price: Optional[int]
    model_number: Optional[str]
    hsn_number: Optional[str]
    created_on: Optional[str]
    created_by: Optional[int]
    last_updated_on: Optional[str]
    last_updated_by: Optional[int]

    def __init__(self, product_id: Optional[int], product_title: Optional[str], product_description: Optional[str], product_images: Optional[str], category_id: Optional[int], brand_id: Optional[int], material_id: Optional[int], frame_type_id: Optional[int], frame_shape_id: Optional[int], color_id: Optional[int], unit_id: Optional[int], origin: Optional[str], cost_price: Optional[int], sale_price: Optional[int], model_number: Optional[str], hsn_number: Optional[str], created_on: Optional[str], created_by: Optional[int], last_updated_on: Optional[str], last_updated_by: Optional[int]) -> None:
        self.product_id = product_id
        self.product_title = product_title
        self.product_description = product_description
        self.product_images = product_images
        self.category_id = category_id
        self.brand_id = brand_id
        self.material_id = material_id
        self.frame_type_id = frame_type_id
        self.frame_shape_id = frame_shape_id
        self.color_id = color_id
        self.unit_id = unit_id
        self.origin = origin
        self.cost_price = cost_price
        self.sale_price = sale_price
        self.model_number = model_number
        self.hsn_number = hsn_number
        self.created_on = created_on
        self.created_by = created_by
        self.last_updated_on = last_updated_on
        self.last_updated_by = last_updated_by

    @staticmethod
    def from_dict(obj: Any) -> 'InventoryAddProducts':
        assert isinstance(obj, dict)
        product_id = from_union([from_int, from_none], obj.get("product_id"))
        product_title = from_union([from_str, from_none], obj.get("productTitle"))
        product_description = from_union([from_str, from_none], obj.get("productDescription"))
        product_images = from_union([from_str, from_none], obj.get("productImages"))
        category_id = from_union([from_int, from_none], obj.get("categoryId"))
        brand_id = from_union([from_int, from_none], obj.get("brandId"))
        material_id = from_union([from_int, from_none], obj.get("materialId"))
        frame_type_id = from_union([from_int, from_none], obj.get("frameTypeId"))
        frame_shape_id = from_union([from_int, from_none], obj.get("frameShapeId"))
        color_id = from_union([from_int, from_none], obj.get("colorId"))
        unit_id = from_union([from_int, from_none], obj.get("unitId"))
        origin = from_union([from_str, from_none], obj.get("origin"))
        cost_price = from_union([from_int, from_none], obj.get("costPrice"))
        sale_price = from_union([from_int, from_none], obj.get("salePrice"))
        model_number = from_union([from_str, from_none], obj.get("modelNumber"))
        hsn_number = from_union([from_str, from_none], obj.get("hsnNumber"))
        created_on = from_union([from_str, from_none], obj.get("created_on"))
        created_by = from_union([from_int, from_none], obj.get("created_by"))
        last_updated_on = from_union([from_str, from_none], obj.get("last_updated_on"))
        last_updated_by = from_union([from_int, from_none], obj.get("last_updated_by"))
        return InventoryAddProducts(product_id, product_title, product_description, product_images, category_id, brand_id, material_id, frame_type_id, frame_shape_id, color_id, unit_id, origin, cost_price, sale_price, model_number, hsn_number, created_on, created_by, last_updated_on, last_updated_by)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.product_id is not None:
            result["product_id"] = from_union([from_int, from_none], self.product_id)
        if self.product_title is not None:
            result["productTitle"] = from_union([from_str, from_none], self.product_title)
        if self.product_description is not None:
            result["productDescription"] = from_union([from_str, from_none], self.product_description)
        if self.product_images is not None:
            result["productImages"] = from_union([from_str, from_none], self.product_images)
        if self.category_id is not None:
            result["categoryId"] = from_union([from_str, from_none], self.category_id)
        if self.brand_id is not None:
            result["brandId"] = from_union([from_str, from_none], self.brand_id)
        if self.material_id is not None:
            result["materialId"] = from_union([from_str, from_none], self.material_id)
        if self.frame_type_id is not None:
            result["frameTypeId"] = from_union([from_str, from_none], self.frame_type_id)
        if self.frame_shape_id is not None:
            result["frameShapeId"] = from_union([from_str, from_none], self.frame_shape_id)
        if self.color_id is not None:
            result["colorId"] = from_union([from_str, from_none], self.color_id)
        if self.unit_id is not None:
            result["unitId"] = from_union([from_str, from_none], self.unit_id)
        if self.origin is not None:
            result["origin"] = from_union([from_str, from_none], self.origin)
        if self.cost_price is not None:
            result["costPrice"] = from_union([from_str, from_none], self.cost_price)
        if self.sale_price is not None:
            result["salePrice"] = from_union([from_str, from_none], self.sale_price)
        if self.model_number is not None:
            result["modelNumber"] = from_union([from_str, from_none], self.model_number)
        if self.hsn_number is not None:
            result["hsnNumber"] = from_union([from_str, from_none], self.hsn_number)
        if self.created_on is not None:
            result["created_on"] = from_union([from_str, from_none], self.created_on)
        if self.created_by is not None:
            result["created_by"] = from_union([from_int, from_none], self.created_by)
        if self.last_updated_on is not None:
            result["last_updated_on"] = from_union([from_str, from_none], self.last_updated_on)
        if self.last_updated_by is not None:
            result["last_updated_by"] = from_union([from_str, from_none], self.last_updated_by)
        return result


def inventory_add_products_from_dict(s: Any) -> InventoryAddProducts:
    return InventoryAddProducts.from_dict(s)


def inventory_add_products_to_dict(x: InventoryAddProducts) -> Any:
    return to_class(InventoryAddProducts, x)
