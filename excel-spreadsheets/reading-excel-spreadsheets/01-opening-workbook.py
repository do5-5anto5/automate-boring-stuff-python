import openpyxl

wb_path = "excel-spreadsheets\\example3.xlsx"
workbook = openpyxl.load_workbook(wb_path)

print(type(workbook))

sheets = workbook.sheetnames
print(sheets)

sheet = workbook['Sheet3'] # getting a sheet from workbook
print(sheet)

current_sheet = workbook.active # getting active sheet
current_sheet_title = current_sheet.title # getting active sheet
print(current_sheet)
print(current_sheet_title)


