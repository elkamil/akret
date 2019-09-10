import re

from budynki.variables_ak import ae_rodzaj_budynku

# V = re.compile('Rodzaj\\s?bud\\.\\s?:\\s?(jednorodzinne|wielorodzinne|wieIorodzinne)')
V = re.compile('Rodzaj\\s?bud\\.\\s?:(.*)', re.MULTILINE)


def rodzaj_budynku(line):
    try:
        if V.search(line):
            res7 = V.search(line)
            ae_rodzaj_budynku.append(res7.group(1))
        else:
            ae_rodzaj_budynku.append('')
        return ae_rodzaj_budynku
    except:
        return ae_rodzaj_budynku
