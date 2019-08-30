import re

from grunty.variables_ak import g_typ_wlasciciela

Y = re.compile('Typ\\s?właś.*\\s?:\\s?(osoba fizyczna|\\s?osoba\\s?fizyczna|\\s?osoba\\s?prawna|gmina|\\s?gmina\\s?|\
               \\s?Skarb\\s?Państwa|Skarb Państwa)', re.IGNORECASE)


def rodzaj_osoby(line):
    if Y.search(line):
        res = Y.search(line)
        g_typ_wlasciciela.append(res.group(1))
    else:
        g_typ_wlasciciela.append('-')
    return g_typ_wlasciciela
