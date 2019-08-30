import re

from budynki.variables import z_typ_budynku

V = re.compile('Rodzaj\\s?bud\\.\\s?:\\s?(jednorodzinne|wielorodzinne|wieIorodzinne)')


def typ_budynku(line):
    if V.search(line):
        res7 = V.search(line)
        if res7.group(1) == 'jednorodzinne':
            typ = ['jednorodzinny']
            z_typ_budynku.append(typ)
        else:
            z_typ_budynku.append(res7.group(1))
    else:
        z_typ_budynku.append('')
    return z_typ_budynku
