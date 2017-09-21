from termcolor import colored
from pymodm import connect
from datetime import datetime
from BaseAccount import MetaInfo
from ExpenseAccount import ExpenseAccount
import config as CONFIG

ExpAccounts = { 'shopping:clothes',
             'Auto:Fuel', 'Auto:Servicing', 'Auto:Repair',
             'Auto:Upkeep', 'Auto:Insurance', 'Auto:MonthlyCleaning',

             'Utilities:Udai_Phone', 'Utilities:Ammu_Phone',

             'Ammu:PocketMoney', 'Ammu:Servant', 'Ammu:Milk',
             'Ammu:Water', 'Ammu:Iron', 'Ammu:CableTv', 'Ammu:WinnyAuto',

             'Maintenance:HomeMainteanance', 'Maintenance:OtherMaintenance',

             'Food:Grocories', 'Food:Vegetables', 'Food:Dining:FastFood',
             'Food:Dining:Accompaniments', 'Food:Dining:Breakfast',
             'Food:Dining:Lunch', 'Food:Dining:Supper', 'Food:Dining:Snacks',

             'Bank:EMI', 'Bank:Interest', 'Bank:BankCharges',
             'Gifts:IPHC', 'Gifts:LordsChruch', 'Gifts:Ammamma', 'Gifts:Others',

             'Medical:Diagnostics',
             'Medical:DoctorsFee', 'Medical:Hospitalization', 'Medical:Medicines',

             'Celebrations:Gifts', 'Celebrations:Food', 'Celebrations:Cakes'}

# connect to the database
connect(CONFIG.URI, alias = CONFIG.CONN_NAME)

acc_in_db = set()
for acc in ExpenseAccount.objects.all():
    acc_in_db.add(acc.name)

# create only those that not present in the database
for exp in ExpAccounts - acc_in_db:
    acc = ExpenseAccount(name=exp, balance=0.0,
                         description=exp, dateCreated=datetime.now())
    acc.metaInfo = MetaInfo(updates=0)
    acc.save()
    print("Created new expense account", colored(acc.name, 'red'))
