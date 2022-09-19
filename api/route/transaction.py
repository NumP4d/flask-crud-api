from flask import Blueprint, request
from api.service import transaction_service


transaction_api = Blueprint('transaction', __name__)


@transaction_api.route('/<int:product_id>', methods=['GET'])
def get_seller_products(product_id):
    return transaction_service.get_for_parent_id(product_id)


@transaction_api.route('/<int:product_id>', methods=['POST'])
def create_seller_product(product_id):
    body = request.get_json()

    return transaction_service.create(body, product_id)
