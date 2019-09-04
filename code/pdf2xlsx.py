__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import re
import subprocess
# -*- coding: utf-8 -*-
import time

from PyPDF2 import PdfFileReader

from clear_tmp import clear_tmp_files
from csv2xlsx import CSV2XLSX
from ocr2csv import OCR2CSV
from variables import folder_tmp, Input_file, result_no_blank_lines, result_no_page_numbers, pdf_folder


def RemoveBlankLines():
    bad_words = [
        '--------------------------------------------------------------------------------------------------------------------------------------------']
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


def Ilosc_Stron_PDF(plik_pdf):
    pdf = PdfFileReader(open(plik_pdf, 'rb'), strict=False)
    ilosc_stron = pdf.getNumPages()
    return ilosc_stron


def main(filename):
    # create_structure()
    Ilosc_Stron_PDF(pdf_folder + filename)
    print(time.strftime("%H:%M:%S"))
    gs_exe = "C:\\Program Files\\gs\\gs9.26\\bin\\gswin64c.exe"
    # file = folder_tmp + "result.txt"
    ocr = subprocess.Popen([gs_exe, '-sDEVICE=txtwrite', '-dNOPAUSE', '-dBATCH',
                            '-sOUTPUTFILE=C:\\Users\\User\\PycharmProjects\\akret\\code\\tmp\\result.txt',
                            pdf_folder + filename])
    ocr.wait()
    ocr.kill()
    ocr.poll()

    RemoveBlankLines()
    # if isOnline():
    #     sendbeforeemail(filename)
    OCR2CSV()
    xlsx_f = CSV2XLSX(filename)
    # if isOnline():
    #    sendemail(filename, xlsx_f)
    clear_tmp_files(filename)
    print(time.strftime("%H:%M:%S"))
    return xlsx_f


if __name__ == "__main__":  #
    # main("przetargowe.pdf", 1)
    main(filename)
