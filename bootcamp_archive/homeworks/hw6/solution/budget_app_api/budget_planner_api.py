from fastapi import FastAPI
import uvicorn
from core_functions.budget import Budget, Income, Expense

app = FastAPI()

my_budget = Budget()


@app.post("/income")
async def add_income_api(new_income: dict) -> dict:
    amount = new_income.get("amount")
    description = new_income.get("description")
    created_income = my_budget.add_income(amount, description)
    return {"Status": "success", "added": created_income.amount}


@app.post("/expense")
async def add_expense_api(new_expense: dict) -> dict:
    amount = new_expense.get("amount")
    description = new_expense.get("description")
    created_expense = my_budget.add_expense(amount, description)
    return {"Status": "success", "added": created_expense.amount}


@app.delete("/{type}/{id}")
async def delete_income_api(type: str, id: int) -> dict:
    my_budget.remove_by_id(type, id)
    return {"message": "Item has removed successfully"}


@app.delete("/clear")
async def clear_all_api() -> dict:
    my_budget.clear_all()
    return {"message": "Budget cleared successfully"}


@app.get("/summary")
async def summary_api() -> dict:
    total_incomes, total_expenses, remaning_budget = my_budget.view_summary()
    return {
        "Total Incomes": total_incomes,
        "Total Expenses": total_expenses,
        "Remaning Budget": remaning_budget,
    }

@app.get("/income")
async def view_incomes() -> dict:
    incomes = my_budget.view_incomes()
    incomes_dict = {}
    for id, income in incomes.items():
        incomes_dict[id] = {"amount" : income.amount, "description" : income.description}
    return incomes_dict

@app.get("/expense")
async def view_expenses() -> dict:
    expenses = my_budget.view_expenses()
    expenses_dict = {}
    for id, income in expenses.items():
        expenses_dict[id] = {"amount" : income.amount, "description" : income.description}
    return expenses_dict

if __name__ == "__main__":
    uvicorn.run("budget_app_api.budget_planner_api:app", reload=True)
