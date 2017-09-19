from database import database
import menu

account_menu = { "c": (account_create,  "Create bank account") }

def account_create ():
    menu.drive_menu(account_menu)

def modify_account ():
    print modify_account()

def del_account():
    print del_account()

"""
class account:
    def __init__(self, db, name) :
        self._db = db
        self._name = name
        self._balance = 0

    def id_get(self):
        return self._id

    def ifsc_code_set(self, ifsc_code):
        self._ifsc_code = ifsc_code

    def ifsc_code_get(self, ifsc_code):
        return self._ifsc_code

    def name_get(self):
        return self._name

    def amb_set(self, amb):
        self._amb = amb

    def amb_get(self, amb):
        return self._amb

    def intr_rate_get(self):
        return self._interest_rate

    def intereset_rate_set(self, rate):
        self._interest_rate = rate

    def balance_get(self):
        return self._balance

    def account_number_get(self):
        return self._acnt_number

    def account_number_set(self, acnt):
        self._acnt_number = acnt


if __name__ == '__main__' :
    db = database("example.db")
    db.open()
    name = "HDFC BANK"
    acnt = account(db, name)
    db.account_create(acnt)
    db.close()
"""
