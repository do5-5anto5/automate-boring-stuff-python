import zipfile

file_zip = zipfile.ZipFile('example.zip')

files_list = file_zip.filelist

for file in files_list:

    filename = file.filename
    file_size = file.file_size
    file_compress_size = file.compress_size

    print(f'''Filename: {filename}
File size: {file_size}
File compress size: {file_compress_size}
Compressed size is {round(file_size / file_compress_size, 2)}x smaller
''')

file_zip.close()