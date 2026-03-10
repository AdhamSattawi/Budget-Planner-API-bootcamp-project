class BaseEmployee:

    EMPLOYEES = []
    
    def __init__(self, employee_id: int, full_name: str, hourly_rate: float = 0.0) -> None:
        self.employee_id = employee_id
        self.full_name = full_name
        self.hourly_rate = hourly_rate
        BaseEmployee.EMPLOYEES.append(employee_id)

    def __add__(self, other):
        return self.compensation() + other.compensation()

    def compensation(self) -> float:
        working_hours = 160 # 160 hours per mounth
        monthly_payment = self.hourly_rate * working_hours
        return monthly_payment
    
    def get_info(self) -> str:
        info = f"""
        Employee ID: {self.employee_id}, 
        Name: {self.full_name}, 
        Hourly rate: {self.hourly_rate:.2f} $/hr
        Work schedule: Standard 40 hours/week
        """
        return info
    

class FullTimeEmployee(BaseEmployee):
    def __init__(self, employee_id: int, full_name: str, annual_salary: float, department: str) -> None:
        super().__init__(employee_id, full_name)
        self.annual_salary = annual_salary
        self.department = department

    def compensation(self):
        months_per_year = 12
        monthly_payment = self.annual_salary / months_per_year
        return monthly_payment
    
    def get_info(self):
        info = f"""
        Employee ID: {self.employee_id}, 
        Name: {self.full_name}, 
        Salary: {self.annual_salary:.2f} $/year,
        Department: {self.department},
        Benefits: standard package
        """
        return info
    
class Manager(FullTimeEmployee):
    def __init__(self, employee_id: int, full_name: str, annual_salary: float, department: str, team_size: int, bonus_percentage: float) -> None:
        super().__init__(employee_id, full_name, annual_salary, department)
        self.team_size = team_size
        self.bonus_percentage = bonus_percentage

    def compensation(self):
        return super().compensation() * (1 + self.bonus_percentage)
    
    def get_info(self):
        info = f"""
        Employee ID: {self.employee_id}, 
        Name: {self.full_name}, 
        Salary: {self.annual_salary:.2f} $/year,
        Department: {self.department},
        Team Size: {self.team_size},
        Bonus Percentage: {self.bonus_percentage}
        Benefits: standard package plus bonus compensation
        Additional responsibility: Must track and report team size
        """
        return info