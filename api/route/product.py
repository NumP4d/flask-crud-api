from flask import Blueprint, request
from api.service import (
    get_seller_products_service,
    create_seller_product_serivce
)


product_api = Blueprint('product', __name__)


@product_api.route('/<int:seller_id>', methods=['GET'])
def get_seller_products(seller_id):
    return get_seller_products_service(seller_id)


@product_api.route('/<int:seller_id>', methods=['POST'])
def create_seller_product(seller_id):
    body = request.get_json()

    return create_seller_product_serivce(seller_id, body)
