from flask import Blueprint

home_api = Blueprint('home', __name__)

@home_api.route('/')
def hello():
    return 'Hello World!'
