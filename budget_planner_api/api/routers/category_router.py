from fastapi import APIRouter, Depends, HTTPException
from services.category_service import BudgetCategory
from models.category import Category
from api.dependencies import get_category_service
from typing import Annotated
from api.schemas.category_schema import CategoryCreate

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/")
async def view_all_categories(
    category_service: Annotated[BudgetCategory, Depends(get_category_service)],
) -> dict:
    categories_list = await category_service.get_all_categories()
    categories = {}
    for category in categories_list:
        categories[f"{category.id}_{category.name}"] = str(category.type)
    return categories


@router.post("/")
async def add_category(
    category: CategoryCreate,
    category_service: Annotated[BudgetCategory, Depends(get_category_service)],
) -> Category:
    new_category = await category_service.add_category(name=category.name, type=category.type)
    return new_category


@router.delete("/{category_id}")
async def delete_category(
    category_id: int,
    category_service: Annotated[BudgetCategory, Depends(get_category_service)],
) -> bool:
    deleted_cat = await category_service.delete_category(category_id)
    if not deleted_cat:
        raise HTTPException(status_code=404)
    return deleted_cat
