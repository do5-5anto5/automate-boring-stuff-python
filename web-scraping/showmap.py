# showmap.py Launches a map with browser, showing location inputed by clipboard or command line

import sys, pyperclip, webbrowser

def open_street_map():
    """
    Open a map with browser, showing location inputed by clipboard or command line
    If command line arguments are provided, they are joined with a space to form the address.
    Otherwise, the address is copied from the clipboard.
    The address is then used to open a search page on openstreetmap.org in the default browser.
    """
    if len(sys.argv) > 1:
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()

    webbrowser.open('https://www.openstreetmap.org/search?query=' + address)

open_street_map()