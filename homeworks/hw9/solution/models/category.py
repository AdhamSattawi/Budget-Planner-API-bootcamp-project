from dataclasses import dataclass
from enum import Enum
from solution.database import Base
from sqlalchemy import Integer, String, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

class CategoryType(Enum):
    income = "income"
    expense = "expense"


@dataclass
class Category:
    id: int
    name: str
    type: CategoryType

NAME_MAX_CHR = 100

class CategoryORM(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    name: Mapped[str] = mapped_column(String(NAME_MAX_CHR), nullable = False)
    type: Mapped[CategoryType] = mapped_column(SQLEnum(CategoryType), nullable = False)