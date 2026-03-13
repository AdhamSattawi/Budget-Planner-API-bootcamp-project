from datetime import date
from decimal import Decimal
from solution.models.transaction import Transaction, TransactionType
from solution.repository.transaction_repository import TransactionRepo

class BudgetTransaction:
    def __init__(self, repo: TransactionRepo):
        self.repo = repo

    def get_all_transactions(self) -> list[Transaction]:
        return self.repo.get_all()
    
    def add_transaction(self, type: TransactionType, amount: Decimal, description: str, 
        category_id: int, account_id: int, created_on: date) -> Transaction:
        new_transaction = Transaction(id = 0, type = type, amount = amount, 
                                    description = description, category_id = category_id,
                                    account_id = account_id, created_on = created_on)
        return self.repo.create(new_transaction)

    def delete_transaction(self, transaction_id: int) -> bool:
        transaction = self.repo.get(transaction_id)
        if not transaction:
            return False
        self.repo.delete(transaction_id)
        return True
    
    def get_by_account(self, account_id: int) -> list[Transaction]: 
        transactions = self.get_all_transactions()
        account_transactions = [transaction for transaction in transactions 
                                if transaction.account_id == account_id]
        return account_transactions