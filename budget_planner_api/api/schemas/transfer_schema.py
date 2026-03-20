from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class TransferCreate(BaseModel):
    sender_id: int
    receiver_id: int
    amount: Decimal
    description: str
    created_on: datetime