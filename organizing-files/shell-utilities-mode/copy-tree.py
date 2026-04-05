import shutil
from pathlib import Path

current_dir = Path(__file__).parent

files_backup = shutil.copytree(current_dir / 'files', current_dir / 'backup_files')

print (files_backup)