from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from solution.repository.csv_accessor import CsvFileAccessor

T = TypeVar("T")

class BaseRepository(ABC, Generic[T]):
    def __init__(self, accessor: CsvFileAccessor) -> None:
        self.accessor = accessor
    
    @abstractmethod
    def _to_entity(self, item: dict) -> T: ...

    @abstractmethod
    def _to_dict(self, item: T) -> dict: ...

    def _get_next_id(self) -> int: 
        data = self.get_all()
        if not data:
            return 1
        items_id = [item.id for item in data]
        max_id = max(items_id)
        return max_id + 1

    def create(self, item: T) -> T: 
        item_new_id = self._get_next_id()
        item.id = item_new_id
        data = self.get_all()
        data.append(item)
        data_of_dicts = [self._to_dict(obj) for obj in data]
        self.accessor.writing(data_of_dicts)
        return item

    def get(self, item_id: int) -> T | None: 
        data = self.get_all()
        for item in data:
            if item.id == item_id:
                return item
        return None

    def get_all(self) -> list[T]: 
        csv_data = self.accessor.reading()
        data = [self._to_entity(item) for item in csv_data]
        return data
        

    def update(self, item: T) -> T | None: 
        data = self.get_all()
        new_data = []
        for obj in data:
            if obj.id != item.id:
                new_data.append(obj)
            else: 
                new_data.append(item)
        
        if data == new_data:
            return None
        
        data_of_dicts = [self._to_dict(obj) for obj in new_data]
        self.accessor.writing(data_of_dicts)
        return item
        


    def delete(self, item_id: int) -> None: 
        data = self.get_all()
        new_data = [item for item in data if item.id != item_id]
        data_of_dicts = [self._to_dict(obj) for obj in new_data]
        self.accessor.writing(data_of_dicts)