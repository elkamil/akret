import os
from os import listdir

from variables import folder_tmp

__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"


def clear_tmp_files(filename):
    for f in os.listdir(folder_tmp):
        if os.path.isfile(os.path.join(folder_tmp, f)):
            os.remove(folder_tmp + f)

