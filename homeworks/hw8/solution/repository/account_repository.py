from solution.repository.base_repository import BaseRepository
from solution.models.account import Account
from decimal import Decimal


class AccountRepo(BaseRepository[Account]):
    
    def _to_entity(self, row: dict) -> Account:
        #{id:, name:, opening_balance:}
        id = int(row["id"])
        name = row["name"]
        opening_balance = Decimal(row["opening_balance"])
        return Account(id = id, name = name, opening_balance = opening_balance)
    
    def _to_dict(self, account: Account) -> dict:
        id = account.id
        name = account.name
        opening_balance = account.opening_balance
        return {"id" : id, "name" : name, "opening_balance" : opening_balance}
    
