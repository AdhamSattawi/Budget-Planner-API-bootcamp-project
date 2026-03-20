import pytest
from datetime import datetime
from decimal import Decimal
from models.transfer import Transfer


@pytest.mark.asyncio
async def test_api_add_transfer(async_client, mock_transfer_service):
    mock_transfer_service.add_transfer.return_value = Transfer(
        id=1, sender_id=1, receiver_id=2, amount=Decimal("50"), 
        description="Split", created_on=datetime.now()
    )
    
    payload = {
        "sender_id": 1,
        "receiver_id": 2,
        "amount": "50.0",
        "description": "Split",
        "created_on": datetime.now().isoformat()
    }
    
    response = await async_client.post("/transfers/", json=payload)
    
    assert response.status_code == 200
    assert response.json()["amount"] == "50"


@pytest.mark.asyncio
async def test_api_delete_transfer_not_found(async_client, mock_transfer_service):
    mock_transfer_service.delete_transfer.return_value = False
    
    response = await async_client.delete("/transfers/999")
    
    assert response.status_code == 404
