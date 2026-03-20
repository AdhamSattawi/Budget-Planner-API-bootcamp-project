from fastapi import APIRouter, Depends, HTTPException
from models.account import Account
from api.dependencies import get_account_service
from services.accounts_service import BudgetAccount
from typing import Annotated
from api.schemas.account_schema import AccountCreate

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/")
async def add_new_acccount(
    new_account: AccountCreate,
    account_service: Annotated[BudgetAccount, Depends(get_account_service)],
) -> Account:
    return await account_service.add_account(name=new_account.name, opening_balance=new_account.opening_balance)


@router.get("/")
async def view_all_accounts(
    account_service: Annotated[BudgetAccount, Depends(get_account_service)],
) -> dict:
    accounts = await account_service.get_all_accounts()
    all_accounts = {}
    for account in accounts:
        acc, acc_balance = account
        all_accounts[f"{acc.id}_{acc.name}"] = str(acc_balance)
    return all_accounts


@router.get("/net_worth")
async def view_net_worth(
    account_service: Annotated[BudgetAccount, Depends(get_account_service)],
) -> dict:
    total = await account_service.get_net_worth()
    net_worth = {"net_worth": str(total)}
    return net_worth


@router.get("/{account_id}")
async def view_balance(
    account_id: int,
    account_service: Annotated[BudgetAccount, Depends(get_account_service)],
) -> dict:
    account = await account_service.get_balance(account_id)
    balance = {"account_balance": str(account)}
    return balance


@router.delete("/{account_id}")
async def delete_account(
    account_id: int,
    account_service: Annotated[BudgetAccount, Depends(get_account_service)],
) -> bool:
    return await account_service.delete_account(account_id)


@router.put("/{account_id}")
async def update_account_name(
    account_id: int,
    new_updates: dict,
    account_service: Annotated[BudgetAccount, Depends(get_account_service)],
) -> Account | None:
    new_name = new_updates["new_name"]
    new_account = await account_service.edit_account(account_id, new_name)
    if not new_account:
        raise HTTPException(status_code=404)
    return new_account
