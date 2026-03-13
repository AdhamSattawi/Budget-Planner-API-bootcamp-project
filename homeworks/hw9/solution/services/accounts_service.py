from decimal import Decimal
from solution.repository.account_repository import AccountRepo
from solution.models.account import Account
from solution.models.transaction import TransactionType
from solution.services.transaction_service import BudgetTransaction
from solution.services.transfer_service import BudgetTransfer


class BudgetAccount:
    def __init__(
        self,
        repo: AccountRepo,
        transaction_service: BudgetTransaction,
        transfer_service: BudgetTransfer,
    ) -> None:
        self.repo = repo
        self.transaction_service = transaction_service
        self.transfer_service = transfer_service

    def add_account(self, name: str, opening_balance: Decimal) -> Account:
        new_account = Account(id=0, name=name, opening_balance=opening_balance)
        return self.repo.create(new_account)

    def delete_account(self, account_id: int) -> bool:
        account = self._get_account(account_id)
        if account:
            self.repo.delete(account_id)
            return True
        else:
            return False

    def edit_account(self, account_id: int, new_name: str) -> Account | None:
        account = self._get_account(account_id) 
        if not account:
            return None
        account.name = new_name
        return self.repo.update(account)

    def get_balance(self, account_id: int) -> Decimal | None:
        account = self._get_account(account_id)
        opening_balance = account.opening_balance if account else Decimal(0)
        transactions = self._account_transactions(account_id)
        transfers = self._account_transfers(account_id)
        balance = opening_balance + transactions + transfers
        return balance

    def get_all_accounts(self) -> list[tuple[Account, Decimal | None]]:
        accounts = self.repo.get_all()
        if not accounts:
            return []
        all_accounts_balances = []
        for account in accounts:
            balance = self.get_balance(account.id)
            all_accounts_balances.append((account, balance))
        return all_accounts_balances

    def get_net_worth(self) -> Decimal:
        accounts = self.repo.get_all()
        total = Decimal(0)
        for account in accounts:
            balance = self.get_balance(account.id)
            if balance is not None:
                total += balance
        return total

    def _get_account(self, account_id: int) -> Account | None:
        account = self.repo.get(account_id)
        if account:
            return account
        else:
            return None

    def _account_transfers(self, account_id: int) -> Decimal:
        transfers = self.transfer_service.get_by_account(account_id)
        account_transfers_in: Decimal = Decimal(0)
        account_transfers_out: Decimal = Decimal(0)
        for transfer in transfers:
            if transfer.receiver_id == account_id:
                account_transfers_in += transfer.amount
            else:
                account_transfers_out += transfer.amount
        return account_transfers_in - account_transfers_out

    def _account_transactions(self, account_id: int) -> Decimal:
        transactions = self.transaction_service.get_by_account(account_id)
        account_incomes: Decimal = Decimal(0)
        account_expenses: Decimal = Decimal(0)
        for transaction in transactions:
            if transaction.type == TransactionType.expense:
                account_expenses += transaction.amount
            else:
                account_incomes += transaction.amount
        return account_incomes - account_expenses
