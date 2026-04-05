# This scrpit save backup compressed snapshots from a folder filled with text files
# The files is organized by name order

from pathlib import Path
import os, zipfile

import zipfile, os
from pathlib import Path


def backup_to_file_zip(folder: Path):

    # ensure folder is a Path obj
    folder = Path(folder)
    # count the snapthot number
    number = 1

    # set the zip filename
    while True:
        zip_filename = Path(f"{folder}_{number}.zip")
        if not Path.exists(zip_filename):
            break
        number += 1

    # create de zip file to store the backup
    zip_backup = zipfile.ZipFile(zip_filename, "w")

    # iterate the folder compressing files
    for folder_name, _, filenames in os.walk(folder):
        path = Path(folder_name)
        print(path)

        for filename in filenames:
            print(f"Saving {filename} in folder: {folder_name}")
            zip_backup.write(
                path / filename, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9
            )

    zip_backup.close()
    print("Done.")


backup_to_file_zip(Path("files-to-backup"))
