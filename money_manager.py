import sys
import config as CONFIG
import readchar
from menu_item import menu_item
from menu_list import menu_list
from pymodm import connect
from BaseAccount import BaseAccount
from BankAccount import BankAccount
from LoanAccount import LoanAccount
from ExpenseAccount import ExpenseAccount

def create_account():
    b = {'b': "Bank Account",
         'l': "Loan Account",
         'c': "Credit Card",
         'e': "Expense Account",
         'i': "Insurance Account" }
    print("Creating Account", b)
    key = readchar.readkey()
    acnt = None

    if key == 'b':
        acnt = BankAccount()
        acnt.populate()
    elif key == 'l':
        acnt = LoanAccount()
        acnt.populate()
    elif key == 'c':
        acnt = CreditCard()
        acnt.populate()
    elif key == 'e':
        acnt = ExpenseAccount()
        acnt.populate()
    elif key == 'i':
        acnt = Insurance()
        acnt.populate()
    else:
        return

    acnt.save()


def delete_account():
    pass

def modify_account():
    pass

def quit_local_menu():
    return "quit"

def account_menu():
    menu = menu_list()
    menu.addItem(menu_item(create_account, "Create Account", 'a'))
    menu.addItem(menu_item(delete_account, "Delete Account", 'd'))
    menu.addItem(menu_item(modify_account, "Modify Account", 'm'))
    menu.addItem(menu_item(quit_local_menu, "Quit Menu", 'q'))
    menu.drive_menu()

def create_transaction():
    pass

def delete_transaction():
    pass

def modify_transaction():
    pass

def transaction_menu ():
    menu = menu_list()
    menu.addItem(menu_item(create_transaction, "Create Transaction", 'a'))
    menu.addItem(menu_item(delete_transaction, "Delete Transaction", 'd'))
    menu.addItem(menu_item(modify_transaction, "Modify Transaction", 'm'))
    menu.addItem(menu_item(quit_local_menu, "Quit Menu", 'q'))
    menu.drive_menu()

def app_quit():
    print("exiting")
    quit()

menu = menu_list()
menu.addItem(menu_item(transaction_menu, "Transaction Menu", 't'))
menu.addItem(menu_item(account_menu, "Account Menu", 'a'))
menu.addItem(menu_item(app_quit, "Quit money manager", 'q'))

if __name__ == '__main__' :
    connect(CONFIG.URI, alias = CONFIG.CONN_NAME)
    menu.drive_menu()
