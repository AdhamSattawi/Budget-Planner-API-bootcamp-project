from repository.base_repository import BaseRepository
from models.category import CategoryORM


class CategoryRepo(BaseRepository[CategoryORM]):
    def __init__(self) -> None:
        super().__init__(CategoryORM)
