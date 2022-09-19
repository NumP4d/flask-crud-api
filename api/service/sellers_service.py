from api.model import Seller
from api.schema import SellerSchema
from .db_base_service import DbBaseService

seller_service = DbBaseService(
    model=Seller, schema=SellerSchema
)
