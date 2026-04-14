import ezsheets

ss = ezsheets.Spreadsheet()
ss.title = 'Sheets'

sheet2 = ss.Sheet('Spam')
sheet3 = ss.Sheet('Eggs')

print(ss.sheetTitles)