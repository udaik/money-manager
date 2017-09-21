from pymongo.write_concern import WriteConcern
from pymodm import EmbeddedMongoModel, MongoModel, fields
from datetime import datetime
import config as CONFIG

class MetaInfo(EmbeddedMongoModel):
    updates = fields.IntegerField()

class BaseAccount(MongoModel):
    name = fields.CharField(primary_key = True)
    balance = fields.FloatField()
    description = fields.CharField()
    dateCreated = fields.DateTimeField()
    metaInfo = fields.EmbeddedDocumentField(MetaInfo)

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = CONFIG.CONN_NAME
        collection_name = CONFIG.COLLECTION_NAME

if __name__ == '__main__' :
    from pymodm import connect
    connect(CONFIG.URI, alias=CONFIG.CONN_NAME)
    base = BaseAccount(name="test", balance=100.0,
                description='test', dateCreated=datetime.now()).save()
