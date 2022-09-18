from flask import jsonify, abort
from sqlalchemy.exc import IntegrityError
from api.model import db, Seller
from api.schema import SellerSchema

_seller_schema = SellerSchema()
_seller_schemas = SellerSchema(many=True)


def get_all_sellers_service():
    sellers = Seller.query.all()
    return jsonify(_seller_schemas.dump(sellers))


def get_seller_service(seller_id):
    seller = Seller.query.get_or_404(seller_id,
        description=f'There is no seller with id {seller_id}')
    return jsonify(_seller_schema.dump(seller))


def create_seller_serivce(body):
    try:
        seller_name = body['name']
        country_code = body['country_code']
    except KeyError:
        abort(400, f'You must pass seller attributes: name and country_code')

    new_seller = Seller(name=seller_name, country_code=country_code)
    try:
        db.session.add(new_seller)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, f'The seller of name {seller_name} already exists!')

    return 'Seller created.'
