import pypdf
from filenames import PDF_FILENAME

writer = pypdf.PdfWriter()

writer.append(PDF_FILENAME)

# add_blank_page method adds a blank page to the end of file
page_blank = writer.add_blank_page()
print(page_blank)

# insert_blank_page method receives a index as parameter, inserting there a blank page
indexed_blank_page = writer.insert_blank_page(index=2)
print(indexed_blank_page)

with open("gen_files/insert_blank.pdf", "wb") as file:
    writer.write(file)
