from solution.repository.csv_accessor import CsvFileAccessor

from solution.repository.account_repository import AccountRepo
from solution.repository.category_repository import CategoryRepo
from solution.repository.transaction_repository import TransactionRepo
from solution.repository.transfer_repository import TransferRepo

from solution.services.accounts_service import BudgetAccount
from solution.services.category_service import BudgetCategory
from solution.services.transaction_service import BudgetTransaction
from solution.services.transfer_service import BudgetTransfer


ACCOUNTS_CSV_PATH = "data/accounts.csv"
ACCOUNTS_HEADERS = ["id", "name", "opening_balance"]

CATEGORIES_CSV_PATH = "data/categories.csv"
CATEGORIES_HEADERS = ["id", "name", "type"]

TRANSACTIONS_CSV_PATH = "data/transactions.csv"
TRANSACTIONS_HEADERS = ["id", "type", "amount", "description", "category_id", "account_id", "created_on"]

TRANSFERS_CSV_PATH = "data/transfers.csv"
TRANSFERS_HEADERS = ["id", "sender_id", "receiver_id", "amount", "description", "created_on"]

trf_accessor = CsvFileAccessor(TRANSFERS_CSV_PATH, TRANSFERS_HEADERS)
trf_repo = TransferRepo(trf_accessor)
transfer_service = BudgetTransfer(trf_repo)

trn_accessor = CsvFileAccessor(TRANSACTIONS_CSV_PATH, TRANSACTIONS_HEADERS)
trn_repo = TransactionRepo(trn_accessor)
transaction_service = BudgetTransaction(trn_repo)

acc_accessor = CsvFileAccessor(ACCOUNTS_CSV_PATH, ACCOUNTS_HEADERS)
acc_repo = AccountRepo(acc_accessor)
account_service = BudgetAccount(acc_repo, transaction_service = transaction_service, 
                                transfer_service = transfer_service)

cat_accessor = CsvFileAccessor(CATEGORIES_CSV_PATH, CATEGORIES_HEADERS)
cat_repo = CategoryRepo(cat_accessor)
category_service = BudgetCategory(cat_repo)


def get_account_service() -> BudgetAccount:
    return account_service

def get_category_service() -> BudgetCategory:
    return category_service

def get_transaction_service() -> BudgetTransaction:
    return transaction_service

def get_transfer_service() -> BudgetTransfer:
    return transfer_service





