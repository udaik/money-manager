from pymodm import connect
from Asset import Asset
from BankAccount import BankAccount

connect(CONFIG.URI, alias=CONFIG.CONN_NAME)

asset = Asset("Test-Asset5", "BANK").save()
asset.bankAccount = BankAccount(1000.00, 1000.00, 1000.00)
asset.save()
