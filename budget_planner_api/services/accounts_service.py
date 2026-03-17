from decimal import Decimal
from repository.account_repository import AccountRepo
from models.account import Account, AccountORM
from models.transaction import TransactionType
from services.transaction_service import BudgetTransaction
from services.transfer_service import BudgetTransfer
from typing import Optional
from database import async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio


def _orm_to_dataclass(account: AccountORM) -> Account:
    return Account(
        id=account.id, name=account.name, opening_balance=account.opening_balance
    )


def _dataclass_to_orm(account: Account) -> AccountORM:
    return AccountORM(
        id=account.id, name=account.name, opening_balance=account.opening_balance
    )


class BudgetAccount:
    def __init__(
        self,
        transaction_service: BudgetTransaction,
        transfer_service: BudgetTransfer,
        repo: Optional[AccountRepo] = None,
        session_maker: AsyncSession = None,
    ) -> None:
        self.repo = repo or AccountRepo()
        self.transaction_service = transaction_service
        self.transfer_service = transfer_service
        self._session_maker = session_maker or async_session_maker

    async def add_account(self, name: str, opening_balance: Decimal) -> Account:
        async with self._session_maker() as session:
            async with session.begin():
                new_account = AccountORM(name=name, opening_balance=opening_balance)
                created_account = await self.repo.create(session, new_account)
                return _orm_to_dataclass(created_account)

    async def delete_account(self, account_id: int) -> bool:
        async with self._session_maker() as session:
            async with session.begin():
                return await self.repo.delete(session, account_id)

    async def edit_account(self, account_id: int, new_name: str) -> Account | None:
        async with self._session_maker() as session:
            async with session.begin():
                account = await self._get_account(account_id)
                if not account:
                    return None
                account.name = new_name
                orm_account = _dataclass_to_orm(account)
                new_account = await self.repo.update(session, orm_account)
                return _orm_to_dataclass(new_account)

    async def get_balance(self, account_id: int) -> Decimal | None:
        account = await self._get_account(account_id)
        opening_balance = account.opening_balance if account else Decimal(0)
        transactions = await self._account_transactions(account_id)
        transfers = await self._account_transfers(account_id)
        balance = opening_balance + transactions + transfers
        return balance

    async def get_all_accounts(self) -> list[tuple[Account, Decimal | None]]:
        async with self._session_maker() as session:
            orm_accounts = await self.repo.get_all(session)
            if not orm_accounts:
                return []
            accounts = [_orm_to_dataclass(orm) for orm in orm_accounts]
            tasks = [self.get_balance(acc.id) for acc in accounts]
            balances = await asyncio.gather(*tasks)
            return list(zip(accounts, balances))

    async def get_net_worth(self) -> Decimal:
        async with self._session_maker() as session:
            accounts = await self.repo.get_all(session)
            total = Decimal(0)
            list_of_balances = [self.get_balance(account.id) for account in accounts]
            balances = await asyncio.gather(*list_of_balances)
            total = sum((b for b in balances if b is not None), Decimal(0))
            return total

    async def _get_account(self, account_id: int) -> Account | None:
        async with self._session_maker() as session:
            account = await self.repo.get(session, account_id)
            if not account:
                return None
            return _orm_to_dataclass(account)

    async def _account_transfers(self, account_id: int) -> Decimal:
        transfers = await self.transfer_service.get_by_account(account_id)
        account_transfers_in: Decimal = Decimal(0)
        account_transfers_out: Decimal = Decimal(0)
        for transfer in transfers:
            if transfer.receiver_id == account_id:
                account_transfers_in += transfer.amount
            else:
                account_transfers_out += transfer.amount
        return account_transfers_in - account_transfers_out

    async def _account_transactions(self, account_id: int) -> Decimal:
        transactions = await self.transaction_service.get_by_account(account_id)
        account_incomes: Decimal = Decimal(0)
        account_expenses: Decimal = Decimal(0)
        for transaction in transactions:
            if transaction.type == TransactionType.expense:
                account_expenses += transaction.amount
            else:
                account_incomes += transaction.amount
        return account_incomes - account_expenses
