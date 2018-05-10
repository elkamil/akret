__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from variables import folder_tmp, Input_file, result_no_blank_lines, result_no_page_numbers
import re


def RemoveBlankLines():
    blanks = folder_tmp+Input_file
    output_tmp_file = folder_tmp+result_no_page_numbers
    output_file = folder_tmp+result_no_blank_lines
    with open(blanks, "r") as f, open(output_tmp_file, "w") as outfile_tmp:
        for i in f.readlines():
            if (not (re.search('^\d+$', i) or re.search('^\d+\s\d+$', i))):
                outfile_tmp.write(i)

    with open(output_tmp_file, "r") as f, open(output_file, "w") as outfile:
        for i in f.readlines():
            if not i.strip():
                continue
            if i:
                outfile.write(i)

RemoveBlankLines()
