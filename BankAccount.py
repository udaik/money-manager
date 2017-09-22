from pymodm import fields
from BaseAccount import BaseAccount
import config as CONFIG

class BankAccount(BaseAccount):
    bankName = fields.CharField()
    ifscCode = fields.CharField()
    accountNumber = fields.CharField()
    interestRate = fields.FloatField()
    mab = fields.FloatField()
    holdersName = fields.CharField()

    def deposit(self, amount):
        balance += amount

    def withdraw(self, amount):
        balance -= amount

    def populate(self):
        print("Adding Banking Account")
        self.name = input("Name: ")
        self.balance = 0.0
        self.description = input("Description: ")
        self.bankName = input("Name of the Bank: ")
        self.ifscCode = input("IFSC code: ")
        self.accountNumber = input("Account Number: ")
        self.rateOfInterest = float(input("Rate of interest: "))
        self.mab = float(input("Monthly Average Balance: "))

if __name__ == '__main__' :
    from pymodm import connect
    connect(CONFIG.URI, alias=CONFIG.CONN_NAME)
    b = BankAccount(name="testBankAccount", balance=100.0,
                    description='test', bankName='sbi',
                    ifscCode='12312', accountNumber='12312',
                    interestRate='8.65').save()
    print(b.name)
