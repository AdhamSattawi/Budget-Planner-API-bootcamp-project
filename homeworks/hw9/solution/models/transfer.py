from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from solution.database import Base
from sqlalchemy import Integer, String, DECIMAL, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

@dataclass
class Transfer:
    id: int
    sender_id: int
    receiver_id: int
    amount: Decimal
    description: str
    created_on: datetime

DESC_MAX_CHR = 300

class TransfersORM(Base):
    __tablename__ = "transfers"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    sender_id: Mapped[int] = mapped_column(Integer, nullable = False)
    receiver_id: Mapped[int] = mapped_column(Integer, nullable = False)
    amount: Mapped[Decimal] = mapped_column(DECIMAL, nullable = False)
    description: Mapped[str] = mapped_column(String(DESC_MAX_CHR))
    created_on: Mapped[datetime] = mapped_column(DateTime, nullable = False, server_default = func.now())