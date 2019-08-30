__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import re

from variables import folder_tmp, Input_file, result_no_blank_lines, result_no_page_numbers

# def RemoveBlankLines():
#    blanks = folder_tmp+Input_file
#    output_tmp_file = folder_tmp+result_no_page_numbers
#    output_file = folder_tmp+result_no_blank_lines
#    with open(blanks, "r") as f, open(output_tmp_file, "w") as outfile_tmp:
#        for i in f.readlines():
#            if (not (re.search('^\d+$', i) or re.search('^\d+\s\d+$', i))):
#                outfile_tmp.write(i)
#
#    with open(output_tmp_file, "r") as f, open(output_file, "w") as outfile:
#        for i in f.readlines():
#            if not i.strip():
#                continue
#            if i:
#                outfile.write(i)
bad_words = [
    '--------------------------------------------------------------------------------------------------------------------------------------------']


def RemoveBlankLines():
    blanks = folder_tmp + Input_file
    output_tmp_file = folder_tmp + result_no_page_numbers
    output_file = folder_tmp + result_no_blank_lines
    with open(blanks, "r", encoding="utf8") as f, open(output_tmp_file, "w", encoding="utf8") as outfile_tmp:
        for i in f.readlines():
            i = re.sub(r'^\s+', '', i)
            i = re.sub(r'-----', '', i)
            if not re.search('^\\d+$', i):
                outfile_tmp.write(i)

    with open(output_tmp_file, "r", encoding="utf8") as f, open(output_file, "w", encoding="utf8") as outfile:
        for i in f.readlines():
            if not i.strip():
                continue
            if i and not any(bad_word in i for bad_word in bad_words):
                outfile.write(i)
