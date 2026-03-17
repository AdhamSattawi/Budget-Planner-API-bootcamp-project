from datetime import datetime
from decimal import Decimal
from models.transaction import Transaction, TransactionType, TransactionORM
from repository.transaction_repository import TransactionRepo
from typing import Optional
from database import async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession


def _orm_to_dataclass(transaction: TransactionORM) -> Transaction:
    return Transaction(
        id=transaction.id,
        type=transaction.type,
        amount=transaction.amount,
        description=transaction.description,
        category_id=transaction.category_id,
        account_id=transaction.account_id,
        created_on=transaction.created_on,
    )


class BudgetTransaction:
    def __init__(
        self, repo: Optional[TransactionRepo] = None, session_maker: AsyncSession = None
    ) -> None:
        self.repo = repo or TransactionRepo()
        self._session_maker = session_maker or async_session_maker

    async def get_all_transactions(self) -> list[Transaction]:
        async with self._session_maker() as session:
            orm_transactions = await self.repo.get_all(session)
            transactions = []
            for orm_transaction in orm_transactions:
                transaction = _orm_to_dataclass(orm_transaction)
                transactions.append(transaction)
            return transactions

    async def add_transaction(
        self,
        type: TransactionType,
        amount: Decimal,
        description: str,
        category_id: int,
        account_id: int,
        created_on: datetime,
    ) -> Transaction:
        async with self._session_maker() as session:
            async with session.begin():
                new_transaction = TransactionORM(
                    type=type,
                    amount=amount,
                    description=description,
                    category_id=category_id,
                    account_id=account_id,
                    created_on=created_on,
                )
                created_transaction = await self.repo.create(session, new_transaction)
                return _orm_to_dataclass(created_transaction)

    async def delete_transaction(self, transaction_id: int) -> bool:
        async with self._session_maker() as session:
            async with session.begin():
                return await self.repo.delete(session, transaction_id)

    async def get_by_account(self, account_id: int) -> list[Transaction]:
        transactions = await self.get_all_transactions()
        account_transactions = [
            transaction
            for transaction in transactions
            if transaction.account_id == account_id
        ]
        return account_transactions
