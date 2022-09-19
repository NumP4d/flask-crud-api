from . import db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'),
        nullable=False)
    transactions = db.relationship('Transaction',
        backref=db.backref('products', lazy=True))

    def __repr__(self):
        return f"<Product {self.name} for seller id {self.seller_id}>"
