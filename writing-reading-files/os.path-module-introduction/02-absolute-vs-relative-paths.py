import os

# •	 Calling os.path.abspath(path) will return a string of the absolute path
# of the argument. This is an easy way to convert a relative path into an
# absolute one.
print(os.path.abspath("."))

# •	 Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.
print(os.path.isabs("D:\\DevTools\web\code\\automate-boring-stuff-python"))

# •	 Calling os.path.relpath(path, start) will return a string of a relative path
# from the start path to path.
print(os.path.isabs(os.path.abspath(".")))

# relpath 'discovers' the relative path from 'where you are' to given dir or file
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
print(os.path.relpath("C:\\Windows", "C:\\"))


# returns current running diretory
print(os.getcwd())

# Calling os.path.dirname(path) will return a string of everything that comes
# before the last slash in the path argument. Calling os.path.basename(path) will
# return a string of everything that comes after the last slash in the path argument

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.dirname(path))
print(os.path.basename(path))


# call os.path.split() to get a tuple value with these two strings

print(os.path.split(path))

# return a list of strings of each folder and the file
print(path.split(os.path.sep))