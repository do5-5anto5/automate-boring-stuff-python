import os

# get an unique file size
file_path = "C:\\Windows\\System32\\calc.exe"
print(os.path.getsize(file_path))

# get size of all files in a directory
system32_path = "C:\\Windows\\System32"
files_list = os.listdir(system32_path)

total_size = 0

for filename in files_list:
    file_size = os.path.getsize(os.path.join(system32_path, filename))
    total_size += file_size

print(f"System32 total size: {total_size}")
