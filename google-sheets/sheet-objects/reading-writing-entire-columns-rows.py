import ezsheets

ss = ezsheets.upload('exercises\\excel-spreadsheets\\update-prices\\produceSales3.xlsx')
sheet = ss.sheets[0]

column_one = sheet.getColumn(1) # The first column or row is always 1, not 0

for i, value in enumerate(column_one):
    # make the Python list contain uppercase strings
    column_one[i] = value.upper()

# Update the entire column in one request
sheet.updateColumn(1, column_one) 

# getColumn() and getRow() retrieves data from every cel in a column or row as a list of values
rows = sheet.getRows() # Get every row in the spreadsheet.
rows[0] # Examine the values in the first row.
    # >>> ['PRODUCE', 'COST PER POUND', 'POUNDS SOLD', 'TOTAL', '', '']

rows[1] # ['POTATOES', '0.86', '21.6', '18.58', '', '']
rows[1][0] = 'PUMPKIN' # Change the produce name.
rows[1] # ['PUMPKIN', '0.86', '21.6', '18.58', '', '']

rows[10] # OKRA', '2.26', '40', '90.4', '', '']
rows[10][2] = '400' # Change the pounds sold.
rows[10][3] = '904' # Change the total.
rows[10] # OKRA', '2.26', '400', '904', '', '']

sheet.updateRows(rows) # Update the online spreadsheet with the changes.

sheet.rowCount # The number of rows in the sheet
sheet.columnCount # The number of columns in te sheet: 23758

# Change the number of rows to 4 (only ocuppied columns)
#   really useful to make the sheets only as big as needed
sheet.columnCount = 4 
