from repository.base_repository import BaseRepository
from models.transaction import TransactionORM


class TransactionRepo(BaseRepository[TransactionORM]):
    def __init__(self) -> None:
        super().__init__(TransactionORM)
