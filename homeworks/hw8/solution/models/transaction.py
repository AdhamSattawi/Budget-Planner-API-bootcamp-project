from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from datetime import date

class TransactionType(Enum):
    income = "income"
    expense = "expense"

@dataclass
class Transaction:
    id: int
    type: TransactionType
    amount: Decimal
    description: str
    category_id: int
    account_id: int
    created_on: date
