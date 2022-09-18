from flask import Blueprint, request
from api.service import (
    get_all_sellers_service,
    get_seller_service,
    create_seller_serivce
)


seller_api = Blueprint('seller', __name__)


@seller_api.route('/', methods=['GET'])
def get_all_sellers():
    return get_all_sellers_service()


@seller_api.route('/', methods=['POST'])
def create_seller():
    body = request.get_json()

    return create_seller_serivce(body)


@seller_api.route('/<int:seller_id>', methods=['GET'])
def get_seller(seller_id):
    return get_seller_service(seller_id)
