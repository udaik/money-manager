from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId

ACCOUNTS_COLLECTION = 'ACCOUNTS'
TRANSACTIONS_COLLECTION = 'TRANSACTIONS'

class Database:

    def __init__(self, uri, db):
        self._uri = uri
        self._client = MongoClient(uri)
        self._db = self._client[db]
        print "Connected to ", uri, db

    def account_create(self, account ):
        return self._db['ACCOUNTS_COLLECTION'].insert(account)

    def account_del( self, id ):
        return self._db['ACCOUNTS_COLLECTION'].delete_one({"_id": ObjectId(id)})

    def account_by_id ( self, id ):
        return self._db['ACCOUNTS_COLLECTION'].find_one({"_id": ObjectId(id)})

    def accounts_all_get(self):
        return self._db['ACCOUNTS_COLLECTION']

    def transactions_all_get ( self ):
        return self._db['TRANSACTIONS_COLLECTION']

    def transactions_add ( self, trx ):
        return self._db['TRANSACTIONS_COLLECTION'].insert(trx)

    def trasaction_del (self, trx_id):
        return self._db['TRANSACTIONS_COLLECTION'].delete_one({"_id": ObjectId(trx_id)})

    def close(self):
        self._client.close()

if __name__ == '__main__' :
    uri = 'mongodb://localhost:27017/'
    dbname = 'test_db'
    db = Database(uri, dbname)
    account = {"id": "1234", "name": "name1"}
    # print "inserted account", db.account_create(account)
    print "all accounts", db.accounts_all_get().find_one()
    print "get account ", db.account_by_id(ObjectId('59bcfaa5da6fa91efe452471'))
    print "delete account ", db.account_del(ObjectId('59bcfaa5da6fa91efe452471'))
    db.close()
