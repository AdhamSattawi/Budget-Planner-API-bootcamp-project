
from solution.repository.account_repository import AccountRepo
from solution.repository.category_repository import CategoryRepo
from solution.repository.transaction_repository import TransactionRepo
from solution.repository.transfer_repository import TransferRepo

from solution.services.accounts_service import BudgetAccount
from solution.services.category_service import BudgetCategory
from solution.services.transaction_service import BudgetTransaction
from solution.services.transfer_service import BudgetTransfer

transfer_service = BudgetTransfer()
transaction_service = BudgetTransaction()
account_service = BudgetAccount(
    transaction_service=transaction_service, transfer_service=transfer_service
)
category_service = BudgetCategory()


def get_account_service() -> BudgetAccount:
    return account_service


def get_category_service() -> BudgetCategory:
    return category_service


def get_transaction_service() -> BudgetTransaction:
    return transaction_service


def get_transfer_service() -> BudgetTransfer:
    return transfer_service
