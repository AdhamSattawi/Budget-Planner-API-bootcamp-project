from decimal import Decimal
from fastapi import APIRouter
from services.accounts_service import BudgetAccount
from repository.account_repository import AccountRepo
from models.account import Account
from repository.csv_accessor import CsvFileAccessor

router = APIRouter(prefix = "/accounts", tags = ["Accounts"])

ACCOUNTS_CSV_PATH = "data/accounts.csv"
ACCOUNTS_HEADERS = ["id", "name", "opening_balance"]

accessor = CsvFileAccessor(ACCOUNTS_CSV_PATH, ACCOUNTS_HEADERS)
repo = AccountRepo(accessor)
account_service = BudgetAccount(repo)

@router.post("/")
async def add_new_acccount(new_account: dict) -> Account:
    name = str(new_account["name"])
    opening_balance = Decimal(str(new_account["opening_balance"]))
    return account_service.add_account(name = name, opening_balance = opening_balance)

@router.get("/")
async def view_all_accounts() -> dict:
    accounts = account_service.get_all_accounts()
    all_accounts = {}
    for account in accounts:
        acc, acc_balance = account
        all_accounts[f"{acc.id}_{acc.name}"] = str(acc_balance)
    return all_accounts

@router.get("/{account_id}")
async def view_balance(account_id: int) -> dict:
    account = account_service.get_balance(account_id)
    balance = {"account_balance" : str(account)}
    return balance

@router.delete("/{account_id}")
async def delete_account(account_id: int) -> bool:
    return account_service.delete_account(account_id)

@router.get("/net_worth")
async def view_net_worth() -> dict:
    total = account_service.get_net_worth()
    net_worth = {"net_worth" : str(total)}
    return net_worth

@router.put("/{account_id}")
async def update_account_name(account_id: int, new_updates: dict) -> Account:
    new_name = new_updates["new_name"]
    return account_service.edit_account(account_id, new_name)