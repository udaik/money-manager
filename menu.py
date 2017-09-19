def _show_menu( menu ):
    for k in sorted(menu.keys()):
        print k, ": ", menu[k][1]

def _invoke_menu( menu, item ):
    try:
        menu[item][0](item)
    except Exception, e:
        print "menu item not found", str(e)

def key_get():
    c = None
    try:
        c = raw_input('Enter your choice: ')
    except Exception, e:
        print "error occured" , str(e)
    return c

def drive_menu( menu ):
    while True:
        _show_menu( menu )
        k = key_get()
        _invoke_menu( menu, k )
