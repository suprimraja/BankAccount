class BankAccount:
    total_accounts = 0

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.__balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amt):
        if amt <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amt

    def withdraw(self, amt):
        if amt <= 0:
            raise ValueError("Withdraw must be positive.")
        if amt > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amt

    @property
    def balance(self):
        return self.__balance

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return BankAccount(self.owner + " & " + other.owner, self.balance + other.balance)


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0.0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.deposit(self.balance * self.interest_rate)


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0.0, overdraft_limit=0.0):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amt):
        if amt <= 0:
            raise ValueError("Withdraw must be positive.")
        if amt > self.balance + self._overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self._set_balance(self.balance - amt)

    def _set_balance(self, value):
        self._BankAccount__balance = value


if __name__ == "__main__":
    s = SavingsAccount("Raj", 500, 0.05)
    c = CheckingAccount("Priya", 300, 200)

    s.deposit(100)
    c.withdraw(400)
    s.apply_interest()

    print("Savings Balance:", s.balance)
    print("Checking Balance:", c.balance)

    merged = s + c
    print("Merged Owner:", merged.owner)
    print("Merged Balance:", merged.balance)
