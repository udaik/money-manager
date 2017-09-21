from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields
from pymodm.errors import ValidationError, ConfigurationError

from BankAccount import BankAccount
from CreditCard import CreditCard
from MutualFund import MutualFund
from Wallet import Wallet

LIABILITY_TYPES = ("CREDIT_CARD", "LOAN")

class Liability(MongoModel):
    name = fields.CharField(primary_key = True)
    acntType = fields.CharField(choices = LIABILITY_TYPES)
    # bankAccount = fields.EmbeddedDocumentField(BankAccount)
    # creditCard = fields.EmbeddedDocumentField(CreditCard)
    # mutualFund = fields.EmbeddedDocumentField(MutualFund)
    # wallet = fields.EmbeddedDocumentField(Wallet)
    collection_name = "Assets"

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'Money-Manager'
        collection_name = "Liabilities"

    def clean(self):
        """if (self.acntType == "BANK" and not self.bankAccount):
            raise ValidationError('Bank Account data not set')
        elif(self.acntType == "CREDIT_CARD" and not self.creditCard):
            raise ValidationError('Credit Card data not set')
        elif(self.acntType == "MUTUAL_FUND" and not self.mutualFund):
            raise ValidationError('Mutual Fund not set')
        elif(self.acntType == "WALLET" and not self.wallet):
            raise ValidationError('Mutual Fund not set')"""
