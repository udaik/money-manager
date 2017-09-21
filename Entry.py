from pymongo.write_concern import WriteConcern
from pymodm import MongoModel, fields
import datetime
from BaseAccount import BaseAccount

import config as CONFIG

class Entry(MongoModel):
    amount = fields.FloatField()
    debitAccount = fields.ReferenceField(BaseAccount)
    creditAccount = fields.ReferenceField(BaseAccount)
    dateTime = fields.DateTimeField()
    description = fields.CharField()
    debitAccountBalance = fields.FloatField()
    creditAccountBalance = fields.FloatField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = CONFIG.CONN_NAME
        collection_name = CONFIG.TRX_COLL_NAME

if __name__ == '__main__' :
    from pymodm import connect
    connect(CONFIG.URI, alias=CONFIG.CONN_NAME)
    b = BaseAccount(name="test", balance=100.0, description='test').save()
    entry = Entry(amount = 100, debitAccount = b,
                  creditAccount = b, dateTime = datetime.datetime.now()).save()
