import ezsheets

ss = ezsheets.Spreadsheet('https://autbor.com/examplegs')
print(f'Loaded "{ss.title}" spreadsheet')

ss.downloadAsExcel() # downloads the spreadsheet as an excel file
ss.downloadAsODS() # downloads the spreadsheet as an OpenOffice file
ss.downloadAsCSV() # downloads the spreadsheet as a CSV file
ss.downloadAsTSV() # downloads the spreadsheet as a TSV file
ss.downloadAsPDF() # downloads the spreadsheet as a PDF file
ss.downloadAsHTML() # downloads the spreadsheet as a ZIP of HTML file

## CSV and TSV files can contain just one sheet

# download the spreadsheet as an excel file, changing filename.
#  the same can be done to other download methods.
#  the function returns the local filename
ss.downloadAsExcel('a_different_filename.xlsx') 
