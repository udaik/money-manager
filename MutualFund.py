from pymodm import EmbeddedMongoModel, MongoModel, fields

class MutualFund(EmbeddedMongoModel):
    fundName = fields.CharField()
    schemeName = fields.CharField()
    units = fields.FloatField()
    cost = fields.FloatField()
    nav = fields.FloatField()
    value = fields.FloatField()
    folioNumber = fields.FloatField()
