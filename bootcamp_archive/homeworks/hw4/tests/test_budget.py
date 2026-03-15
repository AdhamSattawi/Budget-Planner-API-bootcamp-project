import pytest
from solution.budget import Budget

@pytest.fixture
def my_budget():
    return Budget()

def test_add_income(my_budget):
    my_budget.add_income(1000, "Freelance")
    my_budget.add_expense(500, "Food")
    assert len(my_budget.incomes) == 1
    assert len(my_budget.expenses) == 1
    assert my_budget.incomes[1].amount == 1000
    assert my_budget.incomes[1].description == "Freelance"
    assert my_budget.expenses[1].amount == 500
    assert my_budget.expenses[1].description == "Food"

def test_negative_income(my_budget):
    with pytest.raises(ValueError):
        assert my_budget.add_income(-1000, "Freelance")
        assert my_budget.add_expense(-1000, "Freelance")

def test_no_description(my_budget):
    with pytest.raises(ValueError):
        assert my_budget.add_income(1000, "")
        assert my_budget.add_expense(1000, "")

def test_remove_by_id(my_budget):
    my_budget.add_income(1000, "Freelance")
    my_budget.remove_by_id("income",1)
    assert len(my_budget.incomes) == 0

def test_remove_by_description(my_budget):
    my_budget.add_income(1000, "Freelance")
    my_budget.remove_by_description("income", "Freelance")
    assert len(my_budget.incomes) == 0

def test_clear_all(my_budget):
    my_budget.add_income(1000, "Freelance")
    my_budget.add_expense(1000, "Freelance")
    my_budget.clear_all()
    assert len(my_budget.incomes) == 0
    assert len(my_budget.expenses) == 0