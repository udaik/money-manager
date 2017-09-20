from pymodm import fields
from BankAccount import BankAccount
import config as CONFIG

class SavingsAccount(BankAccount):
    currency = fields.CharField()
