from pymodm import MongoModel, fields
from BaseAccount import BaseAccount
import config as CONFIG

class Equity(BaseAccount):

    def decrease(self, amount):
        self.balance += amount

    def increase(self, amount):
        self.balance -= amount

    def debit(self, amount):
        self.decrease(self, amount)

    def credit(self, amount):
        self.increase(self, amount)
