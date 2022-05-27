from unicodedata import decomposition


class Account:
    def __init__(self,balance,account_name):
        self.balance=balance
        self.name=account_name
    def dep(self,amount):
        self.balance+=amount
        return f"Your new balance is{self.balance}"
    def withdraw(self,amount):
        self.balance-=amount
        return f"Your new balance is {self.balance}"
