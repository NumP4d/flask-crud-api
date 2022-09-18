from . import ma
from api.model import Seller

class SellerSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Seller
