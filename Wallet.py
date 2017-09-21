from pymodm import EmbeddedMongoModel, fields

class Wallet(BaseAccount):
    rateOfInterest = fields.FloatField()
