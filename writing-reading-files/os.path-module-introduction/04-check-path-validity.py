# Many Python functions will crash with an error if you supply them with a
# path that does not exist. The os.path module provides functions to check
# whether a given path exists and whether it is a file or folder.

import os

folder_path = "C\\Windows\\System32"
file_path = "C:\\Windows\\System32\\calc.exe"

# •	 Calling os.path.exists(path) will return True if the file or folder referred
# to in the argument exists and will return False if it does not exist.
file_path_check = os.path.exists(file_path)

# •	 Calling os.path.isfile(path) will return True if the path argument exists
# and is a file and will return False otherwise.
isfile_path_check = os.path.isfile(file_path)

# •	 Calling os.path.isdir(path) will return True if the path argument exists
# and is a folder and will return False otherwise.
isdir_check = os.path.isdir(folder_path)

print(file_path_check)
print(isfile_path_check)
print(isdir_check)
