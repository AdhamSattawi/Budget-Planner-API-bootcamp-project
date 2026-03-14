from solution.repository.base_repository import BaseRepository
from solution.models.transfer import TransferORM


class TransferRepo(BaseRepository[TransferORM]):
    def __init__(self):
        super().__init__(TransferORM)
