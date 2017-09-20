from pymodm import EmbeddedMongoModel, fields

class AccountTransferInfo(EmbeddedMongoModel):
    accountNumber = fields.CharField()
    ifscCode = fields.CharField()

class SavingsAccountInfo(EmbeddedMongoModel):
    accountNumber = fields.CharField()
