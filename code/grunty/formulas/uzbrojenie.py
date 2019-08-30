import re

from grunty.variables_ak import x_uzbrojenie

UZ = re.compile('Uzbrojenie\\s?:\\s?(.*?)(?=Rodzaj).*')


def uzbrojenie(line):
    if UZ.search(line):
        uzb = UZ.search(line)
        x_uzbrojenie.append(uzb.group(1))
    else:
        x_uzbrojenie.append('-')
    return x_uzbrojenie
