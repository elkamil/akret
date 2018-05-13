__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from multiprocessing import Process
from count_pages import Ilosc_Stron_PDF
from threads_ocr import ThreadOCR
from variables import folder_tmp
from split_addition import pdf_splitter
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileReader


def OCRPDF(folder):
    i=1
    # ilosc_stron = Ilosc_Stron_PDF(filename)
    # pdf_splitter(filename, folder)
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    print(onlyfiles)
    only_files_len = len(onlyfiles)
    for zz in range(only_files_len):
        print(zz)
        pdf = PdfFileReader(folder+str(zz)+".pdf")
        ilosc_stron = pdf.getNumPages()
        ThreadOCR(str(zz)+".pdf", ilosc_stron, i, zz)
        # p = Process(target=ThreadOCR, args=[filename, ilosc_stron, i+1])
