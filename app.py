import os
from flask import Flask
from api.model import db
from api.schema import ma
from api.route import home_api, product_api, seller_api, transaction_api


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(app)
ma.init_app(app)
app.register_blueprint(home_api)
app.register_blueprint(seller_api, url_prefix='/seller')
app.register_blueprint(product_api, url_prefix='/product')
app.register_blueprint(transaction_api, url_prefix='/transaction')

with app.app_context():
    db.create_all()
