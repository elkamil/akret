import re

from grunty.variables_ak import z_rodzaj_bud

# V = re.compile('Rodzaj\\s?bud\\.\\s?:\\s?(jednorodzinne|wielorodzinne|wieIorodzinne)')
V = re.compile('Rodzaj\\s?bud\\.\\s?:(.*)', re.MULTILINE)


def typ_budynku(line):
    if V.search(line):
        res7 = V.search(line)
        z_rodzaj_bud.append(res7.group(1))
    else:
        z_rodzaj_bud.append('-')
    return z_rodzaj_bud
