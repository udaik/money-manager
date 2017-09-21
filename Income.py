from pymodm import fields
from BaseAccount import BaseAccount
import config as CONFIG

class Income(BaseAccount):
    currency = fields.CharField()

    def charge(self, amount):
        self.balance -= amount

    def income(self, amount):
        self.balance += amount
