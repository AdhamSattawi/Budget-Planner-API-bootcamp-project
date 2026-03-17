from repository.account_repository import AccountRepo
from repository.category_repository import CategoryRepo
from repository.transaction_repository import TransactionRepo
from repository.transfer_repository import TransferRepo
from services.accounts_service import BudgetAccount
from services.category_service import BudgetCategory
from services.transaction_service import BudgetTransaction
from services.transfer_service import BudgetTransfer

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
