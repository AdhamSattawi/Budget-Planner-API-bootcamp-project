from repository.base_repository import BaseRepository
from models.transfer import TransferORM


class TransferRepo(BaseRepository[TransferORM]):
    def __init__(self) -> None:
        super().__init__(TransferORM)
