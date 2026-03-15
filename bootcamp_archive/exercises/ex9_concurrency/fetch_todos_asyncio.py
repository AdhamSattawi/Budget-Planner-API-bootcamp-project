import asyncio
import aiohttp
import time
from typing import Any


async def fetch_todo(session: aiohttp.ClientSession, todo_id: int) -> dict[str, Any]:
    async with session.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}") as response:
        return await response.json()

async def proccess_all():
    async with aiohttp.ClientSession() as session:
        responses = [fetch_todo(session, i) for i in range(1,21)]
        tasks = await asyncio.gather(*responses)
        return tasks

if __name__ == "__main__":
    start = time.time()
    data = asyncio.run(proccess_all())
    for task in data:
        print(task)
    end = time.time() - start
    print(f"execution took {end:.2f} secounds")




