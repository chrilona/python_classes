class Account:
    # def __init__(self,balance,account_name):
    #     #balance is initially zero so it cannot be passed as an arguement 
    #     self.balance=balance
    #     self.name=account_name
    #     # rather self.balance=0
    def __init__(self,account_name,account_number):
       self.account_name=account_name
       self.account_number=account_number
       self.deposits=[]
       self.withdrawals=[]
       self.balance=0
    def dep(self,amount):
        dep=True
        self.balance+=amount
        if amount<=0:
            return f"Deposit must be a positive number"
        else:   
           return f"Hello {self.account_name}.Your new balance is {self.balance}"
        if dep is True:
            dep+=1
            print(f"You have deposited{dep}")
    # def withdraw(self,amount):
    #     if amount<=0:
    #         return f"You cannot withdraw nothing"
    #     elif amount>self.balance:
    #         return f"You cannot withdraw {amount} your balance is {self.balance}"
    #     else:
    #         self.balance-=amount
    #         return f" Hello {self.account_name},you have withdrawn {amount}.Your new balance is {self.balance}"
# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance.