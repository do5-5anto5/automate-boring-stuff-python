import pypdf
from pdf_and_word.filenames import PDF_FILENAME

def isEncrypetd(reader: pypdf.PdfReader):
    print(reader.is_encrypted)

reader = pypdf.PdfReader('gen_files/encrypted.pdf')
writer = pypdf.PdfWriter()
isEncrypetd(reader)

print()

# trying to decrypt with wrong password
result = reader.decrypt('wrong password').name
print(result)

# decrypting with right password
result = reader.decrypt('swordfish').name
print(result)
print()
print(reader.pages[0])

writer.append(reader)
with open('gen_files/decrypted.pdf', 'wb') as file:
    writer.write(file)