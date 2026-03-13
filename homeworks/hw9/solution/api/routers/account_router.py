from decimal import Decimal
from fastapi import APIRouter, Depends
from solution.models.account import Account
from solution.api.dependencies import get_account_service
from solution.services.accounts_service import BudgetAccount
from typing import Annotated

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/")
async def add_new_acccount(
    new_account: dict, account_service: Annotated[BudgetAccount, Depends(get_account_service)]
) -> Account:
    name = str(new_account["name"])
    opening_balance = Decimal(str(new_account["opening_balance"]))
    return account_service.add_account(name=name, opening_balance=opening_balance)


@router.get("/")
async def view_all_accounts(
    account_service: Annotated[BudgetAccount, Depends(get_account_service)],
) -> dict:
    accounts = account_service.get_all_accounts()
    all_accounts = {}
    for account in accounts:
        acc, acc_balance = account
        all_accounts[f"{acc.id}_{acc.name}"] = str(acc_balance)
    return all_accounts


@router.get("/net_worth")
async def view_net_worth(
    account_service: Annotated[BudgetAccount, Depends(get_account_service)],
) -> dict:
    total = account_service.get_net_worth()
    net_worth = {"net_worth": str(total)}
    return net_worth


@router.get("/{account_id}")
async def view_balance(
    account_id: int, account_service: Annotated[BudgetAccount, Depends(get_account_service)]
) -> dict:
    account = account_service.get_balance(account_id)
    balance = {"account_balance": str(account)}
    return balance


@router.delete("/{account_id}")
async def delete_account(
    account_id: int, account_service: Annotated[BudgetAccount, Depends(get_account_service)]
) -> bool:
    return account_service.delete_account(account_id)


@router.put("/{account_id}")
async def update_account_name(
    account_id: int,
    new_updates: dict,
    account_service: Annotated[BudgetAccount, Depends(get_account_service)],
) -> Account | None:
    new_name = new_updates["new_name"]
    new_account = account_service.edit_account(account_id, new_name)
    if not new_account:
        return None
    return new_account
