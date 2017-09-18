import config as CONFIG

class menu_list:
    def __init__(self):
        self._idx = 0
        self._menu_list = {}

    def addItem(self, item):
        self._menu_list[self._idx] = item
        self._idx += 1

    def show_seperator(self):
        print CONFIG.SEPERATOR

    def show(self):
        idx = 0
        for m in self._menu_list:
            print self._menu_list[idx].text(), "[", idx , "]"
            idx += 1

    def exec_menu_item(self):
        input = raw_input(CONFIG.INPUT_PROMPT)

        if input < len(self._menu_list):
            print "Invalid choice"
            return

        item = self._menu_list[int(input)].action()
        return item()

    def drive_menu(self):
        while True:
            self.show()
            self.exec_menu_item()
            self.show_seperator()
