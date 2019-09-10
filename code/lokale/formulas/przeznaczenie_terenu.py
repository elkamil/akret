import re

from lokale.variables_ak import ae_przeznaczenie_terenu

BZ = re.compile('Przez.*terenu\\s?:\\s?(.*?)(?=Opis)', re.DOTALL)


def przeznaczenie_terenu(line):
    try:
        if BZ.search(line):
            bz = BZ.search(line)
            ae_przeznaczenie_terenu.append(re.sub(r'\n', '', bz.group(1)))
        else:
            ae_przeznaczenie_terenu.append('')
        return ae_przeznaczenie_terenu
    except:
        return ae_przeznaczenie_terenu
