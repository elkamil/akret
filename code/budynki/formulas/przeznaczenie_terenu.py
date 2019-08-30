import re

from budynki.variables_ak import ad_przeznaczenie_terenu

BZ = re.compile('Przez.*terenu\\s?:\\s?(.*?)(?=Opis)', re.DOTALL)


def przeznaczenie_terenu(line):
    if BZ.search(line):
        bz = BZ.search(line)
        ad_przeznaczenie_terenu.append(bz.group(1))
    else:
        ad_przeznaczenie_terenu.append('')
    return ad_przeznaczenie_terenu
