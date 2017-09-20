from pymongo.write_concern import WriteConcern
from pymodm import MongoModel, fields

import config as CONFIG

class BaseAccount(MongoModel):
    name = fields.CharField()
    balance = fields.FloatField()
    description = fields.CharField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = CONFIG.CONN_NAME
        collection_name = CONFIG.COLLECTION_NAME
