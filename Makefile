.PHONY: run test test-coverage lint format clean

# Sets PYTHONPATH to current directory so modules can find each other
export PYTHONPATH := $(PWD)

run:
	cd budget_planner_api && uvicorn api.main:app --reload

run-ui:
	cd budget_planner_api && python -m ui.app_ui

test:
	pytest budget_planner_api/tests/

test-coverage:
	pytest budget_planner_api/tests/ --cov=budget_planner_api --cov-report=term-missing

lint:
	flake8 budget_planner_api/
	mypy budget_planner_api/

format:
	black budget_planner_api/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .coverage .pytest_cache .mypy_cache
