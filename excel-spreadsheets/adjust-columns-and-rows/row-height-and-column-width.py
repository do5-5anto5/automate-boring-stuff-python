import openpyxl
from pathlib import Path

def dimensions():
    """
    Creates an Excel spreadsheet with a single sheet that contains
    a row with a height of 70 and a column with a width of 20.

    Saves the spreadsheet to a file named "dimensions.xlsx" in the
    same directory as this script.
    """
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet['a1'] = 'Tall row'
    sheet['b2'] = 'Wide column'

    sheet.row_dimensions[1].height = 70
    sheet.column_dimensions['b'].width = 20

    path = Path(__file__).parent

    workbook.save(path/'dimensions.xlsx')

dimensions()