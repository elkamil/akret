__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from variables import folder_tmp, Input_file
import os
from os import listdir
from os.path import isfile, join


def MergeSplittedCSV():
    filenames = [f for f in listdir(folder_tmp+"split_csv/") if isfile(join(folder_tmp+"split_csv/", f))]
    open(folder_tmp+Input_file, 'w').close()
    with open(folder_tmp+Input_file, 'w') as mergedfile:
        for i in range(len(filenames)):
            with open(folder_tmp+"split_csv/"+str(i)+".txt") as infile:
                mergedfile.write(infile.read())
            os.remove(folder_tmp+"split_csv/"+str(i)+".txt")
