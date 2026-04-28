"""
This file has example to read and extract information from pdf files
libs used: pypdf and pdfminer.six
    ''' python -m pip install pypdf pdfminer.six ''' on terminal

The paragraphs extracted may not be in the same order as the original pdf
recomended to use some IA to fast format the text
"""

import pypdf
import pdfminer.high_level
from filenames import PDF_FILENAME, TEXT_FILENAME



text =''
try:
    # read the pdf file
    reader = pypdf.PdfReader(PDF_FILENAME)

    # extract text from pdf file
    for page in reader.pages:
        text += page.extract_text()

    # write the text to a file
    with open(TEXT_FILENAME,'w', encoding='UTF-8') as file_obj:
        file_obj.write(text)

#  if fail for a particular PDF file and launch an exception, fall back on the pdfminer module
except Exception as e:
    text = pdfminer.high_level.extract_text(PDF_FILENAME)
    with open(TEXT_FILENAME,'w', encoding='UTF-8') as file_obj:
        file_obj.write(text)

