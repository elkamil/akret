import re
from lokale.variables_ak import ad_rodzaj_budynku

V = re.compile('Rodzaj\\s?bud\\.\\s?:\\s?(.*?)(?=Przeznaczenie\\s?tere).*', re.DOTALL)


def rodzaj_budynku(line):
    if V.search(line):
        res7 = V.search(line)
        ad_rodzaj_budynku.append(re.sub(r'\n', '', res7.group(1)))
    else:
        ad_rodzaj_budynku.append('')
    return ad_rodzaj_budynku
