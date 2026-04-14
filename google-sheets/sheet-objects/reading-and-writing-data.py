import ezsheets

ss = ezsheets.Spreadsheet()
ss.title = 'Writing and Reading Data'
sheet = ss[0] # get the first sheet

# writing data
sheet['a1'] = 'Name'
sheet['b1'] = 'Age'
sheet['c1'] = 'Favorite Movie'
sheet['a2'] = 'Quinto'
sheet['b2'] = '5'
sheet['c2'] = 'Robocop'


# reading data
print(f'{sheet['a1']}: {sheet['a2']}')
print(f'{sheet['b1']}: {sheet['b2']}')
print(f'{sheet['c1']}: {sheet['c2']}')