from solution.repository.base_repository import BaseRepository
from solution.models.transaction import TransactionORM


class TransactionRepo(BaseRepository[TransactionORM]):
    def __init__(self):
        super().__init__(TransactionORM)