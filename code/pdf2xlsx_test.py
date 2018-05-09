__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

# -*- coding: utf-8 -*-
import time
from shutil import copyfile
from split_pdf_file import split_pdf
from variables import folder_tmp, split_pdf_1, split_pdf_2, split_pdf_3, pdf_folder
from ocr2pdf import OCRPDF
from count_pages import Ilosc_Stron_PDF
from merge_csv import MergeSplittedCSV
from csv_remove_blank_lines import RemoveBlankLines
from csv2xlsx import CSV2XLSX
from clear_tmp import clear_tmp_files
from ocr2csv import OCR2CSV
from sendEmail import sendemail


def main(filename, wybor):
    print(filename)
    print(wybor)
    ilosc_stron = Ilosc_Stron_PDF(pdf_folder+filename)
    print(time.strftime("%H:%M:%S"))
    if ilosc_stron > 5:
        split_pdf(pdf_folder+filename)
        processes = []
        filename_split = [split_pdf_1, split_pdf_2, split_pdf_3]
        for i in range(3):
            splited_pdf = filename_split[i]
            processes.append(OCRPDF(folder_tmp+splited_pdf, i))
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        MergeSplittedCSV(folder_tmp+"result"+str(1)+".txt",
                         folder_tmp+"result"+str(2)+".txt",
                         folder_tmp+"result"+str(3)+".txt")
    else:
        processes = []
        processes.append(OCRPDF(pdf_folder+filename, 0))
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        copyfile(folder_tmp+"result1.txt", folder_tmp+"result.txt")

    RemoveBlankLines()
    OCR2CSV(wybor)
    xlsx_f = CSV2XLSX(filename, wybor)
    # sendemail(filename, xlsx_f)
    # clear_tmp_files(filename)
    print(time.strftime("%H:%M:%S"))
    return xlsx_f


if __name__ == "__main__":
    main()
