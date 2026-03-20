import pytest
from decimal import Decimal
from models.account import Account


@pytest.mark.asyncio
async def test_api_add_account(async_client, mock_account_service):
    mock_account_service.add_account.return_value = Account(id=1, name="Test", opening_balance=Decimal("100"))
    
    response = await async_client.post("/accounts/", json={"name": "Test", "opening_balance": "100.0"})
    
    assert response.status_code == 200
    assert response.json()["name"] == "Test"
    mock_account_service.add_account.assert_called_once()


@pytest.mark.asyncio
async def test_api_view_all_accounts(async_client, mock_account_service):
    mock_account_service.get_all_accounts.return_value = [
        (Account(id=1, name="Acc1", opening_balance=Decimal("100")), Decimal("150"))
    ]
    
    response = await async_client.get("/accounts/")
    
    assert response.status_code == 200
    assert response.json() == {"1_Acc1": "150"}


@pytest.mark.asyncio
async def test_api_delete_account_success(async_client, mock_account_service):
    mock_account_service.delete_account.return_value = True
    
    response = await async_client.delete("/accounts/1")
    
    assert response.status_code == 200
    assert response.json() is True


@pytest.mark.asyncio
async def test_api_delete_account_not_found(async_client, mock_account_service):
    mock_account_service.delete_account.return_value = False
    
    response = await async_client.delete("/accounts/999")
    
    assert response.status_code == 404
