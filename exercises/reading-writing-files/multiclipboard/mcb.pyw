import shelve, pyperclip, sys

# Open (or create) simple data file
mcbShelf = shelve.open('exercises\\reading-writing-files\\multiclipboard\\data\\mcb')

# case 1: comand 'save' - save current clipboard
# ex on terminal: py mcb.pyw save spam
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print('saved')    

#case 2: just 1 argument
elif len(sys.argv) == 2:

    # sub-case 2.1: "list" - show all keywords
    # ex on terminal: py mcb.pyw list
    if sys.argv[1].lower() == "list":
        # get shelved keys, converts to string
        keywords = str(list(mcbShelf.keys()))
        pyperclip.copy(keywords)
        print(f'Keywords copied {keywords}')

    # sub-case 2.2 - specific keyword - loads and copy saved text
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(f'Text from {sys.argv[1]} copied to clipboard.')
        

    # sub-case 2.3: keyword not found
    else:
        print(f'Keyword not {sys.argv[1]} not found.')

# case 3: invalid arguments
else:
    print("""
Correct use:
py exercises\reading-writing-files\multiclipboard\mcb.pyw save <keyword>   - saves current clipboard
py exercises\reading-writing-files\multiclipboard\mcb.pyw <keyword>        - loads saved text
py exercises\reading-writing-files\multiclipboard\mcb.pyw list             - lists all keywords
""")
    
mcbShelf.close()