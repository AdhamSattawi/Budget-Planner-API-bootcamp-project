import pytest
from models.category import Category, CategoryType


@pytest.mark.asyncio
async def test_api_add_category(async_client, mock_category_service):
    mock_category_service.add_category.return_value = Category(id=1, name="Rent", type=CategoryType.expense)
    
    response = await async_client.post("/categories/", json={"name": "Rent", "type": "expense"})
    
    assert response.status_code == 200
    assert response.json()["name"] == "Rent"


@pytest.mark.asyncio
async def test_api_delete_category_not_found(async_client, mock_category_service):
    mock_category_service.delete_category.return_value = False
    
    response = await async_client.delete("/categories/999")
    
    assert response.status_code == 404
