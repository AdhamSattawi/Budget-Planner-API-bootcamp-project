from solution.repository.base_repository import BaseRepository
from solution.models.category import Category, CategoryType


class CategoryRepo(BaseRepository[Category]):

    def _to_entity(self, row: dict) -> Category:
        # {id:, name:, type:}
        id = int(row["id"])
        name = row["name"]
        type = CategoryType(row["type"])
        return Category(id=id, name=name, type=type)

    def _to_dict(self, category: Category) -> dict:
        id = category.id
        name = category.name
        type = category.type.value
        return {"id": id, "name": name, "type": type}
