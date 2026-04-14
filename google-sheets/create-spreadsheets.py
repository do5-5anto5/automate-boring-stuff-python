import ezsheets

ss = ezsheets.Spreadsheet()
ss.title = 'Title'

print(f'''Spreadsheet {ss.title}
url: {ss.url}
id: {ss.id}''')
