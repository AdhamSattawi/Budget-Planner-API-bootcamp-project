from fastapi import APIRouter
from services.category_service import BudgetCategory
from repository.category_repository import CategoryRepo
from models.category import Category, CategoryType
from repository.csv_accessor import CsvFileAccessor

router = APIRouter(prefix = "/categories", tags = ["Categories"])

ACCOUNTS_CSV_PATH = "data/categories.csv"
ACCOUNTS_HEADERS = ["id", "name", "type"]

accessor = CsvFileAccessor(ACCOUNTS_CSV_PATH, ACCOUNTS_HEADERS)
repo = CategoryRepo(accessor)
category_service = BudgetCategory(repo)

@router.get("/")
async def view_all_categories() -> dict:
    categories_list = category_service.get_all_categories()
    categories = {}
    for category in categories_list:
        categories[f"{category.id}_{category.name}"] = str(category.type)
    return categories

@router.post("/")
async def add_category(category: dict) -> Category:
    category_name = str(category["name"])
    category_type = CategoryType(category["type"])
    new_category = category_service.add_category(name = category_name, type = category_type)
    return new_category

@router.delete("/{category_id}")
async def delete_category(category_id: int) -> bool:
    return category_service.delete_category(category_id)