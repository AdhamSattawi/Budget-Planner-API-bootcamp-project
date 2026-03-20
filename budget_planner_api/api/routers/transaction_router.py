from typing import Annotated
from fastapi import APIRouter, Depends
from models.transaction import Transaction
from services.transaction_service import BudgetTransaction
from api.dependencies import get_transaction_service
from api.schemas.transaction_schema import TransactionCreate

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/")
async def view_all_transactions(
    transaction_service: Annotated[BudgetTransaction, Depends(get_transaction_service)],
) -> dict:
    transactions_list = await transaction_service.get_all_transactions()
    transactions = {}
    for transaction in transactions_list:
        transactions[transaction.id] = [
            transaction.type,
            str(transaction.amount),
            transaction.description,
            transaction.category_id,
            transaction.account_id,
            transaction.created_on,
        ]
    return transactions


@router.post("/")
async def add_transaction(
    transaction: TransactionCreate,
    transaction_service: Annotated[BudgetTransaction, Depends(get_transaction_service)],
) -> Transaction:
    new_transaction = await transaction_service.add_transaction(
        transaction.type, transaction.amount, transaction.description, 
        transaction.category_id, transaction.account_id, transaction.created_on
    )
    return new_transaction


@router.delete("/{transaction_id}")
async def delete_transaction(
    transaction_id: int,
    transaction_service: Annotated[BudgetTransaction, Depends(get_transaction_service)],
) -> bool:
    return await transaction_service.delete_transaction(transaction_id)
