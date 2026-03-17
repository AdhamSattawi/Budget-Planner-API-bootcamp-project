from datetime import datetime
from decimal import Decimal
from models.transfer import Transfer, TransferORM
from repository.transfer_repository import TransferRepo
from typing import Optional
from database import async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession


def _orm_to_dataclass(transfer: TransferORM) -> Transfer:
    return Transfer(
        id=transfer.id,
        sender_id=transfer.sender_id,
        receiver_id=transfer.receiver_id,
        amount=transfer.amount,
        description=transfer.description,
        created_on=transfer.created_on,
    )


class BudgetTransfer:
    def __init__(
        self, repo: Optional[TransferRepo] = None, session_maker: AsyncSession = None
    ) -> None:
        self.repo = repo or TransferRepo()
        self._session_maker = session_maker or async_session_maker

    async def get_all_transfers(self) -> list[Transfer]:
        async with self._session_maker() as session:
            orm_transfers = await self.repo.get_all(session)
            transfers = []
            for orm_transfer in orm_transfers:
                transfer = _orm_to_dataclass(orm_transfer)
                transfers.append(transfer)
            return transfers

    async def add_transfer(
        self,
        sender_id: int,
        receiver_id: int,
        amount: Decimal,
        description: str,
        created_on: datetime,
    ) -> Transfer:
        async with self._session_maker() as session:
            async with session.begin():
                new_transfer = TransferORM(
                    sender_id=sender_id,
                    receiver_id=receiver_id,
                    amount=amount,
                    description=description,
                    created_on=created_on,
                )
                created_transfer = await self.repo.create(session, new_transfer)
                return _orm_to_dataclass(created_transfer)

    async def delete_transfer(self, transfer_id: int) -> bool:
        async with self._session_maker() as session:
            async with session.begin():
                return await self.repo.delete(session, transfer_id)

    async def get_by_account(self, account_id: int) -> list[Transfer]:
        transfers = await self.get_all_transfers()
        account_transfers = [
            transfer
            for transfer in transfers
            if transfer.sender_id == account_id or transfer.receiver_id == account_id
        ]
        return account_transfers
