from solution.repository.base_repository import BaseRepository
from solution.models.account import AccountORM


class AccountRepo(BaseRepository[AccountORM]):
    def __init__(self):
        super().__init__(AccountORM)
