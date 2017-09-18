from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields

class MutualFund(MongoModel):
    name = fields.CharField(primary_key = True)
    fundName = fields.CharField()
    scheme = fields.CharField()
    units = fields.FloatField()
    cost = fields.FloatField()
    nav = fields.FloatField()
    value = fields.FloatField()
    folioNumber = fields.FloatField()
    
    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'
