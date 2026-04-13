import openpyxl

workbook = openpyxl.load_workbook("excel-spreadsheets\example3.xlsx")
sheet = workbook['Sheet1']

# get print each cell coordinate and value from the slice, row by row
for row_of_cell_objects in sheet["A1":"C3"]:
    for cell_obj in row_of_cell_objects:
        print(cell_obj.coordinate, cell_obj.value)
    print('END OF ROW')

# get every value from an entire column
column1 = list(sheet.columns)[1]
print (column1)
for cell in column1:
    print(cell.value)