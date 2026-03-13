from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Transfer:
    id: int
    sender_id: int
    receiver_id: int
    amount: Decimal
    description: str
    created_on: date
