import openpyxl
from pathlib import Path

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, 11):
    sheet["a" + str(i)] = i * i

ref_obj = openpyxl.chart.Reference(sheet, 1, 1, 1, 10)

series_obj = openpyxl.chart.Series(ref_obj, title='First series')

chart_obj = openpyxl.chart.BarChart()
chart_obj_title = 'My Chart'
chart_obj.append(series_obj)

sheet.add_chart(chart_obj, 'c5')
wb.save(Path(__file__).parent/'sampleChart.xlsx')