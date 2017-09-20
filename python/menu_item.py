
class menu_item:
    def __init__(self, action, help_text, key):
        self._action = action
        self._help = help_text
        self._key = key

    def action(self):
        return self._action

    def text(self):
        return self._help

    def key(self):
        return self._key
