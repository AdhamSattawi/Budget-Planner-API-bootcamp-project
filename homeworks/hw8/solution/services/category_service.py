from models.category import Category
from repository.category_repository import CategoryRepo, CategoryType


class BudgetCategory:
    def __init__(self, repo: CategoryRepo):
        self.repo = repo
        self.add_defaults()

    def get_all_categories(self) -> list[Category]:
        return self.repo.get_all()
    
    def add_category(self, name: str, type: CategoryType) -> Category:
        new_category = Category(id = 0, name = name, type = type)
        return self.repo.create(new_category)

    def delete_category(self, category_id: int) -> bool:
        category = self.repo.get(category_id)
        if not category:
            return False
        self.repo.delete(category_id)
        return True
    
    def add_defaults(self) -> None:
        if len(self.repo.get_all()) == 0:
            self.add_category(name = "Rent", type = "expense")
            self.add_category(name = "Freelancing", type = "income")
            self.add_category(name = "Groceries", type = "expense")
            self.add_category(name = "Work", type = "income")
            self.add_category(name = "SideHustle", type = "income")
            self.add_category(name = "Electronics", type = "expense")
            self.add_category(name = "HomeStuff", type = "expense")
            self.add_category(name = "CarMaintanance", type = "expense")
            self.add_category(name = "SelfCare", type = "expense")
            self.add_category(name = "Resturants", type = "expense")
