import re
Z = re.compile('.*Opis\\s?dodatkowy\\s?:\\s?(.*?)(?=Zlecenie\\s?nr).*', re.DOTALL)
X = re.compile('.*Opis\\s?dodatkowy\\s?:\\s?(.*)', re.DOTALL)


def opis(line):
    if Z.search(line):
        res10 = Z.search(line)
        opis_dodatkowy = re.sub(r'2[Łł]', 'zł', re.sub(r'\n', ' ', res10.group(1)))
    else:
        if X.search(line):
            res10 = X.search(line)
            opis_dodatkowy = re.sub(r'2[Łł]', 'zł', re.sub(r'\n', ' ', res10.group(1)))
        else:
            opis_dodatkowy = '-'
    return opis_dodatkowy
