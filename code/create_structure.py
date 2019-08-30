import os

from variables import folder_pdf_splits, folder_csv_splits


def create_structure():
    if not os.path.exists(folder_pdf_splits):
        os.makedirs(folder_pdf_splits)
    if not os.path.exists(folder_csv_splits):
        os.makedirs(folder_csv_splits)
