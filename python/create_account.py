import sys
import os
import datetime
import config as CONFIG
from Database import Database
from AccountType import AccountType

if __name__ == '__main__' :
    db = Database(CONFIG.URI, CONFIG.DATEBASE)
