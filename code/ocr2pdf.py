__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

import multiprocessing
import re
from multiprocessing import Pool
from os import listdir
from os.path import isfile, join

from PyPDF2 import PdfFileReader

from clear_tmp import clear_pdf_splits, clear_csv_splits
from split_addition import pdf_splitter
from threads_ocr import ThreadOCR
from variables import folder_pdf_splits, pdf_folder


def threadStart(zz):
    i = 1
    g = multiprocessing.current_process()
    i = re.sub(r'\D', '', str(g))
    pdf = PdfFileReader(folder_pdf_splits + str(zz) + ".pdf")
    ilosc_stron = pdf.getNumPages()
    ThreadOCR(str(zz) + ".pdf", ilosc_stron, int(i), zz)


def OCRPDF(filename, folder):
    clear_pdf_splits()
    clear_csv_splits()
    # ilosc_stron = Ilosc_Stron_PDF(filename)
    pdf_splitter(pdf_folder + filename, folder_pdf_splits)
    onlyfiles = [f for f in listdir(folder_pdf_splits) if isfile(join(folder_pdf_splits, f))]
    only_files_len = len(onlyfiles)
    numCores = multiprocessing.cpu_count()
    # pool_number = multiprocessing.Pool(processes = numCores)
    with Pool(numCores + 1) as pool:
        pool.map(threadStart, (zz for zz in range(only_files_len)), chunksize=1)
    # for zz in range(only_files_len):
    # p = Process(target=ThreadOCR, args=[filename, ilosc_stron, i+1])

# OCRPDF("/home/ee/tmp/split_pdf1/")
