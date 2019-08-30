from PyPDF2 import PdfFileReader

__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"


def Ilosc_Stron_PDF(plik_pdf):
    pdf = PdfFileReader(open(plik_pdf, 'rb'), strict=False)
    ilosc_stron = pdf.getNumPages()
    return ilosc_stron
