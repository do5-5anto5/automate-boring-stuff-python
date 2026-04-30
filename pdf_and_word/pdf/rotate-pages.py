import pypdf
from pdf_and_word.pdf.filenames import PDF_FILENAME

writer = pypdf.PdfWriter(PDF_FILENAME)

for i in range(len(writer.pages)):
    writer.pages[i].rotate(90)

with open('gen_files/rotate.pdf', 'wb') as file:
    writer.write(file)