import os

from variables import folder_tmp, xlsx_folder, backup_folder, folder, pdf_folder, logs_dir


def create_structure():
    if not os.path.exists(xlsx_folder):
        os.makedirs(xlsx_folder)
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    if not os.path.exists(folder):
        os.makedirs(folder)
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    if not os.path.exists(folder_tmp):
        os.makedirs(folder_tmp)
