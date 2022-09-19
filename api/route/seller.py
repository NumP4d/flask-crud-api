from flask import Blueprint, request
from api.service import seller_service


seller_api = Blueprint('seller', __name__)


@seller_api.route('/', methods=['GET'])
def get_all_sellers():
    return seller_service.get_all()


@seller_api.route('/', methods=['POST'])
def create_seller():
    body = request.get_json()

    return seller_service.create(body)


@seller_api.route('/<int:seller_id>', methods=['GET'])
def get_seller(seller_id):
    return seller_service.get(seller_id)
