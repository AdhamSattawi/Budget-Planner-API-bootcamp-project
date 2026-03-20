from models.category import CategoryType
from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name = str
    type = CategoryType