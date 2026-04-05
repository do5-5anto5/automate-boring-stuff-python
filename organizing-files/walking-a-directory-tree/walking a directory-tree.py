import os
from pathlib import Path

home = Path().home()
# listing all files and subfolders in a folder with os.listdir() method
files_and_subfolders = os.listdir(home)
print(files_and_subfolders)

# listing path objects in a folder with iterdir() method
path_objects = list(home.iterdir())
print(path_objects)

