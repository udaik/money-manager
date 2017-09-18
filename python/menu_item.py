
class menu_item:
    def __init__(self, action, help_text):
        self._action = action
        self._help = help_text

    def action(self):
        return self._action

    def text(self):
        return self._help
