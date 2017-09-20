import sys
import config as CONFIG

from menu_item import menu_item
from menu_list import menu_list
from pymodm import connect

def add_trans ():

    print("Add transaction")

def mod_trans ():
    print("Modify transaction")

def add_transaction ():
    print("Add transaction")

def del_trans ():
    print("delete transaction")

def menu_quit():
    print("exiting")
    quit()

menu = menu_list()

item = menu_item(add_trans, "Asset transfer", 'a')
menu.addItem(item)

item = menu_item(add_trans, "Add transaction", 'a')
menu.addItem(item)

item = menu_item(mod_trans, "Modify transaction", 'm')
menu.addItem(item)

item = menu_item(del_trans, "Delete transaction", 'd')
menu.addItem(item)

item = menu_item(menu_quit, "Quit money manager", 'q')
menu.addItem(item)

if __name__ == '__main__' :
    connect(CONFIG.URI, alias = CONFIG.CONN_NAME)
    menu.drive_menu()
