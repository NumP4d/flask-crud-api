from flask import Blueprint, request
from api.service import product_service


product_api = Blueprint('product', __name__)


@product_api.route('/<int:seller_id>', methods=['GET'])
def get_seller_products(seller_id):
    return product_service.get_for_parent_id(seller_id)


@product_api.route('/<int:seller_id>', methods=['POST'])
def create_seller_product(seller_id):
    body = request.get_json()

    return product_service.create(body, seller_id)
