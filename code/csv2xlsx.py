__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from variables import folder_tmp, csv_file, lokale_csv_file, grunty_csv_file, budynki_csv_file, static_folder
from shutil import copyfile
# from choose_method import choose_method
from csv_record_separator import NumeryLiniiDoPodzialu
import pandas as pd

# lokale mieszkalne


def CSV2XLSX(filename, wybor):
    numery_linii_do_podzialu = NumeryLiniiDoPodzialu()
    # choose = choose_method(wybor)
    done_folder = static_folder + "lokale_mieszkalne/"
    backup_folder = static_folder + "backup/lokale_mieszkalne/"

    xlsx_file = filename+".xlsx"
    engine = 'xlsxwriter'
    print("..Konwersja CSV na Excel...")
    writer = pd.ExcelWriter(done_folder+xlsx_file, engine=engine)
    read_lokale = pd.read_csv(folder_tmp+lokale_csv_file, sep=';', encoding='utf-8')
    read_grunty = pd.read_csv(folder_tmp+grunty_csv_file, sep=';', encoding='utf-8')
    read_budynki = pd.read_csv(folder_tmp+budynki_csv_file, sep=';', encoding='utf-8')
    read_lokale.to_excel(writer, sheet_name="Lokale", index=False)
    read_grunty.to_excel(writer, sheet_name="Działki", index=False)
    read_budynki.to_excel(writer, sheet_name="Domy", index=False)
    workbook = writer.book
    worksheet = writer.sheets["Lokale"]
    worksheet = writer.sheets["Działki"]
    worksheet = writer.sheets["Domy"]
    # format1 = workbook.add_format({'num_format': '#,##0.00'})
    # worksheet.set_column('M:M', 18, format1)

    writer.save()
    copyfile(done_folder+xlsx_file, backup_folder+xlsx_file)
    return(done_folder+xlsx_file)

CSV2XLSX('wolny_rynek.xlsx', 1)
