from api.model import Seller, Product
from api.schema import ProductSchema
from .db_base_service import DbChildBaseService


product_service = DbChildBaseService(
    model=Product, schema=ProductSchema,
    model_parent=Seller, parent_id_name='seller_id'
)
