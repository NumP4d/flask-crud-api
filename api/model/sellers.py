from . import db
from iso3166 import countries


class Seller(db.Model):
    __tablename__ = 'sellers'
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    products = db.relationship('Product',
        backref=db.backref('sellers', lazy=True))

    def __repr__(self):
        country_name = countries.get(self.country_code).name
        return f"<Seller {self.name}, country: {country_name}>"

    def __init__(self, country_code, name):
        if country_code not in countries:
            raise KeyError("Incorrect country code")
        if not isinstance(country_code, int):
            country_code = countries.get(country_code).numeric
        self.country_code = country_code
        self.name = name
