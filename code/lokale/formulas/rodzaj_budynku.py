import re
from lokale_mieszkalne.variables import v_rodzaj_budynku

V = re.compile('Rodzaj\\s?bud\\.\\s?:\\s?(jednorodzinne|wielorodzinne|wieIorodzinne)')


def rodzaj_budynku(line):
    if V.search(line):
        res7 = V.search(line)
        v_rodzaj_budynku.append(res7.group(1))
    else:
        v_rodzaj_budynku.append('')
    return v_rodzaj_budynku
