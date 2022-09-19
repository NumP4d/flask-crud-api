from . import db


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'),
        nullable=False)
    price = db.Column(db.Float(precision=53), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Transaction {self.id} for product {self.product_id}>"
