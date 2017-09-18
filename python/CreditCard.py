from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields

class CreditCard(MongoModel):
    name = fields.CharField(primary_key = True)
    cardName = fields.CharField()
    cardType = fields.CharField()
    totalLiability = fields.CharField()
    creditLimit = fields.FloatField()
    cashLimit = fields.FloatField()
    availableCredit = fields.FloatField()
    loyaltyPoints = fields.FloatField()
    minimumPaymentDue = fields.FloatField9)
    dueDate = fields.DateTimeField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'
