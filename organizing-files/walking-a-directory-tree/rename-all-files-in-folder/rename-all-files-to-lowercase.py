# use os.walk() method to renaming each file to uppercase
import os, shutil
from pathlib import Path

home = Path(__file__).parent/'files'

for folder_name, subfolders, filenames in os.walk(home):
    print(f'FOLDER: {folder_name}')

    for subfolder in subfolders:
        print(f'SUBFOLDER of {folder_name}')

    for filename in filenames:
        print(f'FILE {filename} in FOLDER: {folder_name}')
        # renaming files
        path = Path(folder_name)
        shutil.move(path/filename, path/filename.lower())

# os.walk() returns a string for current folder name, 
# a list of strings for each subfolder in current folder 
# and a list of strings for each file in current folder