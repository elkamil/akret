__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import os
from os import listdir
from os.path import isfile, join

from variables import folder_tmp, Input_file


def MergeSplittedCSV():
    filenames = [f for f in listdir(folder_tmp + "split_csv/") if isfile(join(folder_tmp + "split_csv/", f))]
    open(folder_tmp + Input_file, 'w', encoding="utf8").close()
    with open(folder_tmp + Input_file, 'w', encoding="utf8") as mergedfile:
        for i in range(len(filenames)):
            with open(folder_tmp + "split_csv/" + str(i) + ".txt", encoding="utf8") as infile:
                mergedfile.write(infile.read())
            os.remove(folder_tmp + "split_csv/" + str(i) + ".txt", encoding="utf8")
