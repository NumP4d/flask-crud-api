from flask import Blueprint, request, jsonify
from api.model import db, Seller

seller_api = Blueprint('seller', __name__)

@seller_api.route('/', methods=['POST'])
def create_seller():
    body = request.get_json()
    try:
        seller_name = body['name']
        new_seller = Seller(name=seller_name)
        db.session.add(new_seller)
        db.session.commit()
    except KeyError as exc:
        raise exc
    return 'seller created'

@seller_api.route('/', methods=['GET'])
def get_sellers():
    sellers = []
    for seller in db.session.query(Seller).all():
        del seller.__dict__['_sa_instance_state']
        sellers.append(seller.__dict__)
    return jsonify(sellers)

@seller_api.route('/<id>', methods=['GET'])
def get_seller(id):
    seller = Seller.query.get(id)
    del seller.__dict__['_sa_instance_state']
    return jsonify(seller.__dict__)
