from variables import obreby_plik
import re
import pandas as pd
from grunty.variables_ak import k_obreb, l_arkusz, m_dzialka, j_dzielnica


obreby_csv = pd.read_csv(obreby_plik, sep=';', encoding='utf-8')
H = re.compile('.*Obręb\\s?:\\s?(\\d{2})(\\d{2})\\s?-\\s?([^,]+),\\s?Ark\\.:\\s?\\b(.*)(?=\\s?,\\s?Nr\\s?dz\\.)\\s?,\\s?Nr\\s?dz\\.:\\s?(.*?)(?=\\s?(Funkcja|\\s?Funkcja)).*', re.DOTALL)


def lokalizacja(line):
    if H.search(line):
        res3 = H.search(line)
        obr = res3.group(1)+ res3.group(2)+" - "+res3.group(3)
        k_obreb.append(obr)
        m_dzialka = res3.group(5)
        l_arkusz.append(res3.group(4))
        G = obreby_csv[obreby_csv['Numer'] == int(res3.group(2))].Dzielnica
        G_val = G.values
        j_dzielnica.append(G_val)
    else:
        k_obreb.append('-')
        l_arkusz.append('-')
        j_dzielnica.append('-')
        m_dzialka = '-'
    return k_obreb, l_arkusz, j_dzielnica, m_dzialka
