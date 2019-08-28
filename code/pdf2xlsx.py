__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

# -*- coding: utf-8 -*-
import time
#from shutil import copyfile
#from split_pdf_file import split_pdf
from variables import folder_tmp, folder_pdf_splits, pdf_folder
#from ocr2pdf import OCRPDF
from count_pages import Ilosc_Stron_PDF
#from merge_csv import MergeSplittedCSV
from csv_remove_blank_lines import RemoveBlankLines
from csv2xlsx import CSV2XLSX
#from clear_tmp import clear_tmp_files
from ocr2csv import OCR2CSV
#from split_addition import pdf_splitter
from create_structure import create_structure
#from sendEmail import sendemail
#from sendBeforeEmail import sendbeforeemail
#from isOnline import isOnline
import os
import subprocess
#import ghostscript

def main(filename, wybor):
    #create_structure()
    ilosc_stron = Ilosc_Stron_PDF(pdf_folder+filename)
    print(time.strftime("%H:%M:%S"))
    # folder = folder_tmp + "split_pdf/"
    # pdf_splitter(pdf_folder+filename, folder)
    # OCRPDF(filename,pdf_folder)

    #if ilosc_stron > 5:
        # split_pdf(pdf_folder+filename)
     #   processes = []
     #   filename_split = [split_pdf_1, split_pdf_2, split_pdf_3]
       # for i in range(3):
        #    splited_pdf = filename_split[i]
        #    processes.append(OCRPDF(folder_tmp+splited_pdf, i))
        #for p in processes:
        #    p.start()
        #for p in processes:
        #    p.join()
        # MergeSplittedCSV(folder_tmp+"result"+str(1)+".txt",
        #                 folder_tmp+"result"+str(2)+".txt",
        #                 folder_tmp+"result"+str(3)+".txt")
    #else:
     #   processes = []
      #  processes.append(OCRPDF(pdf_folder+filename, 0))
       # for p in processes:
        #    p.start()
        #for p in processes:
        #    p.join()
        #copyfile(folder_tmp+"result1.txt", folder_tmp+"result.txt")

    # MergeSplittedCSV()
    gs = "C:\\Program Files\\gs\\gs9.26\\bin\\gswin64c.exe"
   # os.system(gs+' -sDEVICE=txtwrite -o '+folder_tmp+"result.txt"' '+ pdf_folder+filename)
    file = folder_tmp+"result.txt"
    #subprocess.check_output([gs,'-sDEVICE=txtwrite','-sOUTPUTFILE=result.txt',pdf_folder+filename])
    subprocess.Popen([gs, '-sDEVICE=txtwrite','-dNOPAUSE', '-sOUTPUTFILE=C:\\Users\\User\\PycharmProjects\\akret\\code\\tmp\\result.txt',pdf_folder+filename])
    print("test")
    #args = [ "-sDEVCE=txtwrite", "-sOutputFile="+folder_tmp+"result.txt", "-f " +pdf_folder+filename]
    #ghostscript.Ghostscript(*args)
    RemoveBlankLines()
    # if isOnline():
    #     sendbeforeemail(filename)
    print(wybor)
    OCR2CSV(wybor)
    xlsx_f = CSV2XLSX(filename, wybor)
    #if isOnline():
    #    sendemail(filename, xlsx_f)
    # clear_tmp_files(filename)
    print(time.strftime("%H:%M:%S"))
    return xlsx_f


if __name__ == "__main__":
    # main("zkk17.te.6621.1863.2018_wolny_rynek.pdf", 1)
    main("")
