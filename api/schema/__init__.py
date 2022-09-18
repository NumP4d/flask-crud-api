from flask_marshmallow import Marshmallow

ma = Marshmallow()

from .products_schema import ProductSchema
from .sellers_schema import SellerSchema

__all__ = [
    'ma',
    'ProductSchema'
]
