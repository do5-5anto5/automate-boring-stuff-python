import ezsheets

example_ss = ezsheets.Spreadsheet('https://autbor.com/examplegs')
ss = ezsheets.Spreadsheet()

# Acess the first spreadsheet from example and copy it to new spreadsheet
example_ss.sheets[0].copyTo(ss)

# Delete previous empty spreadsheet
ss.sheets[0].delete()

# change the title.
ss.title = 'Al Sweigart books'


# getting attributes
ss.id # the spreadsheet id

ss.url # the spreadsheet id

ss.sheetTitles # the spreadsheet id

ss.sheets[0] # the first sheet object in this spreadsheet

ss['Copy of Books'] # sheets can also be accessed by name/title

ss.Sheet('New Blank sheet') # create new sheet

ss.sheets[1].delete() # Delete the second sheet object in this spreadsheet


# if the spreadsheet changes in browser, the script can update the object to match the online data
ss.refresh()

