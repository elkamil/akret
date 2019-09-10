import re

from budynki.variables_ak import ac_uzbrojenie

UZ = re.compile('Uzbrojenie\\s?:\\s?(.*?)(?=Rodzaj).*')


def uzbrojenie(line):
    try:
        if UZ.search(line):
            uzb = UZ.search(line)
            ac_uzbrojenie.append(uzb.group(1))
        else:
            ac_uzbrojenie.append('-')
        return ac_uzbrojenie
    except:
        return ac_uzbrojenie
