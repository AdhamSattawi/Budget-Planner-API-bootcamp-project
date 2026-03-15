from functools import wraps


# transactions data save decoration func
def info_save(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        func_output = func(self, *args, **kwargs)
        self.transactions.append(func_output)
        return func_output

    return wrapper


class BankAccount:
    def __init__(self, account_id: str, _balance: float = 0) -> None:
        self.account_id = account_id
        self._balance = _balance
        self.transactions: list[str] = []

    @property
    def balance(self) -> float:
        return self._balance

    @info_save
    def deposit(self, amount: float) -> str:
        if amount <= 0:
            raise ValueError("Can't deposit zero or nagative amount.")
        self._balance += amount
        return f"deposited {amount}"

    @info_save
    def withdraw(self, amount: float) -> str:
        if amount > self._balance:
            raise ValueError("no enough money.")
        if amount <= 0:
            raise ValueError("Can't withdraw zero or nagative amount.")
        self._balance -= amount
        return f"withdrew -{amount}"

    def get_statement(self) -> str:
        return f"statement for account {self.account_id}: current _balance is {self._balance}, transactions: {self.transactions}"
