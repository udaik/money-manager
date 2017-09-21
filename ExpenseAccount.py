from pymodm import MongoModel, fields
from BaseAccount import BaseAccount

class ExpenseAccount(BaseAccount):
    def expense(amount):
        balance += amount

    def rebate(amount):
        balance -= amount

    def populate(self):
        print("Adding a Expense account")
        self.name = input("Name: ")
        self.balance = 0.0
        self.description = input("Description: ")
