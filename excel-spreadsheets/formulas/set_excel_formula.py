import openpyxl
from pathlib import Path


def set_execel_formula():
    """
    Creates an Excel spreadsheet with a single sheet that contains a formula
    to calculate the sum of cells a1 to a3.

    Saves the spreadsheet to a file named "formula.xlsx" in the same directory
    as this script.
    """
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet['a1'].value = 200
    sheet['a2'].value = 300
    sheet['a3'].value = 400
    sheet['a4'].value = '=sum(a1:a3)'

    # Note that Python does'nt the calcule, it stores de formula in the cell
    print(sheet['a4'].value)

    path = Path(__file__).parent

    workbook.save(path/'formula.xlsx')

    

set_execel_formula()

# To see the value, is needed to open it in Excel, 
#   then save the file and reopen it with data_only=True

# wb = openpyxl.load_workbook(path/'formula.xlsx', data_only=True)
# sheet = wb.active

# print(sheet['a4'].value)