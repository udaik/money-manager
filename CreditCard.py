from pymodm import fields
from BaseAccount import BaseAccount

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
    holdersName = fields.CharField()

    def populate(self):
        print("Adding Banking Account")
        self.name = input("Name: ")
        self.balance = 0.0
        self.description = input("Description: ")
        self.cardNumber = input("Card Number: ")
        self.creditLimit = input("Credit Limit: ")
        self.availCreditLimit = input("Available Credit Limit")
        self.availCashLimit = input("Available Cash Limit")
        self.minAmountDue = 0.0
        self.lastBilledAmount = 0.0
        self.unbilledPurchases = 0.0
        self.unbilledPayments = 0.0
        self.outstandingTotal = 0.0

    def payment(self, amount):
        self.balance -= amount
        self.availCreditLimit += amount

    def paymentCash(self, amount):
        self.balance -= amount
        self.availCreditLimit += amount
        self.availCashLimit += amount

    def charge(self, amount):
        self.balance += amount
        self.availCreditLimit -= amount

    def chargeCash(self, amount):
        self.balance += amount
        self.availCreditLimit -= amount
        self.availCashLimit -= amount
