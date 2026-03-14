from solution.repository.base_repository import BaseRepository
from solution.models.transaction import TransactionsORM


class TransactionRepo(BaseRepository[TransactionsORM]):
    def __init__(self):
        super().__init__(TransactionsORM)