__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from variables import folder_tmp, wpisy, result_no_blank_lines, line_numbers
import re


def NumeryLiniiDoPodzialu():
    Wpisy_file = folder_tmp+wpisy
    Output_file = folder_tmp+result_no_blank_lines
    test1 = open(Wpisy_file, 'w')
    # licznik = re.compile('^[0-9]+\s?\.\s?[Ww]')
    # licznik = re.compile('^([0-9]+\s?\.|[0-9]+\s?[0-9]+\s?\.)\s?[Ww]')
    licznik = re.compile('^(([0-9]+\s?\.|[0-9]+\s?[0-9]+\s?\.)\s?[Ww]|([0-9]+\s?\.|[0-9]+\s?[0-9]+\s?\.).*\()')
    with open(Output_file, 'r') as plik:
            numery_linii_do_podzialu = []
            with open(folder_tmp+line_numbers, 'w') as output:
                    for line_i, line in enumerate(plik, 1):
                        if licznik.search(line):
                            output.write("%d\n" % line_i)
                            test1.write("%s\n" % line)
                            numery_linii_do_podzialu.append(line_i)
    return numery_linii_do_podzialu
    test1.close()

NumeryLiniiDoPodzialu()
