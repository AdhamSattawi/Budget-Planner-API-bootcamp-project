from solution.models.category import Category, CategoryType
from solution.repository.category_repository import CategoryRepo, CategoryORM
from typing import Optional
from solution.database import async_session_maker


def _orm_to_dataclass(category: CategoryORM) -> Category:
    return Category(id=category.id, name=category.name, type=category.type)


class BudgetCategory:
    def __init__(self, repo: Optional[CategoryRepo] = None, session_maker=None) -> None:
        self.repo = repo or CategoryRepo()
        self._session_maker = session_maker or async_session_maker

    async def get_all_categories(self) -> list[Category]:
        async with self._session_maker() as session:
            orm_categories = await self.repo.get_all(session)
            categories = []
            for orm_category in orm_categories:
                transfer = _orm_to_dataclass(orm_category)
                categories.append(transfer)
            return categories

    async def add_category(self, name: str, type: CategoryType) -> Category:
        async with self._session_maker() as session:
            async with session.begin():
                new_category = CategoryORM(name=name, type=type)
                created_cat = await self.repo.create(session, new_category)
                return _orm_to_dataclass(created_cat)

    async def delete_category(self, category_id: int) -> bool:
        async with self._session_maker() as session:
            async with session.begin():
                return await self.repo.delete(session, category_id)

    async def add_defaults(self) -> None:
        async with self._session_maker() as session:
            if len(await self.repo.get_all(session)) == 0:
                await self.add_category(name="Rent", type=CategoryType.expense)
                await self.add_category(name="Freelancing", type=CategoryType.income)
                await self.add_category(name="Groceries", type=CategoryType.expense)
                await self.add_category(name="Work", type=CategoryType.income)
                await self.add_category(name="SideHustle", type=CategoryType.income)
                await self.add_category(name="Electronics", type=CategoryType.expense)
                await self.add_category(name="HomeStuff", type=CategoryType.expense)
                await self.add_category(
                    name="CarMaintanance", type=CategoryType.expense
                )
                await self.add_category(name="SelfCare", type=CategoryType.expense)
                await self.add_category(name="Resturants", type=CategoryType.expense)
