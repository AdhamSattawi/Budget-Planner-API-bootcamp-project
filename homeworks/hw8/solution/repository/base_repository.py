from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from csv_accessor import CsvFileAccessor

T = TypeVar("T")

class BaseRepository(ABC, Generic[T]):
    def __init__(self, accessor: CsvFileAccessor):
        self.accessor = accessor
    
    @abstractmethod
    def _to_entity(self, data: dict): ...

    @abstractmethod
    def _to_dict(self, item: T) -> dict: ...

    def _get_next_id(self) -> int: ...

    def create(self, item: T) -> T: ...

    def get(self, item_id: int) -> T: ...

    def get_all(self) -> list[T]: ...

    def update(self, item: T) -> T: ...

    def delete(self, item_id: int) -> None: ...
