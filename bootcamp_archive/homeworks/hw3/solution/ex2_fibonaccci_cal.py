from functools import lru_cache

@lru_cache
def fibonacci(num: int) -> int:
    """This function calculates the nth Fibonacci number."""
    if num < 1:
        raise ValueError("it must be 1 or greater")
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)
