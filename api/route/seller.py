from flask import Blueprint, request, jsonify
from api.model import db, Seller
from api.schema import SellerSchema


seller_api = Blueprint('seller', __name__)

seller_schema = SellerSchema()
seller_schemas = SellerSchema(many=True)

@seller_api.route('/', methods=['GET'])
def get_sellers():
    sellers = Seller.query.all()
    return jsonify(seller_schemas.dump(sellers))


@seller_api.route('/', methods=['POST'])
def create_seller():
    body = request.get_json()
    try:
        seller_name = body['name']
        country_code = body['country_code']
        new_seller = Seller(name=seller_name, country_code=country_code)
        db.session.add(new_seller)
        db.session.commit()
    except KeyError as exc:
        raise exc
    return 'seller created'


@seller_api.route('/<id>', methods=['GET'])
def get_seller(id):
    seller = Seller.query.get(id)
    return jsonify(seller_schema.dump(seller))
