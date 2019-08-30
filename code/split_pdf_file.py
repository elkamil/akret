import math

from PyPDF2 import PdfFileReader, PdfFileWriter

from count_pages import Ilosc_Stron_PDF
from variables import folder_tmp, split_pdf_1, split_pdf_2, split_pdf_3


def split_pdf(filename):
    inputpdf = PdfFileReader(open(filename, "rb"), strict=False)
    ilosc_stron = Ilosc_Stron_PDF(filename)

    split_point = math.ceil(ilosc_stron / 3)

    with open(folder_tmp + split_pdf_1, "wb") as outputStream:
        output = PdfFileWriter()
        for i in range(split_point):
            output.addPage(inputpdf.getPage(i))
            output.write(outputStream)

    with open(folder_tmp + split_pdf_2, "wb") as outputStream:
        output = PdfFileWriter()
        for i in range(split_point, ilosc_stron - split_point):
            output.addPage(inputpdf.getPage(i))
            output.write(outputStream)
    with open(folder_tmp + split_pdf_3, "wb") as outputStream:
        output = PdfFileWriter()
        for i in range(ilosc_stron - split_point, ilosc_stron):
            output.addPage(inputpdf.getPage(i))
            output.write(outputStream)
    return split_point, ilosc_stron - split_point
