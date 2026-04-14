import ezsheets

# creating the spreadsheets
ss1 = ezsheets.Spreadsheet()
ss1.title = "First Spreadsheet"
ss2 = ezsheets.Spreadsheet()
ss2.title = "Second Spreadsheet"

# naming sheets
ss1[0].title = 'Spam'
ss2[0].title = 'Eggs'

# add dummy data  to First Spreadsheet
ss1[0].updateRow(1, ["Some", "Data", "Inserted", "At", "This", "Row"])

# copy the entire sheet to Second Spreadsheet
ss1[0].copyTo(ss2)

print(ss2.sheetTitles)
