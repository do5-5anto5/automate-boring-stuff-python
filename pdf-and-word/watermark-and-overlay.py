import pypdf
from filenames import PDF_FILENAME

writer = pypdf.PdfWriter()
writer.append(PDF_FILENAME)

watermark_page = pypdf.PdfReader("gen_files/watermark.pdf").pages[0]

for page in writer.pages:
    page.merge_page(
        watermark_page, over=True
    )  # the parameter 'over' defines if the watermark_page content is under or over the merged page content

with open("gen_files/with_watermark.pdf", "wb") as file:
    writer.write(file)
