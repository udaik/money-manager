from pymodm import EmbeddedMongoModel, fields
from Authentication import AuthInfo

class BankAccount(EmbeddedMongoModel):
    bookBalance = fields.FloatField()
    availBalance = fields.FloatField()
    description = fields.CharField()
    overdraftLimit = fields.FloatField()
    unclearedBalance = fields.FloatField()
    drawingPower = fields.FloatField()
    currency = fields.CharField()
    rateOfInterest = fields.CharField()
    lienAmount = fields.CharField()
    monthlyAverageBalance = fields.FloatField()
    authInfo = fields.EmbeddedDocumentField(AuthInfo)

    
