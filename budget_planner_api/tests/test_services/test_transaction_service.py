import pytest
from datetime import datetime
from decimal import Decimal
from unittest.mock import AsyncMock, MagicMock
from models.transaction import TransactionType, TransactionORM
from services.transaction_service import BudgetTransaction


@pytest.mark.asyncio
async def test_add_transaction(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    mock_repo.create.return_value = TransactionORM(
        id=1, type=TransactionType.income, amount=Decimal("100.0"), 
        description="Test", category_id=1, account_id=1, created_on=datetime.now()
    )
    
    service = BudgetTransaction(repo=mock_repo, session_maker=mock_session_maker)
    result = await service.add_transaction(
        TransactionType.income, Decimal("100.0"), "Test", 1, 1, datetime.now()
    )
    
    assert result.amount == Decimal("100.0")
    mock_repo.create.assert_called_once()


@pytest.mark.asyncio
async def test_get_by_account(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    now = datetime.now()
    mock_repo.get_all.return_value = [
        TransactionORM(id=1, type=TransactionType.income, amount=Decimal("100"), description="A1", category_id=1, account_id=1, created_on=now),
        TransactionORM(id=2, type=TransactionType.expense, amount=Decimal("50"), description="A2", category_id=2, account_id=2, created_on=now)
    ]
    
    service = BudgetTransaction(repo=mock_repo, session_maker=mock_session_maker)
    result = await service.get_by_account(1)
    
    assert len(result) == 1
    assert result[0].account_id == 1
