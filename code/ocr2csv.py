__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import csv
import re
from itertools import islice
import math

from tqdm import tqdm

from budynki.merge_ak import if_statements as budynki_merge
from budynki.variables_ak import header_csv as budynki_header
from grunty.merge_ak import if_statements as grunty_merge
from grunty.variables_ak import header_csv as grunty_header
from lokale.merge_ak import if_statements as lokale_merge
from lokale.variables_ak import header_csv as lokale_header
from variables import budynki_csv_file, lokale_csv_file, grunty_csv_file
from variables import folder_tmp, result_no_blank_lines
from variables import wpisy, line_numbers
import redis

redis_host = "localhost"
redis_port = 6379
redis_password = ""
grunty_regex = re.compile('^GRUNT\s?$', re.MULTILINE)
lokale_regex = re.compile('^GRUNT\s+LOKAL$', re.MULTILINE)
budynek_regex = re.compile('^GRUNT\s+BUDYNEK$', re.MULTILINE)
izby_regex = re.compile('Liczba\\s?izb', re.MULTILINE)
r = redis.StrictRedis(  host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


def Ilosc_Wierszy():
    Output_file = folder_tmp + result_no_blank_lines
    with open(Output_file, 'r', encoding="utf8") as output:
        ilosc_el = (sum(1 for _ in output))
        return ilosc_el


def NumeryLiniiDoPodzialu():
    Wpisy_file = folder_tmp + wpisy
    output_file = folder_tmp + result_no_blank_lines
    test1 = open(Wpisy_file, 'w')
    licznik = re.compile('^(([0-9]+\s?\.|[0-9]+\s?[0-9]+\s?\.)\s?[Ww]|([0-9]+\s?\.|[0-9]+\s?[0-9]+\s?\.).*\()')
    with open(output_file, 'r', encoding="utf8") as plik:
        numery_linii_do_podzialu = []
        with open(folder_tmp + line_numbers, 'w', encoding="utf8") as output:
            for line_i, line in enumerate(plik, 1):
                if licznik.search(line):
                    output.write("%d\n" % line_i)
                    test1.write("%s\n" % line)
                    numery_linii_do_podzialu.append(line_i)
    return numery_linii_do_podzialu


def OCR2CSV():
    # wybor = 1
    print("...Tworzenie pliku CSV z OCR...")
    numery_linii_do_podzialu = NumeryLiniiDoPodzialu()
    pbar_ocr2csv = tqdm(total=len(numery_linii_do_podzialu))
    ilosc_el = Ilosc_Wierszy()

    i = 0
    finito_grunty = open(folder_tmp + grunty_csv_file, 'w', newline='', encoding="utf8")
    finito_lokale = open(folder_tmp + lokale_csv_file, 'w', newline='', encoding="utf8")
    finito_budynki = open(folder_tmp + budynki_csv_file, 'w', newline='', encoding="utf8")
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
        with open(folder_tmp + result_no_blank_lines, 'r', encoding="utf8") as dane3:
            if i + 1 < len(numery_linii_do_podzialu):
                line = ''.join(islice(dane3, numery_linii_do_podzialu[i] - 1,
                                      numery_linii_do_podzialu[i + 1] - 1))
                line = re.sub('  ', ' ', line)
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
                line = ''.join(islice(dane3, numery_linii_do_podzialu[i] - 1,
                                      ilosc_el))
                if grunty_regex.search(line) is not None:
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
        r.set("progress", round(100*(pbar_ocr2csv.n/pbar_ocr2csv.total)))
        pbar_ocr2csv.update(1)
    finito_grunty.close()
    finito_budynki.close()
    finito_lokale.close()
    pbar_ocr2csv.close()
