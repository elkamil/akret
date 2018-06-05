
import re
from lokale.variables_ak import h_udzial

BD = re.compile('.*Udzia[lł]\\s?:\\s?(.*?)(?=Typ).*', re.DOTALL)
ulamek = re.compile('(.*)/(.*)', re.DOTALL)


def udzial(line):
    if BD.search(line):
        res5 = BD.search(line)
        res6 = re.sub(r'//','/',re.sub(r'l','/',re.sub(r'\n', '', res5.group(1))))
        print(res6)
        if ulamek.search(res6):
            ul = ulamek.search(res6)
            print("val1:"+ul.group(1)+" "+"val2:"+ul.group(2))
            licznik = int(ul.group(1))
            mianownik = int(ul.group(2))
            wynik = round((licznik/mianownik)*100,5)
            print(wynik)
        else:
            print("blad")
        h_udzial.append("- Udział: "+re.sub(r'(\||I)', '/', res6))
    else:
        h_udzial.append('-')
    return h_udzial
