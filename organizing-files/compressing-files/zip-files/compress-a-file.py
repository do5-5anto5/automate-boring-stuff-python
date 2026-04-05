import zipfile

with open('file1.txt', 'w', encoding='utf-8') as file:
    file.write('Hello' * 10_000)
    # this created file has among 49kb

with zipfile.ZipFile('example.zip', 'w') as example:
    example.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    # the compressed file has just 1kb

# as the open() method, if I dont want to overwrite the file,
# pass 'a' to second argument on zipfile.ZipFile(), to append mode