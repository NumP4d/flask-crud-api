from flask import Blueprint, request, jsonify
from api.model import db, Product, Seller
from api.schema import ProductSchema

product_api = Blueprint('product', __name__)

product_schemas = ProductSchema(many=True)


def check_for_seller_id(id):
    Seller.query.get_or_404(id,
        description=f'There is no seller with id {id}'
    )


@product_api.route('/', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify(product_schemas.dump(products))


@product_api.route('/<int:seller_id>', methods=['GET'])
def get_seller_products(seller_id):
    check_for_seller_id(seller_id)
    seller_products = Product.query.filter_by(seller_id=seller_id).all()
    return jsonify(product_schemas.dump(seller_products))


@product_api.route('/<int:seller_id>', methods=['POST'])
def create_seller_product(seller_id):
    check_for_seller_id(seller_id)
    body = request.get_json()
    try:
        product_name = body['name']
        new_product = Product(name=product_name, seller_id=seller_id)
        db.session.add(new_product)
        db.session.commit()
    except KeyError as exc:
        raise exc
    return 'product created'