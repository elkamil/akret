__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import subprocess
# -*- coding: utf-8 -*-
import time

from clear_tmp import clear_tmp_files
from count_pages import Ilosc_Stron_PDF
from csv2xlsx import CSV2XLSX
from csv_remove_blank_lines import RemoveBlankLines
from ocr2csv import OCR2CSV
from variables import folder_tmp, pdf_folder


def main(filename, wybor):
    # create_structure()
    ilosc_stron = Ilosc_Stron_PDF(pdf_folder + filename)
    print(time.strftime("%H:%M:%S"))
    gs = "C:\\Program Files\\gs\\gs9.26\\bin\\gswin64c.exe"
    file = folder_tmp + "result.txt"
    ocr = subprocess.Popen([gs, '-sDEVICE=txtwrite', '-dNOPAUSE', '-dBATCH',
                      '-sOUTPUTFILE=C:\\Users\\User\\PycharmProjects\\akret\\code\\tmp\\result.txt',
                      pdf_folder + filename])
    ocr.wait()
    ocr.kill()
    ocr.poll()

    RemoveBlankLines()
    # if isOnline():
    #     sendbeforeemail(filename)
    print(wybor)
    OCR2CSV(wybor)
    xlsx_f = CSV2XLSX(filename, wybor)
    # if isOnline():
    #    sendemail(filename, xlsx_f)
    clear_tmp_files(filename)
    print(time.strftime("%H:%M:%S"))
    return xlsx_f


if __name__ == "__main__":
    # main("zkk17.te.6621.1863.2018_wolny_rynek.pdf", 1)
    main()
