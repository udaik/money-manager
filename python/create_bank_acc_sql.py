import sqlite3
import sys
import os
import uuid
import datetime
import BankAccount

if __name__ == '__main__' :
    if len(sys.argv) < 2:
        print "db file needed"
        sys.exit(-1)

    if not os.path.isfile(sys.argv[1]):
        print "db ", sys.argv[1]," not present"
        sys.exit(-1)

    try:
        conn = sqlite3.connect(sys.argv[1])
    except Exception, e:
        print "Unable to connect the db file" , str(e)

    b = BankAccount.BankAccount()
    b.populate_data()
    str = 'INSERT INTO MM_Account (' + b.keys_get() + ')' + ' VALUES (' +  b.values_get() + ')'
    print str
    conn.execute(str)

    conn.commit()
    conn.close()
