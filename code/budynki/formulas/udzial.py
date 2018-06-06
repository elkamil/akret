
import re
from budynki.variables_ak import h_udzial, h1_udzial_procent

BD = re.compile('.*Udzia[lł]\\s?:\\s?(.*?)(?=Typ).*', re.DOTALL)
ulamek = re.compile('(.*)/(.*)', re.DOTALL)


def udzial(line):
    if BD.search(line):
        res5 = BD.search(line)
        res6 = re.sub(r'//','/',re.sub(r'l','/',re.sub(r'\n', '', res5.group(1))))
        if (len(re.findall('/', res6)) == 1):
            ul = ulamek.search(re.sub(r'\s','',res6))
            licznik = float(re.sub(r'\s', '', ul.group(1)))
            mianownik = float(re.sub(r'\s', '', ul.group(2)))
            wynik = round((licznik/mianownik)*100,5)
            h1_udzial_procent.append(wynik)
        else:
            h1_udzial_procent.append('')
        h_udzial.append("- Udział: "+re.sub(r'(\||I)', '/', res6))
    else:
        h_udzial.append('-')
        h1_udzial_procent.append('')
    return h_udzial,h1_udzial_procent
