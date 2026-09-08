# Bank Account
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"


# Savings Account
class SavingsAccount:
    def __init__(self, savings_account, balance=0):
        self.savings_account = savings_account
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def get_savings_account(self):
        return self.savings_account

    def __str__(self):
        return f"Savings Account: {self.savings_account}, Balance: {self.balance}"


# Checking Account
class CheckingAccount:
    def __init__(self, checking_account, balance=0):
        self.checking_account = checking_account
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def get_checking_account(self):
        return self.checking_account

    def __str__(self):
        return f"Checking Account: {self.checking_account}, Balance: {self.balance}"


# Create objects
account = BankAccount("ACC1001", 5000)
savings = SavingsAccount("SAV1001", 10000)
checking = CheckingAccount("CHK1001", 3000)

# Test
print(account)
print(savings)
print(checking)

account.deposit(1000)
print("After deposit:", account.get_balance())

checking.withdraw(500)
print("Checking balance:", checking.get_balance())