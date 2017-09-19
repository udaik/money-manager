import config as CONFIG
import sys
import readchar

class menu_list:
    def __init__(self):
        self._idx = 0
        self._menu_list = {}

    def addItem(self, item):
        self._menu_list[self._idx] = item
        self._idx += 1

    def show_seperator(self):
        print(CONFIG.SEPERATOR)

    def show(self):
        idx = 0
        for m in self._menu_list:
            print(self._menu_list[idx].text(), "[", idx , "]")
            idx += 1

    def exec_menu_item(self):
        # c = readchar.readchar()
        print(CONFIG.INPUT_PROMPT, end=' ')
        key = readchar.readkey()

        if int(key) > len(self._menu_list):
            print("Invalid choice", key)
            return

        item = self._menu_list[int(key)].action()
        return item()

    def drive_menu(self):
        while True:
            self.show()
            self.exec_menu_item()
            self.show_seperator()
