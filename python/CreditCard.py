from pymodm import fields
from BaseAccount import BaseAccount
import config as CONFIG

class CreditCard(BaseAccount):
    cardNumber = fields.CharField()
    cardType = fields.CharField()
    creditLimit = fields.FloatField()
    availCreditLimit = fields.FloatField()
    availCashLimit = fields.FloatField()
    lastBilledDate = fields.DateTimeField()
    minAmountDue = fields.FloatField()
    lastBilledAmount = fields.FloatField()
    unbilledPurchases = fields.FloatField()
    unbilledPayments = fields.FloatField()
    outstandingTotal = fields.FloatField()
    paymentDueDate = fields.FloatField()
