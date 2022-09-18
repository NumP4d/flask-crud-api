import os
from flask import Flask
from api.model import db, Seller, Product
from api.schema import ma
from api.route.home import home_api
from api.route.seller import seller_api
from api.route.product import product_api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(app)
ma.init_app(app)
app.register_blueprint(home_api, url_prefix='/api')
app.register_blueprint(seller_api, url_prefix='/seller')
app.register_blueprint(product_api, url_prefix='/product')

with app.app_context():
    db.create_all()