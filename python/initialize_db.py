from pymodm import connect
from BankAccount import BankAccount
from MutualFund import MutualFund
from CreditCard import CreditCard
from Insurance import Insurance
from EPF import EmployeeProvidentFund


connect("mongodb://localhost:27017/mydb", alias="my-app")

BankAccount("SBI Joint", "Savings", 100.0, 200.0, "descr").save()
# b = BankAccount("SBI Joint")
