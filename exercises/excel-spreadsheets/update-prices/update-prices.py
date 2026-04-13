import openpyxl
from pathlib import Path


def update_prices():
    """
    Update prices in an Excel spreadsheet.

    This function loads an Excel spreadsheet, updates the prices of certain
    produces in the spreadsheet, and then saves the updated spreadsheet to a
    new file.
    """
    workbook = openpyxl.load_workbook(
        "exercises/excel-spreadsheets/update-prices/produceSales3.xlsx"
    )

    sheet = workbook.active

    PRICE_UPDT = {"Lemon": 1.37, "Garlic": 1.15, "Celery": 3.18}

    # Loop skiping the first line (columns' titles)
    for row in range(2, sheet.max_row + 1):
        produce = sheet[f"a{row}"].value

        if produce in PRICE_UPDT:
            sheet[f"b{row}"].value = PRICE_UPDT[produce]

    path = Path(__file__).parent

    workbook.save(path / "produceSales4.xlsx")

update_prices()
