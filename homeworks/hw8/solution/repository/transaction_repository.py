from solution.repository.base_repository import BaseRepository
from solution.models.transaction import Transaction, TransactionType
from decimal import Decimal
from datetime import date


class TransactionRepo(BaseRepository[Transaction]):
    
    def _to_entity(self, row: dict) -> Transaction:
        #{id:, type:, amount:, description:, category_id:, account_id:, created_on:}
        id = int(row["id"])
        type = TransactionType(row["type"])
        amount = Decimal(row["amount"])
        description = row["description"]
        category_id = int(row["category_id"])
        account_id = int(row["account_id"])
        created_on = date.fromisoformat(row["created_on"])
        return Transaction(
            id = id, 
            type = type, 
            amount = amount, 
            description = description, 
            category_id = category_id, 
            account_id = account_id, 
            created_on = created_on)
    
    def _to_dict(self, transaction: Transaction) -> dict:
        id = transaction.id
        type = transaction.type.value
        amount = transaction.amount 
        description = transaction.description
        category_id = transaction.category_id
        account_id = transaction.account_id
        created_on = transaction.created_on
        return {
            "id" : id, 
            "type" : type, 
            "amount" : amount,
            "description" : description, 
            "category_id" : category_id,
            "account_id" : account_id, 
            "created_on" : created_on}