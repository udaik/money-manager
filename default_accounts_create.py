from pymodm import connect
from datetime import datetime
import json
from BankAccount import BankAccount
from Equity import Equity
from BaseAccount import MetaInfo
import config as CONFIG

connect(CONFIG.URI, alias=CONFIG.CONN_NAME)

# Create Equity:Open balance
equity = Equity(name="Equity:Opening Balance", balance=0.0,
                description="Equity:Opening Balance", dateCreated=datetime.now())
equity.metaInfo = MetaInfo(updates=0)
equity.save()

with open('default_accounts.json') as json_data:
    d = json.load(json_data)
    print(d)
