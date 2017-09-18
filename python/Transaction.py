from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields

class authInfo(EmbeddedMongoModel):
    username = fields.CharField()
    password = fields.CharField()

class Transaction(MongoModel):
    _id = fields.CharField(primary_key = True)
    debitAccount = fields.ReferenceField()
    creditAccount = fields.ReferenceField()
    amount = fields.FloatField()
    reciept = fileds.ImageField()
    itemize = fields.EmbeddedDocumentField()
    budgetTag = fields.ReferenceField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'
