import pytest
from datetime import datetime
from decimal import Decimal
from unittest.mock import AsyncMock, MagicMock
from models.transfer import TransferORM
from services.transfer_service import BudgetTransfer


@pytest.mark.asyncio
async def test_add_transfer(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    now = datetime.now()
    mock_repo.create.return_value = TransferORM(
        id=1, sender_id=1, receiver_id=2, amount=Decimal("50.0"), description="Fuel", created_on=now
    )
    
    service = BudgetTransfer(repo=mock_repo, session_maker=mock_session_maker)
    result = await service.add_transfer(1, 2, Decimal("50.0"), "Fuel", now)
    
    assert result.amount == Decimal("50.0")
    mock_repo.create.assert_called_once()


@pytest.mark.asyncio
async def test_get_by_account_transfer(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    now = datetime.now()
    mock_repo.get_all.return_value = [
        TransferORM(id=1, sender_id=1, receiver_id=2, amount=Decimal("50"), description="T1", created_on=now),
        TransferORM(id=2, sender_id=3, receiver_id=4, amount=Decimal("20"), description="T2", created_on=now)
    ]
    
    service = BudgetTransfer(repo=mock_repo, session_maker=mock_session_maker)
    # Testing for account 1 (sender)
    result = await service.get_by_account(1)
    assert len(result) == 1
    
    # Testing for account 2 (receiver)
    result_rec = await service.get_by_account(2)
    assert len(result_rec) == 1
