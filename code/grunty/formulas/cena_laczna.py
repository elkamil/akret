import re

from grunty.variables_ak import q_cena_laczna

N = re.compile('.*Cena\\s?łączna\\snieruchomości\\s?:\\s?([^zł]+)(?=\\s?z?ł?\\s?okre[sś]lono).*')


def cena_laczna(line):
    if N.search(line):
        res6 = N.search(line)
        res6prim = res6.group(1)
        res6prim1 = re.sub(r'\s+', '', res6prim)
        q_cena_laczna.append(res6prim1)
    else:
        q_cena_laczna.append('-')

    # if q_cena_laczna[0]:
    #     q_cena_laczna_2f = ['%.2f' % elem for elem in [float(i) for i in q_cena_laczna]]
    # else:
    #     q_cena_laczna_2f = ['-']

    # return q_cena_laczna_2f
    return q_cena_laczna
