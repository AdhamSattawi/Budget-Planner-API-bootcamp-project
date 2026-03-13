import uvicorn
from fastapi import FastAPI
from solution.api.routers import (
    account_router,
    category_router,
    transaction_router,
    transfer_router,
)

app = FastAPI()

app.include_router(account_router.router)
app.include_router(category_router.router)
app.include_router(transaction_router.router)
app.include_router(transfer_router.router)


@app.get("/")
async def root() -> dict:
    return {"message": "Welcome To My Budget Planner App!:D"}


if __name__ == "__main__":
    PORT = 8000
    uvicorn.run(app, host="127.0.0.1", port=PORT)
