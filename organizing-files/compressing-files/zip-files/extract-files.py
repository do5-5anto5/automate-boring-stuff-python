import zipfile

to_extract = zipfile.ZipFile('example.zip')

# extracting to same folder
to_extract.extract('file1.txt')

# extracting to some other folder
# if the does not existis, the method create one
to_extract.extract('file1.txt', 'some/new/folder')