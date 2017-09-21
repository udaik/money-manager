import sqlite3
import uuid

class database:

    def __init__(self, filename):
        self._dbfile = filename

    def open(self):
        print "opening sqlite conn", self._dbfile
        self._conn = sqlite3.connect(self._dbfile)

    def close(self):
        print "closing sqlite conn", self._dbfile
        self._conn.close()

    def commit(self):
        self._conn.commit()

    def account_create( self, account ):
        print "uuid ", str(uuid.uuid4())
        print "name ", account.name_get()
        print "type ", account.balance_get()
        # c.execute("INSERT INTO BANK_ACCOUNT VALUES ()")

        pass

if __name__ == '__main__' :
    filename = "example.db"
    db = database(filename)
    db.open()
    db.commit()
    db.close()
