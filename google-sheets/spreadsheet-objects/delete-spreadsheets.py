import ezsheets, time

# load the spreadsheet
ss = ezsheets.Spreadsheet()
ss.title = "Delete me"

# print spreadsheets listing and wait 10secs to check it in browser
print(f'{ezsheets.listSpreadsheets()}\n')
time.sleep(10)

# than delete the spreadsheet and print the list without it
ss.delete("Delete me")
print(ezsheets.listSpreadsheets())
