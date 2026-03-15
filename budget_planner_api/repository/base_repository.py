from typing import Generic, TypeVar, Protocol
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

class HasId(Protocol):
    id: int

ModelType = TypeVar("ModelType", bound = HasId)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model_class: type[ModelType]):
        self.model_class = model_class

    async def create(self, session: AsyncSession, item: ModelType) -> ModelType:
        session.add(item)
        await session.flush()
        await session.refresh(item)
        return item

    async def get(self, session: AsyncSession, item_id: int) -> ModelType | None:
        return await session.get(self.model_class, item_id)
        
    async def get_all(self, session: AsyncSession) -> list[ModelType]:
        stmt = select(self.model_class)
        db_data = await session.scalars(stmt)
        return list(db_data.all())

    async def update(self, session: AsyncSession, item: ModelType) -> ModelType | None:
        to_update = await self.get(session, item.id)
        if not to_update:
            return None
        updated_item = await session.merge(item)
        await session.flush()
        return updated_item

    async def delete(self, session: AsyncSession, item_id: int) -> bool:
        item = await self.get(session, item_id)
        if not item:
            return False
        await session.delete(item)
        await session.flush()
        return True