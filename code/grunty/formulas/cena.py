import re

from grunty.variables_ak import o_cena, p_cena_1mkw

G = re.compile('(?<=Cena:)\\s?(.*)\\s?z\\s?[lł]\\s?')
B = re.compile('.*Cena\\s?1(.*):\\s?(.*?)(?=Cena\\s?ł).*', re.DOTALL)
number = re.compile('\d')


def cena(line):
    if G.search(line):
        res6 = G.search(line)
        result = re.sub(r'[^\d\.]', '', res6.group(1))
        if number.search(result):
            o_cena.append(result)
        else:
            o_cena.append('')
    else:
        o_cena.append('')

    # if o_cena[0]:
    #    o_cena_2f = ['%.2f' % elem for elem in [float(i) for i in o_cena]]
    # else:
    #    o_cena_2f = ['']

    # return o_cena_2f
    return o_cena


def cena_1mkw(line):
    if B.search(line):
        res6 = B.search(line)
        result = re.sub(r'[^\d\.]', '', res6.group(2))
        if number.search(result):
            p_cena_1mkw.append(result)
        else:
            p_cena_1mkw.append('')
    else:
        p_cena_1mkw.append('')
    return p_cena_1mkw
