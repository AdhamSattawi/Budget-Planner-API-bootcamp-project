from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests
from typing import Any

start = time.time()
def fetch_todo(todo_id: int) -> dict[str, Any]:
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")
    return response.json()

with ThreadPoolExecutor(max_workers = 8) as executor:
    futures = [executor.submit(fetch_todo, i) for i in range(1,21)]
    for future in as_completed(futures):
        print(future.result())

end = time.time() - start
print(f"execution took {end:.2f} secounds")


