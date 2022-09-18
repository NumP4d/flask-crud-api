from flask_marshmallow import Marshmallow

ma = Marshmallow()

from .products_schema import ProductSchema

__all__ = [
    'ma',
    'ProductSchema'
]