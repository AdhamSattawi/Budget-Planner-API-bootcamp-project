from fastapi import APIRouter, Depends
from solution.services.category_service import BudgetCategory
from solution.models.category import Category, CategoryType
from solution.api.dependencies import get_category_service

router = APIRouter(prefix = "/categories", tags = ["Categories"])



@router.get("/")
async def view_all_categories(category_service: BudgetCategory = Depends(get_category_service)) -> dict:
    categories_list = category_service.get_all_categories()
    categories = {}
    for category in categories_list:
        categories[f"{category.id}_{category.name}"] = str(category.type)
    return categories

@router.post("/")
async def add_category(category: dict,
                       category_service: BudgetCategory = Depends(get_category_service)) -> Category:
    category_name = str(category["name"])
    category_type = CategoryType(category["type"])
    new_category = category_service.add_category(name = category_name, type = category_type)
    return new_category

@router.delete("/{category_id}")
async def delete_category(category_id: int,
                          category_service: BudgetCategory = Depends(get_category_service)) -> bool:
    return category_service.delete_category(category_id)