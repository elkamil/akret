__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from multiprocessing import Pool
import multiprocessing
from count_pages import Ilosc_Stron_PDF
from threads_ocr1 import ThreadOCR
from variables import folder_tmp
from split_addition import pdf_splitter
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileReader
import re

def threadStart(zz):
    i = 1
    # print(zz)
    g = multiprocessing.current_process()
    i = re.sub(r'\D', '', str(g))
    print("I::::" + i)
    folder = "/home/ee/tmp/split_pdf1/"
    pdf = PdfFileReader(folder+str(zz)+".pdf")
    ilosc_stron = pdf.getNumPages()
    ThreadOCR(str(zz)+".pdf", ilosc_stron, int(i), zz)


def OCRPDF(folder):
    i=1
    # ilosc_stron = Ilosc_Stron_PDF(filename)
    # pdf_splitter(filename, folder)
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    # print(onlyfiles)
    only_files_len = len(onlyfiles)
    numCores = multiprocessing.cpu_count()
    # pool_number = multiprocessing.Pool(processes = numCores)
    with Pool(numCores) as pool:
        pool.map(threadStart, (zz for zz in range(only_files_len)), chunksize=1)
    # print("Tutaj"+zz)
    # for zz in range(only_files_len):
        # p = Process(target=ThreadOCR, args=[filename, ilosc_stron, i+1])

OCRPDF("/home/ee/tmp/split_pdf1/")
