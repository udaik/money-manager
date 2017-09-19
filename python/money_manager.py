import sys
import config

from menu_item import menu_item
from menu_list import menu_list
from pymodm import connect

def account_create ():
    print("account_create")

def account_modify ():
    print("Modify Account")

def add_transaction ():
    print("Add transaction")

def del_transaction ():
    print("delete transaction")

def menu_quit():
    print("exiting")
    quit()

menu = menu_list()

item = menu_item(add_trans, "Account Create")
menu.addItem(item)

item = menu_item(account_modify, "Account Modify")
menu.addItem(item)

item = menu_item(add_transaction, "Create transaction")
menu.addItem(item)

item = menu_item(del_transaction, "Delete transaction")
menu.addItem(item)

item = menu_item(menu_quit, "Quit money manager")
menu.addItem(item)

if __name__ == '__main__' :
    menu.drive_menu()
    connect(CONFIG.URI, alias=CONFIG.CONN_NAME)

    asset = Asset("Test-Asset5", "BANK").save()
    asset.bankAccount = BankAccount(1000.00, 1000.00, 1000.00)
    asset.save()
