from pymodm import connect
from Asset import Asset
from Account import Account
from BankAccount import BankAccount
from Wallet import Wallet
from CreditCard import CreditCard

import config as CONFIG

connect(CONFIG.URI, alias=CONFIG.CONN_NAME)

# Create Equity:Open balance
Account(name="Open Balance", acntType="EQUITY").save()

# Create Bank Accounts
# SBI Salary Account
sbi_sal = Account(name="SBI-Salary", acntType="ASSET").save()
sbi_sal.assetType = "BANK"
sbi_sal.bankAccount = BankAccount(bookBalance=0.0, availBalance=0.0, description='SBCHQ-CSA-PUB-IND-CSPLT-INR',
                                accountNumber='00000020077230265', ifscCode='SBIN0004155')
sbi_sal.save()

# HDFC Joint Account
hdfc_joint = Account(name="HDFC-JOINT", acntType="ASSET").save()
hdfc_joint.assetType = "BANK"
hdfc_joint.bankAccount = BankAccount(bookBalance=0.0, availBalance=0.0, description='SBCHQ-CSA-PUB-IND-CSPLT-INR',
                                accountNumber='00000020077230265', ifscCode='SBIN0004155')
hdfc_joint.save()

# sbi home loan
sbi_homeloan = Account(name="SBI-HomeLoan", acntType="ASSET").save()
sbi_homeloan.assetType = "BANK"
sbi_homeloan.bankAccount = BankAccount(bookBalance=0.0,
                                       availBalance=0.0,
                                       description='MC-SBI HL MAXGAIN (WOM) JUN 17',
                                       accountNumber='00000034497003740',
                                       ifscCode = 'SBIN0004155',
                                       rateOfInterest = 8.65)
sbi_homeloan.save()

# airtel
airtel = Account(name="AIRTEL Payments Bank", acntType="ASSET").save()
airtel.assetType = "WALLET"
airtel.wallet = Wallet(balance=0.0, accountNumber='9949989024')
airtel.save()

# paytm
paytm = Account(name="PAYTM payments bank", acntType="ASSET").save()
paytm.assetType = "WALLET"
paytm.wallet = Wallet(balance=0.0, accountNumber='9949989024')
paytm.save()

# Wallet
wallet = Account(name="Wallet", acntType="ASSET").save()
wallet.assetType = "WALLET"
wallet.wallet = Wallet(balance=0.0, accountNumber='my-wallet')
wallet.save()

# HDFC Credit Card
hdfc_cc = Account(name="HDFC-CREDIT-CARD", acntType = "LIABILITY").save()
hdfc_cc.liabilityType = "CREDIT_CARD"
hdfc_cc.creditCard = CreditCard(creditLimit=227000.00, cashLimit=90800.00 )
hdfc_cc.save()

# CITI Credit Card
citi_cc = Account(name="CITI-CREDIT-CARD", acntType = "LIABILITY").save()
citi_cc.liabilityType = "CREDIT_CARD"
citi_cc.creditCard = CreditCard(creditLimit=97500.00, cashLimit=13000.00 )
citi_cc.save()

# Transaction Accounts
