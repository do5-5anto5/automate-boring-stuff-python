import openpyxl
from pathlib import Path

path = Path(__file__).parent

workbook = openpyxl.load_workbook(path/'merging_cells.xlsx')
sheet = workbook.active

sheet.unmerge_cells('a1:d3')

workbook.save(path/'unmerging_cells.xlsx')