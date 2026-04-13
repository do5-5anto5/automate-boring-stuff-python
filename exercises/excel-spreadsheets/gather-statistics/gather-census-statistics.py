import openpyxl, pprint
from pathlib import Path

workbook = openpyxl.load_workbook(
    "exercises\\excel-spreadsheets\\gather-statistics\\censuspopdata.xlsx"
)
sheet = workbook.active

county_data = {}

for row in range(2, sheet.max_row +1):
    state = sheet['b' + str(row)].value
    county = sheet['c' + str(row)].value
    pop = sheet['d' + str(row)].value

    county_data.setdefault(state, {})

    county_data[state].setdefault(county, {'pop': 0, 'tracts': 0})

    county_data[state][county]['pop'] += int(pop)
    county_data[state][county]['tracts'] += 1

print(county_data['AK'])

path = Path(__file__).parent

with open(path/'census2010.py', 'w') as result_file:
    result_file.write('allData = ' + pprint.pformat(county_data))
