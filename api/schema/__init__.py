from flask_marshmallow import Marshmallow

ma = Marshmallow()

from .products_schema import ProductSchema
from .sellers_schema import SellerSchema
from .transactions_schema import TransactionSchema


__all__ = [
    'ma',
    'SellerSchema',
    'ProductSchema',
    'TransactionSchema'
]
