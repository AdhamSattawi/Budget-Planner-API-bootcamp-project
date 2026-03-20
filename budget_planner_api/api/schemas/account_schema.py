from decimal import Decimal
from pydantic import BaseModel

class AccountCreate(BaseModel):
    name: str
    opening_balance: Decimal