__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from variables import folder_tmp, result_no_blank_lines


def Ilosc_Wierszy():
    Output_file = folder_tmp+result_no_blank_lines
    with open(Output_file, 'r',encoding="utf8") as output:
        ilosc_el = (sum(1 for _ in output))
        return ilosc_el
