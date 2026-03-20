from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from models.transfer import Transfer
from services.transfer_service import BudgetTransfer
from api.dependencies import get_transfer_service
from api.schemas.transfer_schema import TransferCreate

router = APIRouter(prefix="/transfers", tags=["Transfers"])


@router.get("/")
async def view_all_transfers(
    transfer_service: Annotated[BudgetTransfer, Depends(get_transfer_service)],
) -> dict:
    transfers_list = await transfer_service.get_all_transfers()
    transfers = {}
    for transfer in transfers_list:
        transfers[transfer.id] = [
            transfer.sender_id,
            transfer.receiver_id,
            str(transfer.amount),
            transfer.description,
            transfer.created_on,
        ]
    return transfers


@router.post("/")
async def add_transfer(
    transfer: TransferCreate,
    transfer_service: Annotated[BudgetTransfer, Depends(get_transfer_service)],
) -> Transfer:
    new_transfer = await transfer_service.add_transfer(
        transfer.sender_id, transfer.receiver_id, transfer.amount, transfer.description, transfer.created_on
    )
    return new_transfer


@router.delete("/{transfer_id}")
async def delete_transfer(
    transfer_id: int,
    transfer_service: Annotated[BudgetTransfer, Depends(get_transfer_service)],
) -> bool:
    deleted_trn = await transfer_service.delete_transfer(transfer_id)
    if not deleted_trn:
        raise  HTTPException(status_code=404)
