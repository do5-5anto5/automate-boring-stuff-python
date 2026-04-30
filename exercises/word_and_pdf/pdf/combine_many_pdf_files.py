import pypdf, os

writer = pypdf.PdfWriter()

# create a list with selected pdf files
pdf_filenames = [
    file
    for file in os.listdir(
        "D:/DevTools/web/code/automate-boring-stuff-python/gen_files"
    )
    if file.endswith(".pdf") and not file.startswith('encrypted')
]

pdf_filenames.sort(key=str.lower)

for filename in pdf_filenames:
    writer.append(f'D:/DevTools/web/code/automate-boring-stuff-python/gen_files/{filename}')

with open('D:/DevTools/web/code/automate-boring-stuff-python/gen_files/combined_files.pdf', 'wb') as file:
    writer.write(file)

print(pdf_filenames)
