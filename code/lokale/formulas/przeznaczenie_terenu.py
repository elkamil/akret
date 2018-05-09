import re
from lokale.variables_ak import ae_przeznaczenie_terenu

BZ = re.compile('Przez.*terenu\\s?:\\s?(.*?)(?=Opis)', re.DOTALL)


def przeznaczenie_terenu(line):
    if BZ.search(line):
        bz = BZ.search(line)
        ae_przeznaczenie_terenu.append(bz.group(1))
    else:
        ae_przeznaczenie_terenu.append('')
    return ae_przeznaczenie_terenu
