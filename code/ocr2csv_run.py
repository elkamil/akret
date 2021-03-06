__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from csv_record_separator import NumeryLiniiDoPodzialu
from csv_rows_count import Ilosc_Wierszy
# from choose_method import choose_method
from variables import folder_tmp, result_no_blank_lines, budynki_csv_file, lokale_csv_file, grunty_csv_file
from itertools import islice
from tqdm import tqdm
import csv
import re

# from csv2xlsx import CSV2XLSX
from grunty.variables_ak import header_csv as grunty_header
from grunty.merge_ak import if_statements as grunty_merge
from budynki.variables_ak import header_csv as budynki_header
from budynki.merge_ak import if_statements as budynki_merge
from lokale.variables_ak import header_csv as lokale_header
from lokale.merge_ak import if_statements as lokale_merge
grunty_regex = re.compile('^GRUNT$', re.MULTILINE)
lokale_regex = re.compile('^GRUNT LOKAL$', re.MULTILINE)
budynek_regex = re.compile('^GRUNT BUDYNEK$', re.MULTILINE)
izby_regex = re.compile('Liczba\\s?izb', re.MULTILINE)


def OCR2CSV(wybor):
    print("...Tworzenie pliku CSV z OCR...")
    numery_linii_do_podzialu = NumeryLiniiDoPodzialu()
    pbar_ocr2csv = tqdm(total=len(numery_linii_do_podzialu))
    ilosc_el = Ilosc_Wierszy()
    # choose = choose_method(wybor)
    # header_csv = choose[0]
    # if_statements = choose[1]

    i = 0
    finito_grunty = open(folder_tmp+grunty_csv_file, 'w', newline='')
    finito_lokale = open(folder_tmp+lokale_csv_file, 'w', newline='')
    finito_budynki = open(folder_tmp+budynki_csv_file, 'w', newline='')
    writer_grunty = csv.DictWriter(finito_grunty, fieldnames=grunty_header,
                                   delimiter=';', quoting=csv.QUOTE_ALL)
    writer_grunty.writeheader()
    writer_budynki = csv.DictWriter(finito_budynki, fieldnames=budynki_header,
                                    delimiter=';', quoting=csv.QUOTE_ALL)
    writer_budynki.writeheader()
    writer_lokale = csv.DictWriter(finito_lokale, fieldnames=lokale_header,
                                   delimiter=';', quoting=csv.QUOTE_ALL)
    writer_lokale.writeheader()
    while i < len(numery_linii_do_podzialu):
        with open(folder_tmp+result_no_blank_lines, 'r') as dane3:
            if i+1 < len(numery_linii_do_podzialu):
                line = ''.join(islice(dane3, numery_linii_do_podzialu[i]-1,
                                      numery_linii_do_podzialu[i+1]-1))
                # print(line)
                if grunty_regex.search(line) is not None:
                    if izby_regex.search(line) is not None:
                        z = lokale_merge(line)
                        writer_lokale = csv.writer(finito_lokale, delimiter=';',
                                                quoting=csv.QUOTE_ALL)
                        writer_lokale.writerows(z)
                    else:
                        z = grunty_merge(line)
                        writer_grunty = csv.writer(finito_grunty, delimiter=';',
                                                quoting=csv.QUOTE_ALL)
                        writer_grunty.writerows(z)
                elif budynek_regex.search(line) is not None:
                    z = budynki_merge(line)
                    writer_budynki = csv.writer(finito_budynki, delimiter=';',
                                                quoting=csv.QUOTE_ALL)
                    writer_budynki.writerows(z)
                elif lokale_regex.search(line) is not None:
                    z = lokale_merge(line)
                    writer_lokale = csv.writer(finito_lokale, delimiter=';',
                                               quoting=csv.QUOTE_ALL)
                    writer_lokale.writerows(z)
            else:
                line = ''.join(islice(dane3, numery_linii_do_podzialu[i]-1,
                                      ilosc_el))
                if grunty_regex.search(line) is not None:
                    # z = if_statements(line)
                    z = grunty_merge(line)
                    writer_grunty = csv.writer(finito_grunty, delimiter=';',
                                               quoting=csv.QUOTE_ALL)
                    writer_grunty.writerows(z)
                elif budynek_regex.search(line) is not None:
                    z = budynki_merge(line)
                    writer_budynki = csv.writer(finito_budynki, delimiter=';',
                                                quoting=csv.QUOTE_ALL)
                    writer_budynki.writerows(z)
                elif lokale_regex.search(line) is not None:
                    z = lokale_merge(line)
                    writer_lokale = csv.writer(finito_lokale, delimiter=';',
                                               quoting=csv.QUOTE_ALL)
                    writer_lokale.writerows(z)
                # z = if_statements(line)
        i += 1
        pbar_ocr2csv.update(1)
    finito_grunty.close()
    finito_budynki.close()
    finito_lokale.close()
    pbar_ocr2csv.close()
    # CSV2XLSX('budy', wybor)


OCR2CSV(1)
