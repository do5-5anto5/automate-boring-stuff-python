import ezsheets

ss = ezsheets.Spreadsheet()
ss.title = "Multiple Sheets"

print(ss.sheetTitles)  # ('Sheet1',)


def print_titles():
    print(ss.sheetTitles)


ss.Sheet("Spam")
ss.Sheet("Eggs")


# Moving

print_titles()  # ('Sheet1', 'Spam', 'Eggs')

ss.Sheet("Bacon", 0)  # add sheet titled 'Bacon' to index 0
print_titles()  # ('Bacon', 'Sheet1', 'Spam', 'Eggs')

ss.sheets[0].index = 2  # move sheet from index 2 to index 0
print_titles()

ss.sheets[2].index = 0  # move sheet from index 2 to index 0
print_titles()  # ('Spam', 'Bacon', 'Sheet1', 'Eggs')


# Deleting
#   - deleting sheets is permanent

ss.sheets[0].delete() # Delete sheet indexed 0 ('Bacon')
print_titles()

ss['Spam'].delete() # Delete sheet by title
print_titles()

sheet = ss['Eggs']
sheet.delete() # Delete using a variable
print_titles()
