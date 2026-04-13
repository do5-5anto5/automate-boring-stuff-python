import openpyxl
from openpyxl.styles import Font
from pathlib import Path


def set_font_style():
    """
    Create an Excel spreadsheet with a single cell in the first sheet that
    has the value "Hello, world!" and is styled with the Impact font in
    size 24 and italicized.

    Saves the spreadsheet to a file named "set_font_style.xlsx" in the
    same directory as this script.
    """
    workbook = openpyxl.Workbook()

    sheet = workbook.active

    times_bold_font = Font(name="Times New Roman", bold=True)
    impact_italic_24_font = Font(name='Impact', size=24, italic=True)

    sheet["a1"].font = times_bold_font
    sheet["a1"].value = "Bold Times New Roman"

    sheet['b3'].font = impact_italic_24_font
    sheet['b3'].value = 'Italic Impact 24'

    path = Path(__file__).parent
    workbook.save(path / "set_font_style.xlsx")


set_font_style()
