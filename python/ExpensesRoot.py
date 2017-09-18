from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields

class ExpenseRoot(MongoModel):
    name = fields.CharField(primary_key = True)

    currentBalance = fields.CharField()
    startDate = fields.DateTimeField()
    tenure = fields.IntergerField()
    maturityDate = fields.DateTimeField()
    interestAtMaturity = fields.FloatField()

    class InterestRate(EmbeddedMongoModel):
        interestRate = fields.ListField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'
