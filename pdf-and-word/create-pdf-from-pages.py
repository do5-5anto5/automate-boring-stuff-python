import pypdf
from filenames import PDF_FILENAME

writer = pypdf.PdfWriter()


# to add content to writer  use append() method
writer.append(PDF_FILENAME, (0,5))

# to insert copied pages before the end, use the merge() method
#   it inserts the copied content into an index, moving what was there to the end of the new content.
writer.merge(position=2, fileobj=PDF_FILENAME, pages=(6,9))

with open('gen_files/first_five_pages.pdf', 'wb') as file:
    # write or rewrite file
    writer.write(file)

    writer.append