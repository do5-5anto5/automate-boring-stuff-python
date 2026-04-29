import pypdf
from filenames import PDF_FILENAME

writer = pypdf.PdfWriter(PDF_FILENAME)

for i in range(len(writer.pages)):
    writer.pages[i].rotate(90)

with open('gen_files/rotate.pdf', 'wb') as file:
    writer.write(file)