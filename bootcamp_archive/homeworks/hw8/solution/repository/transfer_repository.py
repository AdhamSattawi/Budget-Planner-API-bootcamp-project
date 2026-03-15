from solution.repository.base_repository import BaseRepository
from solution.models.transfer import Transfer
from decimal import Decimal
from datetime import date


class TransferRepo(BaseRepository[Transfer]):

    def _to_entity(self, row: dict) -> Transfer:
        # {id:, sender_id:, receiver_id:, amount:, description:, created_on:}
        id = int(row["id"])
        sender_id = int(row["sender_id"])
        receiver_id = int(row["receiver_id"])
        amount = Decimal(row["amount"])
        description = row["description"]
        created_on = date.fromisoformat(row["created_on"])
        return Transfer(
            id=id,
            sender_id=sender_id,
            receiver_id=receiver_id,
            amount=amount,
            description=description,
            created_on=created_on,
        )

    def _to_dict(self, transfer: Transfer) -> dict:
        id = transfer.id
        sender_id = transfer.sender_id
        receiver_id = transfer.receiver_id
        amount = transfer.amount
        description = transfer.description
        created_on = transfer.created_on
        return {
            "id": id,
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "amount": amount,
            "description": description,
            "created_on": created_on,
        }
