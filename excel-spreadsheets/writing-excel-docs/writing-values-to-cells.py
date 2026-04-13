import openpyxl

workbook = openpyxl.Workbook()

sheet = workbook.active

sheet['a1'].value = 'Hello, world!'

print (sheet['a1'].value)