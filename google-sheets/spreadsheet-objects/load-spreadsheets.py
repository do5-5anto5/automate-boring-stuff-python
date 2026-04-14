import ezsheets

ss1 = ezsheets.Spreadsheet('https://autbor.com/examplegs')
ss2 = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1TzOJxhNKr15tzdZxTqtQ3EmDP6em_elnbtmZIcyu8vI/')
ss3 = ezsheets.Spreadsheet('1TzOJxhNKr15tzdZxTqtQ3EmDP6em_elnbtmZIcyu8vI')

print('These are the same spreadsheet: ', ss1 == ss2 == ss3)