import shutil

from pathlib import Path

# store current path in a variable
current_dir = Path(__file__).parent
print(f'current dir: {current_dir}')

# copying to other folder (in case, one level above) does not need to rename
shutil.copy(current_dir / 'files/file1.txt', current_dir)

# copying to sample location, needs renaming the copy to create other file.
# Is not possible to create another file with same name
shutil.copy(current_dir / 'files/file1.txt', current_dir / 'files/file2.txt')
