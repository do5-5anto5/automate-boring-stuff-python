import os
from pathlib import Path


current_path = Path(__file__).parent
files2_dir = current_path / 'files2'

# first run the program commenting deletion line, and look at the logs to get attention to watch delete. like this:

# # remove a single file
# # single_remove = os.unlink(current_path / 'files2/file1 copy.txt')
# single_remove = current_path / 'files2/file1 copy.txt'
# print(f'Deleted {single_remove == None}')

# # remove selected various files
# for filename in files2_dir.glob('*.rtxt'):
#     # os.unlink(filename)
#     print(f'Deleting {filename}')

# then run deletion

if not Path.exists:
    single_remove = os.unlink(current_path / 'files2/file1 copy.txt')
    print(f'Deleted {single_remove == None}')

# remove selected various files
for filename in files2_dir.glob('*.rtxt'):
    os.unlink(filename)
    print(f'Deleting {filename}')

# removing an intire folder - it must be empty

files3_folder = Path.mkdir(current_path / 'files3') # create a temporary folder to show deletion
print(f'Create files3 folder')

os.rmdir(current_path / 'files3')
print('files3 folder deleted')

