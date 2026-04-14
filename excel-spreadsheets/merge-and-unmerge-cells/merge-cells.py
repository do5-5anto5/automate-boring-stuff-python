import openpyxl
from pathlib import Path

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet.merge_cells('a1:d3')

sheet['a1'] = 'Twelve chells merged together'

workbook.save(Path(__file__).parent/'merging_cells.xlsx')