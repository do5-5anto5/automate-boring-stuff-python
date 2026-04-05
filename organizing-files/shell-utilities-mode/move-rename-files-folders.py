import shutil
from pathlib import Path

current_dir = Path(__file__).parent

# if the destination already exists, you'll have an error
# so is better to check it before try to create new dir
if not Path.exists(current_dir / "files2"):
    Path.mkdir(current_dir / "files2")

# such as the file moving
if not Path.exists(current_dir / "files2/file1.txt"):
    shutil.move(current_dir / "file1.txt", current_dir / "files2")
else:
    print("The destination already has a file with this name.")
