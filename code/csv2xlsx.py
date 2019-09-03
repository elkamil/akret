__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from shutil import copyfile

import pandas as pd

from csv_record_separator import NumeryLiniiDoPodzialu
from variables import folder_tmp, lokale_csv_file, grunty_csv_file, budynki_csv_file, static_dir, \
    pdf_folder, backup_folder, done_folder


# lokale mieszkalne


def CSV2XLSX(filename):
    print(filename)
    print(pdf_folder + "Probka.pdf")
    add_pdf = pdf_folder + "Probka.pdf"
    numery_linii_do_podzialu = NumeryLiniiDoPodzialu()
    #done_folder = static_dir + "lokale_mieszkalne/"

    xlsx_file = filename + ".xlsx"
    engine = 'xlsxwriter'
    print("..Konwersja CSV na Excel...")
    writer = pd.ExcelWriter(done_folder + xlsx_file, engine=engine)
    read_lokale = pd.read_csv(folder_tmp + lokale_csv_file, sep=';', encoding='utf-8')
    read_grunty = pd.read_csv(folder_tmp + grunty_csv_file, sep=';', encoding='utf-8')
    read_budynki = pd.read_csv(folder_tmp + budynki_csv_file, sep=';', encoding='utf-8')
    read_pdf = pd.DataFrame()
    read_lokale.to_excel(writer, sheet_name="Lokale", index=False)
    read_grunty.to_excel(writer, sheet_name="Działki", index=False)
    read_budynki.to_excel(writer, sheet_name="Domy", index=False)
    workbook = writer.book
    number_format = workbook.add_format({'num_format': '#,##0.00'})
    worksheet_lokale = writer.sheets["Lokale"]
    worksheet_grunty = writer.sheets["Działki"]
    worksheet_budynki = writer.sheets["Domy"]
    worksheet_lokale.set_column('W:W', None, number_format)
    worksheet_lokale.set_column('X:X', None, number_format)
    worksheet_lokale.set_column('T:T', None, number_format)
    worksheet_lokale.set_column('S:S', None, number_format)
    worksheet_grunty.set_column('P:P', None, number_format)
    worksheet_grunty.set_column('Q:Q', None, number_format)
    worksheet_budynki.set_column('S:S', None, number_format)
    worksheet_budynki.set_column('T:T', None, number_format)
    worksheet_budynki.set_column('W:W', None, number_format)
    worksheet_budynki.set_column('X:X', None, number_format)
    # format1 = workbook.add_format({'num_format': '#,##0.00'})
    # worksheet.set_column('M:M', 18, format1)

    writer.save()
    copyfile(done_folder + xlsx_file, backup_folder + xlsx_file)
    # print(workbook.get_sheet_names())
    # ws = workbook.Worksheets(4)
    # objs = ws.OLEObjects()
    # objs.Add(Filename=add_pdf, iconlabel = "Test").Name = 'Test'
    return (done_folder + xlsx_file)

# CSV2XLSX('wolny_rynek.xlsx', 1)
