from datetime import datetime as dt
import shutil
import os


def save_backup(src_filepath: str, backup_path: str, file_name: str) -> None:
    shutil.copy(src_filepath, backup_path)
    tstamp = dt.now().strftime("%Y%m%d%H%M%S")
    os.rename(backup_path + file_name,
              backup_path + file_name.split('.')[0]
              + tstamp + '.' + file_name.split('.')[1])
