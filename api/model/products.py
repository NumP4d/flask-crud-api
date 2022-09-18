from . import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'),
        nullable=False)

    def __repr__(self):
        return f"<Product {self.name} for seller id {self.seller_id}>"