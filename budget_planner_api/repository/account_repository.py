from repository.base_repository import BaseRepository
from models.account import AccountORM


class AccountRepo(BaseRepository[AccountORM]):
    def __init__(self) -> None:
        super().__init__(AccountORM)
