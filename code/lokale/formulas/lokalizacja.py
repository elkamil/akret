import re

import pandas as pd

from lokale.variables_ak import k_obreb, l_arkusz, m_dzialka, n_liczba_izb, \
    j_dzielnica
from variables import obreby_plik

H = re.compile(
    '.*Obręb\\s?:\\s?(\\d{2})(\\d{2})\\s?-\\s?([^,]+),\\s?Ark\\.:\\s?\\b(.*)(?=\\s?,\\s?Nr\\s?dz\\.)\\s?,\\s?Nr\\s?dz\\.:\\s?(.*?)(?=\\s?Liczba\\s?izb)\\s?Liczba\\s?izb\\s?:\\s?(\\d{1})?\\s?(.*?)\\s?(?=(\\s?\\d+?Funkcja|\\s?Funkcja)).*',
    re.DOTALL)

obreby_csv = pd.read_csv(obreby_plik, sep=';', encoding='utf-8')


def lokalizacja(line):
    if H.search(line):
        res3 = H.search(line)
        obr = res3.group(1) + res3.group(2) + " - " + res3.group(3)
        k_obreb.append(obr)
        nr_dzialki = res3.group(5) + res3.group(7)

        l_arkusz.append(res3.group(4))
        m_dzialka.append(nr_dzialki)
        n_liczba_izb.append(res3.group(6))
        G = obreby_csv[obreby_csv['Numer'] == int(res3.group(2))].Dzielnica
        G_val = G.values
        j_dzielnica.append(G_val)
    else:
        k_obreb.append('')
        l_arkusz.append('')
        m_dzialka.append('')
        n_liczba_izb.append('')
        j_dzielnica.append('')
    return k_obreb, l_arkusz, m_dzialka, n_liczba_izb, j_dzielnica
