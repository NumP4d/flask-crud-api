from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .sellers import Seller

__all__ = [
    'db',
    'Seller'
]