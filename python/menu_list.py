import sys
import readchar

import config as CONFIG

class menu_list:
    def __init__(self):
        self._menu_list = {}

    def addItem(self, item):
        self._menu_list[item.key()] = item

    def show_seperator(self):
        print(CONFIG.SEPERATOR)

    def show(self):
        for m in self._menu_list:
            print("[", m , "]", self._menu_list[m].text())

    def exec_menu_item(self):
        print(CONFIG.INPUT_PROMPT, end=' ')
        key = readchar.readkey()

        if not str.isalpha(key):
            return

        item = self._menu_list[key].action()
        return item()

    def drive_menu(self):
        while True:
            self.show()
            self.exec_menu_item()
            self.show_seperator()
