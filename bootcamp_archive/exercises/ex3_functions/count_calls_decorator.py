

def count_calls(func: Callable):
    calls_number = 0
    def wrapper(*args,**kwargs):
        nonlocal calls_number 
        calls_number += 1
        print(f"Call {calls_number} of {func.__name__}")
        return func(*args,**kwargs)
    return wrapper

@count_calls
def a_call():
    return "hello"