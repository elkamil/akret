__author__ = "Kamil Markowiak"
__copyright__ = "Copyright 2018, 4imp Kamil Markowiak"
__license__ = "GPL"
__email__ = "kamil.markowiak@protonmail.com"

from wand.image import Image as WImage
from PIL import Image as PI
import pyocr
import pyocr.builders
# from PIL import ImageEnhance, ImageFilter
# from PIL import Image as Img
from variables import folder_tmp, TMP_JPEG_FILE
from tqdm import tqdm


def ThreadOCR(filename, ilosc_stron, i, file_no):
    index = 0
    i = i
    ilosc_pbar = ilosc_stron
    Input_file = folder_tmp+"split_csv1/"+str(file_no)+".txt"
    open(Input_file, 'w').close()
    # Input_PDF_FILE = filename
    Input_PDF_FILE = folder_tmp + "split_pdf1/" + filename
    print("Tutaj"+Input_PDF_FILE)
    image_file = open(folder_tmp+TMP_JPEG_FILE+str(i), "wb")
    tool = pyocr.get_available_tools()[0]
#    langs = tool.get_available_languages()
    lang_pol = 'pol'
    pbar = tqdm(total=ilosc_pbar, desc="Opis"+str(i), position=i)
    while index < ilosc_stron:
        with WImage(filename=Input_PDF_FILE + "[{}]".format(index), resolution=300) as img:
            test_file = open(Input_file, 'a')
            image_bmp = img.convert('bmp')
            image_bmp.save(filename=image_file.name)
            image_file.close()
            final_text = []
            builder = pyocr.builders.TextBuilder()
            builder.tesseract_flags = ['-psm', '1']
            text = tool.image_to_string(PI.open(folder_tmp+TMP_JPEG_FILE+str(i)), lang=lang_pol, builder=builder)
            final_text.append(text)
            test_file.write(''.join(final_text))
            test_file.write('\n')
            index += 1
            test_file.close()
        pbar.update(1)
    pbar.close()
