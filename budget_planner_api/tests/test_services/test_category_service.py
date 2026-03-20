import pytest
from unittest.mock import AsyncMock, MagicMock
from models.category import CategoryType, CategoryORM
from services.category_service import BudgetCategory


@pytest.mark.asyncio
async def test_add_category(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    mock_repo.create.return_value = CategoryORM(id=1, name="Rent", type=CategoryType.expense)
    
    service = BudgetCategory(repo=mock_repo, session_maker=mock_session_maker)
    result = await service.add_category("Rent", CategoryType.expense)
    
    assert result.name == "Rent"
    mock_repo.create.assert_called_once()


@pytest.mark.asyncio
async def test_get_all_categories(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    mock_repo.get_all.return_value = [
        CategoryORM(id=1, name="Rent", type=CategoryType.expense),
        CategoryORM(id=2, name="Salary", type=CategoryType.income)
    ]
    
    service = BudgetCategory(repo=mock_repo, session_maker=mock_session_maker)
    result = await service.get_all_categories()
    
    assert len(result) == 2
    assert result[0].name == "Rent"


@pytest.mark.asyncio
async def test_add_defaults(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    # Initially empty
    mock_repo.get_all.return_value = []
    
    service = BudgetCategory(repo=mock_repo, session_maker=mock_session_maker)
    await service.add_defaults()
    
    # Check that create was called for default categories
    assert mock_repo.create.call_count > 0
