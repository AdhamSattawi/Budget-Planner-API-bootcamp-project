
company = {
    "departments": [
        {
            "name": "Engineering",
            "teams": [
                {
                    "name": "Backend",
                    "employees": [
                        {"name": "Alice", "salary": 120000},
                        {"name": "Bob", "salary": 110000}
                    ]
                },
                {
                    "name": "Frontend",
                    "employees": [
                        {"name": "Charlie", "salary": 105000}
                    ]
                }
            ]
        },
        {
            "name": "Sales",
            "teams": [
                {
                    "name": "Direct Sales",
                    "employees": [
                        {"name": "Diana", "salary": 95000},
                        {"name": "Eve", "salary": 98000}
                    ]
                }
            ]
        }
    ]
}

def get_all_employee_names(company: dict) -> list[str]:
    employee_names = [
        employee["name"] 
        for dept in company["departments"]
        for team in dept["teams"]
        for employee in team["employees"]
        ]
    return employee_names

def get_employees_by_department(company: dict, department: str) -> list[str]:
    employee_names = [
        employee["name"] 
        for dept in company["departments"]
        for team in dept["teams"]
        for employee in team["employees"]
        if dept["name"] == department
        ]
    return employee_names

def get_average_salary_by_department(company: dict) -> dict[str, float]:
    ...

def get_high_earners(company: dict, threshold: int) -> dict[str, list[str]]:
    ...

print(get_all_employee_names(company))
print(get_employees_by_department(company, "Engineering"))
print(get_average_salary_by_department(company))