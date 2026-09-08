#create a class for a bank account
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

#create a class for a bank account
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

#create a class for a bank account
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