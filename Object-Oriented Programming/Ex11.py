# Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions

class Bank:
    def __init__(self,name,acct_no,balance):
        self.name = name
        self.account_no = acct_no
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance

    def withdrawal(self,amount):
        self.balance = self.balance - amount

        
