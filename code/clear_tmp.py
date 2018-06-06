import os
from variables import folder_tmp, folder_pdf_splits, folder_csv_splits, files
from os import listdir
from os.path import isfile, join

__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"


def clear_tmp_files(filename):
    for f in os.listdir(folder_tmp):
        if os.path.isfile(os.path.join(folder_tmp, f)):
            os.remove(folder_tmp+f)

def clear_pdf_splits():
    for f in [f for f in listdir(folder_pdf_splits)]:
        os.remove(folder_pdf_splits+f)

def clear_csv_splits():
    for f in [f for f in listdir(folder_csv_splits)]:
        os.remove(folder_csv_splits+f)
