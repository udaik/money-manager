def _show_menu(menu):
    for m in sorted(menu):
        print menu[m][1], m

def _take_input():
    x = raw_input()

def drive_menu(menu):
    _show_menu(menu)
