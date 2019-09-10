import re

from grunty.variables_ak import y_przeznaczenie_terenu

BZ = re.compile('Przez.*terenu\\s?:\\s?(.*?)(?=Opis)', re.DOTALL)


def przeznaczenie_terenu(line):
    try:
        if BZ.search(line):
            bz = BZ.search(line)
            y_przeznaczenie_terenu.append(re.sub(r'\n', '', bz.group(1)))
        else:
            y_przeznaczenie_terenu.append('')
        return y_przeznaczenie_terenu
    except:
        return y_przeznaczenie_terenu
