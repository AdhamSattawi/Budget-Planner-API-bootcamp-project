import pytest
from datetime import datetime
from decimal import Decimal
from models.transaction import Transaction, TransactionType


@pytest.mark.asyncio
async def test_api_add_transaction(async_client, mock_transaction_service):
    mock_transaction_service.add_transaction.return_value = Transaction(
        id=1, type=TransactionType.income, amount=Decimal("100"), 
        description="Salary", category_id=1, account_id=1, created_on=datetime.now()
    )
    
    payload = {
        "type": "income",
        "amount": "100.0",
        "description": "Salary",
        "category_id": 1,
        "account_id": 1,
        "created_on": datetime.now().isoformat()
    }
    
    response = await async_client.post("/transactions/", json=payload)
    
    assert response.status_code == 200
    assert response.json()["amount"] == "100"


@pytest.mark.asyncio
async def test_api_delete_transaction_not_found(async_client, mock_transaction_service):
    mock_transaction_service.delete_transaction.return_value = False
    
    response = await async_client.delete("/transactions/999")
    
    assert response.status_code == 404
