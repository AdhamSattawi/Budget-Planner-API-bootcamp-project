from dataclasses import dataclass
from enum import Enum


class CategoryType(Enum):
    income = "income"
    expense = "expense"


@dataclass
class Category:
    id: int
    name: str
    type: CategoryType
