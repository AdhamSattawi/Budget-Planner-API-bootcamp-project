from datetime import datetime
from decimal import Decimal
from typing import Annotated
from fastapi import APIRouter, Depends
from models.transaction import Transaction, TransactionType
from services.transaction_service import BudgetTransaction
from api.dependencies import get_transaction_service

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/")
async def view_all_transactions(
    transaction_service: Annotated[BudgetTransaction, Depends(get_transaction_service)],
) -> dict:
    transactions_list = transaction_service.get_all_transactions()
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
    transaction: dict,
    transaction_service: Annotated[BudgetTransaction, Depends(get_transaction_service)],
) -> Transaction:
    type = TransactionType(transaction["type"])
    amount = Decimal(transaction["amount"])
    description = str(transaction["description"])
    category_id = int(transaction["category_id"])
    account_id = int(transaction["account_id"])
    created_on = datetime.fromisoformat(transaction["created_on"])
    new_transaction = transaction_service.add_transaction(
        type, amount, description, category_id, account_id, created_on
    )
    return new_transaction


@router.delete("/{transaction_id}")
async def delete_transaction(
    transaction_id: int,
    transaction_service: Annotated[BudgetTransaction, Depends(get_transaction_service)],
) -> bool:
    return transaction_service.delete_transaction(transaction_id)
