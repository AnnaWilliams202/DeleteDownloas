import os
import shutil
from datetime import datetime

# Define source and destination directories
downloads_dir = 'Downloads'
backup_dir = 'Backup'

# Ensure the backup directory exists
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Create a timestamped subdirectory within the backup directory
timestamp = datetime.now().strftime('©Y%m%d%H%M%S' )
backup_subdir = os.path.join(backup_dir, timestamp)
os. makedirs (backup_subdir)

# Walk through the files and directories in the Downloads folder
for root, dirs, files in os.walk(downloads_dir):
    for file in files:
        filepath = os.path.join(root, file)
        relative_path = os.path.relpath(filepath, downloads_dir)
        backup_path = os.path.join(backup_subdir, relative_path)

        # Ensure the target directory exists
        os.makedirs(os.path.dirname(backup_path), exist_ok=True)

        # Move the file and print the action
        print(f"Moving {filepath} to {backup_path}")
        shutil.move(filepath, backup_path)

    for dir in dirs:
        dirpath = os.path.join(root, dir)
        relative_path = os.path.relpath(dirpath, downloads_dir)
        backup_path = os.path.join(backup_subdir, relative_path)

        # Ensure the target directory exists
        os.makedirs(os.path.dirname(backup_path), exist_ok=True)

        # Move the directory and print the action
        print(f"Moving {dirpath} to {backup_path}")
        shutil.move(dirpath, backup_path)