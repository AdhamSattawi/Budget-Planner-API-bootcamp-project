from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from datetime import datetime
from solution.database import Base
from sqlalchemy import Integer, String, Enum as SQLEnum, DECIMAL, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

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
    created_on: datetime

DESC_MAX_CHR = 300

class TransactionsORM(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    type: Mapped[TransactionType] = mapped_column(SQLEnum(TransactionType), nullable = False)
    amount: Mapped[Decimal] = mapped_column(DECIMAL, nullable = False)
    description: Mapped[str] = mapped_column(String(DESC_MAX_CHR))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable = False)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable = False)
    created_on: Mapped[datetime] = mapped_column(DateTime, nullable = False, server_default = func.now())