from pymodm import connect
from datetime import datetime
import json
from termcolor import colored
from Wallet import Wallet
from BankAccount import BankAccount
from LoanAccount import LoanAccount
from CreditCard import CreditCard
from Equity import Equity
from BaseAccount import MetaInfo
import config as CONFIG

connect(CONFIG.URI, alias=CONFIG.CONN_NAME)

# Create Equity:Open balance
equity = Equity(name="Equity:Opening Balance", balance=0.0,
                description="Equity:Opening Balance", dateCreated=datetime.now())
equity.metaInfo = MetaInfo(updates=0)
equity.save()

def load_json_file(file):
    with open(file) as json_data:
        return json.load(json_data)

def objects_not_indb(inputAccountList, dbObjects):
    acc_in_db = set()
    for acc in dbObjects:
        acc_in_db.add(acc.name)

    inputList = set()
    for acc in inputAccountList:
        inputList.add(acc['name'])

    return inputList - acc_in_db

def bankAccountCreate(bankAccount):
    b = bankAccount
    dbAcnt = BankAccount(name=b['name'], description=b['description'],
                         bankName=b['bankName'], ifscCode=b['ifscCode'],
                         accountNumber=b['accountNumber'],
                         interestRate=b['interestRate'],
                         mab = b['mab']).save()

    print("BankAccount", colored(dbAcnt.name), "created")

def bankAccountCreateList(bankAccountList):
    acnts = objects_not_indb(bankAccountList, BankAccount.objects.all())
    for bankAccount in bankAccountList:
        if bankAccount['name'] in acnts:
            bankAccountCreate(bankAccount)

def loanAccountCreate(loanAccount):
    l = loanAccount
    dbAcnt = LoanAccount(name=l['name'], description=l['description'],
                         bankName=l['bankName'], ifscCode=l['ifscCode'],
                         accountNumber=l['accountNumber'],
                         rateOfInterest=l['rateOfInterest']).save()
    print("Loan Account", colored(dbAcnt.name), "created")

def loanAccountCreateList(loanAccountList):
    acnts = objects_not_indb(loanAccountList, LoanAccount.objects.all())
    for loanAccount in loanAccountList:
        if loanAccount['name'] in acnts:
            loanAccountCreate(loanAccount)

def creditCardCreate(creditCard):
    c = creditCard
    dbAcnt = CreditCard(name=c['name'], description=c['description'],
                         cardNumber=c['cardNumber'], cardType=c['cardType'],
                         creditLimit=c['creditLimit'],
                         availCreditLimit=c['availCreditLimit'],
                         availCashLimit = c['availCashLimit'],
                         outstandingTotal = c['outstandingTotal'],
                         holdersName = c['holdersName']).save()
    print("Credit Card", colored(dbAcnt.name), "created")

def creditCardCreateList(creditCardList):
    acnts = objects_not_indb(creditCardList, CreditCard.objects.all())
    for creditCard in creditCardList:
        if creditCard['name'] in acnts:
            creditCardCreate(creditCard)

def walletCreate(wallet):
    w = wallet
    dbAcnt = Wallet(name=w['name'], description=w['description'],
                        rateOfInterest=w['rateOfInterest']).save()
    print("Wallet", colored(dbAcnt.name), "created")

def walletCreateList(walletList):
    acnts = objects_not_indb(walletList, Wallet.objects.all())
    for wallet in walletList:
        if wallet['name'] in acnts:
            walletCreate(wallet)

acntTypeList = ['BankAccount', 'LoanAccount', 'CreditCard', 'Wallet']

d = load_json_file('default_accounts.json')

for acnt in acntTypeList:
    if acnt == 'BankAccount':
        bankAccountCreateList(d[acnt])
    elif acnt == 'LoanAccount':
        loanAccountCreateList(d[acnt])
    elif acnt == 'CreditCard':
        creditCardCreateList(d[acnt])
    elif acnt == 'Wallet':
        walletCreateList(d[acnt])
    else:
        print(acnt, "import not implemented")
