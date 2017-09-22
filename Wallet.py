from pymodm import fields
from BaseAccount import BaseAccount

class Wallet(BaseAccount):
    rateOfInterest = fields.FloatField()
