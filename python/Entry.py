from pymongo.write_concern import WriteConcern
from pymodm import MongoModel, fields

import config as CONFIG

class Entry(MongoModel):
    id = fields.UUIDField()
    amount = fields.FloatField()
    debitAccount = field.ReferenceField(BaseAccount)
    creditAccount = field.ReferenceField(BaseAccount)
    dateTime = fields.DateTimeField()
    description = fields.CharField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = CONFIG.CONN_NAME
        collection_name = CONFIG.TRX_COLL_NAME
