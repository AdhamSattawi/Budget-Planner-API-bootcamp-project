from datetime import date
from decimal import Decimal
from fastapi import APIRouter
from services.transfer_service import BudgetTransfer
from repository.transfer_repository import TransferRepo
from models.transfer import Transfer
from repository.csv_accessor import CsvFileAccessor

router = APIRouter(prefix = "/transfers", tags = ["Transfers"])

ACCOUNTS_CSV_PATH = "data/transfers.csv"
ACCOUNTS_HEADERS = ["id", "sender_id", "receiver_id", "amount", "description", "created_on"]

accessor = CsvFileAccessor(ACCOUNTS_CSV_PATH, ACCOUNTS_HEADERS)
repo = TransferRepo(accessor)
transfer_service = BudgetTransfer(repo)

@router.get("/")
async def view_all_transfers() -> dict:
    transfers_list = transfer_service.get_all_transfers()
    transfers = {}
    for transfer in transfers_list:
        transfers[transfer.id] = [transfer.sender_id, transfer.receiver_id, str(transfer.amount),
                                  transfer.description, transfer.created_on]
    return transfers

@router.post("/")
async def add_transfer(transfer: dict) -> Transfer:
    sender_id = int(transfer["sender_id"])
    receiver_id = int(transfer["receiver_id"])
    amount = Decimal(transfer["amount"])
    description = str(transfer["description"])
    created_on = date(transfer["created_on"])
    new_transfer = transfer_service.add_transfer(sender_id, receiver_id, amount, 
                                                 description, created_on)
    return new_transfer

@router.delete("/{transfer_id}")
async def delete_category(transfer_id: int) -> bool:
    return transfer_service.delete_transfer(transfer_id)