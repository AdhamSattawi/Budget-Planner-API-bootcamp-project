from datetime import date
from decimal import Decimal
from fastapi import APIRouter, Depends
from models.transfer import Transfer
from services.transfer_service import BudgetTransfer
from api.dependencies import get_transfer_service

router = APIRouter(prefix = "/transfers", tags = ["Transfers"])


@router.get("/")
async def view_all_transfers(transfer_service: BudgetTransfer = Depends(get_transfer_service)) -> dict:
    transfers_list = transfer_service.get_all_transfers()
    transfers = {}
    for transfer in transfers_list:
        transfers[transfer.id] = [transfer.sender_id, transfer.receiver_id, str(transfer.amount),
                                  transfer.description, transfer.created_on]
    return transfers

@router.post("/")
async def add_transfer(transfer: dict,
                       transfer_service: BudgetTransfer = Depends(get_transfer_service)) -> Transfer:
    sender_id = int(transfer["sender_id"])
    receiver_id = int(transfer["receiver_id"])
    amount = Decimal(transfer["amount"])
    description = str(transfer["description"])
    created_on = date.fromisoformat(transfer["created_on"])
    new_transfer = transfer_service.add_transfer(sender_id, receiver_id, amount, 
                                                 description, created_on)
    return new_transfer

@router.delete("/{transfer_id}")
async def delete_transfer(transfer_id: int,
                          transfer_service: BudgetTransfer = Depends(get_transfer_service)) -> bool:
    return transfer_service.delete_transfer(transfer_id)