from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .sellers import Seller
from .products import Product

__all__ = [
    'db',
    'Seller',
    'Product'
]
