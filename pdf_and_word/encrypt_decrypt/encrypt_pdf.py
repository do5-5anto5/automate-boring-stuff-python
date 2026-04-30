import pypdf
from pdf_and_word.filenames import PDF_FILENAME

writer = pypdf.PdfWriter(PDF_FILENAME)

writer.encrypt('swordfish', algorithm='AES-256')

with open('gen_files/encrypted.pdf', 'wb') as file:
    writer.write(file)