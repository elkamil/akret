# pdf_splitter.py
import os

from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(path, folder):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    ilosc_stron = pdf.getNumPages()
    strony = []
    for i in range(int(ilosc_stron / 10)):
        strony.append(i * 10)
    strony.append(int(ilosc_stron / 10) * 10 + ilosc_stron % 10)
    i = 0
    for i in range(len(strony) - 1):
        output_filename = '{}.pdf'.format(i)
        with open(folder + output_filename, 'wb') as out:
            pdf_writer = PdfFileWriter()
            for page in range(strony[i], strony[i + 1]):
                pdf_writer.addPage(pdf.getPage(page))
                pdf_writer.write(out)
