import ezsheets

# converts adresses
print(ezsheets.convertAddress('a2'))
# converts adresses back
print(ezsheets.convertAddress(1, 2))

# get column letter
print(ezsheets.getColumnLetterOf(2))
# get column number
print(ezsheets.getColumnNumberOf('b'))