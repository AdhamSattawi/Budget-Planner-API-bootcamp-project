from decimal import Decimal
import pytest
from unittest.mock import AsyncMock, MagicMock
from models.account import AccountORM
from services.accounts_service import BudgetAccount
from datetime import datetime


@pytest.mark.asyncio
async def test_add_account(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    mock_repo.create.return_value = AccountORM(id=1, name="Test Acc", opening_balance=Decimal("100.0"))
    
    service = BudgetAccount(None, None, repo=mock_repo, session_maker=mock_session_maker)
    result = await service.add_account(name="Test Acc", opening_balance=Decimal("100.0"))

    assert result.name == "Test Acc"
    mock_repo.create.assert_called_once()
    mock_session.begin.assert_called_once()


@pytest.mark.asyncio
async def test_delete_account_success(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    mock_repo.delete.return_value = True
    
    service = BudgetAccount(None, None, repo=mock_repo, session_maker=mock_session_maker)
    result = await service.delete_account(account_id=1)

    assert result is True
    mock_repo.delete.assert_called_once_with(mock_session, 1)
    mock_session.begin.assert_called_once()


@pytest.mark.asyncio
async def test_delete_account_not_found(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    mock_repo.delete.return_value = False 
    
    service = BudgetAccount(None, None, repo=mock_repo, session_maker=mock_session_maker)
    result = await service.delete_account(account_id=999)
    assert result is False
    mock_repo.delete.assert_called_once_with(mock_session, 999)


@pytest.mark.asyncio
async def test_edit_account_success(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    mock_repo.get.return_value = AccountORM(id=1, name="Old Name", opening_balance=Decimal("100.0"))
    mock_repo.update.return_value = AccountORM(id=1, name="New Name", opening_balance=Decimal("100.0"))
    
    service = BudgetAccount(None, None, repo=mock_repo, session_maker=mock_session_maker)
    result = await service.edit_account(1, "New Name")
    
    assert result.name == "New Name"
    mock_repo.update.assert_called_once()


@pytest.mark.asyncio
async def test_get_balance(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    mock_repo.get.return_value = AccountORM(id=1, name="Test", opening_balance=Decimal("100.0"))
    
    mock_trans = AsyncMock()
    from models.transaction import Transaction, TransactionType
    mock_trans.get_by_account.return_value = [
        Transaction(1, TransactionType.income, Decimal("50.0"), "Salary", 1, 1, datetime.now()),
        Transaction(2, TransactionType.expense, Decimal("20.0"), "Food", 1, 1, datetime.now())
    ]
    
    mock_transfer = AsyncMock()
    from models.transfer import Transfer
    mock_transfer.get_by_account.return_value = [
        Transfer(1, 1, 2, Decimal("10.0"), "Rent", datetime.now())
    ]
    
    service = BudgetAccount(mock_trans, mock_transfer, repo=mock_repo, session_maker=mock_session_maker)
    balance = await service.get_balance(1)
    
    assert balance == Decimal("120.0")


@pytest.mark.asyncio
async def test_get_net_worth(mock_session, mock_session_maker):
    mock_repo = AsyncMock()
    acc1 = AccountORM(id=1, name="Acc 1", opening_balance=Decimal("100.0"))
    acc2 = AccountORM(id=2, name="Acc 2", opening_balance=Decimal("200.0"))
    
    mock_repo.get_all.return_value = [acc1, acc2]
    mock_repo.get.side_effect = [acc1, acc2]
    
    mock_trans = AsyncMock()
    mock_trans.get_by_account.return_value = []
    mock_transfer = AsyncMock()
    mock_transfer.get_by_account.return_value = []
    
    service = BudgetAccount(mock_trans, mock_transfer, repo=mock_repo, session_maker=mock_session_maker)
    net_worth = await service.get_net_worth()
    
    assert net_worth == Decimal("300.0")