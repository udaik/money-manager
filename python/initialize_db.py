from pymodm import connect
from Asset import Asset
from BankAccount import BankAccount

connect("mongodb://localhost:27017/pymod-test", alias="MoneyManager")

asset = Asset("Test-Asset1", "BANK")
asset.save()
