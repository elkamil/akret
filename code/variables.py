__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"
import os

# Input_PDF_FILE = sys.argv[1]
print(os.getcwd())
home = os.getcwd()
Input_file = "result.txt"
folder = home + "\workdir\\"
logs_dir = folder+"logs\\"
static_dir = home + "\static"
backup_folder = static_dir + "\\backup\lokale_mieszkalne\\"
code_folder = ""
done_folder = static_dir+"\lokale_mieszkalne\\"
folder_tmp = home + "\\tmp\\"
pdf_folder = folder + "pdf\\"
split_pdf_1 = "split1.pdf"
split_pdf_2 = "split2.pdf"
split_pdf_3 = "split3.pdf"
result_no_page_numbers = "res_no_page.txt"
result_no_blank_lines = "res.txt"
# result_no_blank_lines = "result_no_blank_lines.txt"
csv_file = "my_excel.csv"
grunty_csv_file = "grunty.csv"
budynki_csv_file = "budynki.csv"
lokale_csv_file = "lokale.csv"
xlsx_file = "my_excel.xlsx"
wpisy = "Wpisy.txt"
line_numbers = "Line_Numbers.txt"
#files = [split_pdf_1, split_pdf_2, split_pdf_3, result_no_blank_lines, csv_file,
#         wpisy, line_numbers, tmp_bmp1_file, tmp_bmp2_file, tmp_bmp3_file]
files = [split_pdf_1, split_pdf_2, split_pdf_3, result_no_blank_lines, csv_file, wpisy, line_numbers ]
obreby_plik = home + "\data\obreby.csv"

xlsx_folder = static_dir + "\lokale_mieszkalne"

# email variables
email_to = 'kamil.markowiak@gmail.com'
email_from = 'emmerson_eval@o2.pl'
email_from_pass = '14rAnx6QnWlgjNGZUs7iyfAhwQ8Hj3Xt23h1y'
