from datetime import datetime
from decimal import Decimal
from models.transaction import TransactionType
from pydantic import BaseModel

class TransactionCreate(BaseModel):
    type: TransactionType
    amount: Decimal
    description: str
    category_id: int
    account_id: int
    created_on: datetime