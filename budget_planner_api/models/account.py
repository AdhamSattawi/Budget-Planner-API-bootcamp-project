from dataclasses import dataclass
from decimal import Decimal
from solution.database import Base
from sqlalchemy import Integer, String, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column

@dataclass
class Account:
    id: int
    name: str
    opening_balance: Decimal

NAME_MAX_CHR = 100

class AccountORM(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    name: Mapped[str] = mapped_column(String(NAME_MAX_CHR), nullable = False)
    opening_balance: Mapped[Decimal] = mapped_column(DECIMAL, nullable = False, default = 0.0)
