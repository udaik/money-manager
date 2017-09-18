from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields

class authInfo(EmbeddedMongoModel):
    username = fields.CharField()
    password = fields.CharField()

class BankAccount(MongoModel):
    name = fields.CharField(primary_key = True)
    acntType = fields.CharField()
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
    authInfo = fields.EmbeddedDocumentListField(authInfo)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'
