import openpyxl
from pathlib import Path

# 'Freeze' rows above cell A2, it will be always visible,
# useful to spreadsheets tha are too large to be displayed at once.
# It can be done to columns freezing columns at left from the given cell

path = Path(__file__).parent

wb = openpyxl.load_workbook(path/'produceSales3.xlsx')
sheet = wb.active

sheet.freeze_panes = 'a2'

wb.save(path/'freezed_example.xlsx')