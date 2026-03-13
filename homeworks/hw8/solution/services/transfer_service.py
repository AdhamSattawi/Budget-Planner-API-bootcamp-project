from datetime import date
from decimal import Decimal
from solution.models.transfer import Transfer
from solution.repository.transfer_repository import TransferRepo


class BudgetTransfer:
    def __init__(self, repo: TransferRepo):
        self.repo = repo

    def get_all_transfers(self) -> list[Transfer]:
        return self.repo.get_all()

    def add_transfer(
        self,
        sender_id: int,
        receiver_id: int,
        amount: Decimal,
        description: str,
        created_on: date,
    ) -> Transfer:
        new_transfer = Transfer(
            id=0,
            sender_id=sender_id,
            receiver_id=receiver_id,
            amount=amount,
            description=description,
            created_on=created_on,
        )
        return self.repo.create(new_transfer)

    def delete_transfer(self, transfer_id: int) -> bool:
        transfer = self.repo.get(transfer_id)
        if not transfer:
            return False
        self.repo.delete(transfer_id)
        return True

    def get_by_account(self, account_id: int) -> list[Transfer]:
        transfers = self.get_all_transfers()
        account_transfers = [
            transfer
            for transfer in transfers
            if transfer.sender_id == account_id or transfer.receiver_id == account_id
        ]
        return account_transfers
