from flask import jsonify, abort
from sqlalchemy.exc import IntegrityError
from api.model import db, Seller, Product
from api.schema import ProductSchema

_product_schemas = ProductSchema(many=True)


def _check_for_seller_id(id):
    Seller.query.get_or_404(id,
        description=f'There is no seller with id {id}'
    )


def get_seller_products_service(seller_id):
    _check_for_seller_id(seller_id)
    seller_products = Product.query.filter_by(seller_id=seller_id).all()
    return jsonify(_product_schemas.dump(seller_products))


def create_seller_product_serivce(seller_id, body):
    _check_for_seller_id(seller_id)
    try:
        product_name = body['name']
    except KeyError:
        abort(400, f'You must pass product attributes: name')

    new_product = Product(name=product_name, seller_id=seller_id)
    try:
        db.session.add(new_product)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, f'The product of name {product_name} already exists!')

    return 'Product created.'
