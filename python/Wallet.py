from pymodm import EmbeddedMongoModel, fields

class Wallet(EmbeddedMongoModel):
    balance = fields.FloatField()
