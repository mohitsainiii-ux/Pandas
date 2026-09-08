import numpy as np


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


# Create 50 account numbers using NumPy
account_numbers = np.arange(1001, 1051)

# Create 50 balances using NumPy
balances = np.random.randint(1000, 50000, 50)

# Create BankAccount objects
accounts = []

for i in range(50):
    account = BankAccount(account_numbers[i], balances[i])
    accounts.append(account)


# Print all 50 employees' accounts
for account in accounts:
    print(account)