from typing import Any
import time

class MyLruCache:
    def __init__(self, max_size: int, ttl: float) -> None:
        if max_size <= 0  or ttl <= 0:
            raise ValueError("The value must be more than zero.")
        self.max_size = max_size # Max memory size
        self.ttl = ttl # Time to live for cached items (seconds)
        self.cache: dict[str, list] = {} #dict {key: [value, time]}
        

    def get(self, key: str) -> Any | None:
        if key not in self.cache:
            return None
        current_time = time.time()
        passed_time = current_time - self.cache[key][1]
        if passed_time >= self.ttl:
            self.cache.pop(key)
            return None
        else:
            old = self.cache.pop(key)
            self.cache[key] =  [old[0], current_time]      
            return self.cache[key][0]


    def set(self, key: str, value: Any) -> None:
        current_time = time.time()
        cach_length = len(self.cache)
        if (key in self.cache):
            self.cache.pop(key)
            self.cache[key] = [value, current_time]
        elif cach_length >= self.max_size:
            first_key = self.first_out(self.cache)
            self.cache.pop(first_key)
            self.cache[key] = [value, current_time]
        else:
            self.cache[key] = [value, current_time]

        
    def first_out(self, cache: dict) -> str:
        """Returns the first key in the dict."""
        least_recent = ""
        for key in cache:
            least_recent = key
            break
        return least_recent

    def clear(self) -> None:
        self.cache.clear()

    def __len__(self) -> int:
        return len(self.cache)

    def __contains__(self, key: str) -> bool:
        if key not in self.cache:
            return False
        current_time = time.time()
        passed_time = current_time - self.cache[key][1]
        return passed_time <= self.ttl