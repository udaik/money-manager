from pymodm import fields
from BaseAccount import BaseAccount
import config as CONFIG

class LoanAccount(BaseAccount):
    bankName = fields.CharField()
    ifscCode = fields.CharField()
    accountNumber = fields.CharField()
    interestRate = fields.FloatField()
    availBalance = fields.FloatField()
    bookBalance = fields.FloatField()
    rateOfInterest = fields.FloatField()
    currency = fields.CharField()
    totalOutstanding = fields.FloatField()

    def payment(self, amount):
        self.balance -= amount

    def charge(self, amount):
        self.balance += amount

    def populate(self):
        print("Adding Banking Account")
        self.name = input("Name: ")
        self.balance = 0.0
        self.description = input("Description: ")
        self.bankName = input("Name of the Bank: ")
        self.ifscCode = input("IFSC code: ")
        self.accountNumber = input("Account Number: ")
        self.rateOfInterest = float(input("Rate of interest: "))
        self.availBalance = 0.0
        self.bookBalance = 0.0
        self.currency = input("Currency: ")
        self.totalOutstanding = 0.0

if __name__ == '__main__' :
    from pymodm import connect
    connect(CONFIG.URI, alias=CONFIG.CONN_NAME)
    l = LoanAccount(name="test", balance=100.0, description='test',
                    bankName='sbi', ifscCode='12312', accountNumber='12312',
                    availBalance=0.0, bookBalance=0.0, rateOfInterest=8.65,
                    currency='INR', totalOutstanding=0.0).save()
