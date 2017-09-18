from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields

class Insurance(MongoModel):
    name = fields.CharField(primary_key = True)
    sumAssured = fields.CharField()
    tenure = fields.CharField()
    premiumDate = fields.DateTimeField()
    startDate = fields.DateTimeField()
    maturityDate = fields.DateTimeField()
    frequency = fields.CharField()
    policyType = fields.CharField()
    premiumPaymentTerm = fields.IntergerField()
    policyName = fields.CharField()
    bonus = fields.FloatField()
    maturityBenefit = fields.FloatField()
    
    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'
