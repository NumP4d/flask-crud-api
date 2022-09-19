from api.model import Transaction, Product
from api.schema import TransactionSchema
from .db_base_service import DbChildBaseService


transaction_service = DbChildBaseService(
    model=Transaction, schema=TransactionSchema,
    model_parent=Product, parent_id_name='product_id'
)
