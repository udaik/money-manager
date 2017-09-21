from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields
from pymodm.errors import ValidationError, ConfigurationError

from BankAccount import BankAccount
from CreditCard import CreditCard
from MutualFund import MutualFund
from Wallet import Wallet

ACCOUNT_TYPES = ("ASSET", "LIABILITY", "EQUITY", "INCOME", "EXPENSE")
INCOME_TYPES = ("SALARY", "INCOME")
ASSET_TYPES = ("BANK", "MUTUAL_FUND", "SMALL_SAVING", "WALLET", "INSURANCE")
LIABILITY_TYPES = ("CREDIT_CARD", "LOAN")

class Account(MongoModel):
    name = fields.CharField(primary_key = True)
    balance = fields.FloatField()
    
    acntType = fields.CharField(choices = ACCOUNT_TYPES)
    incomeType = fields.CharField(choices = INCOME_TYPES)
    assetType = fields.CharField(choices = ASSET_TYPES)
    liabilityType = fields.CharField(choices = LIABILITY_TYPES)
    bankAccount = fields.EmbeddedDocumentField(BankAccount)
    creditCard = fields.EmbeddedDocumentField(CreditCard)
    mutualFund = fields.EmbeddedDocumentField(MutualFund)
    wallet = fields.EmbeddedDocumentField(Wallet)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'Money-Manager'
        collection_name = "Accounts"

    def clean(self):
        """if (self.acntType == "BANK" and not self.bankAccount):
            raise ValidationError('Bank Account data not set')
        elif(self.acntType == "CREDIT_CARD" and not self.creditCard):
            raise ValidationError('Credit Card data not set')
        elif(self.acntType == "MUTUAL_FUND" and not self.mutualFund):
            raise ValidationError('Mutual Fund not set')
        elif(self.acntType == "WALLET" and not self.wallet):
            raise ValidationError('Mutual Fund not set')"""
