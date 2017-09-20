from pymodm import fields
from BaseAccount import BaseAccount
import config as CONFIG

class BankAccount(BaseAccount):
    bankName = fields.CharField()
    ifscCode = fields.CharField()
    accountNumber = fields.CharField()
