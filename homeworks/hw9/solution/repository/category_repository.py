from solution.repository.base_repository import BaseRepository
from solution.models.category import CategoryORM


class CategoryRepo(BaseRepository[CategoryORM]):
    def __init__(self):
        super().__init__(CategoryORM)
