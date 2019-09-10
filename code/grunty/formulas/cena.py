import re

from grunty.variables_ak import o_cena, p_cena_1mkw

G = re.compile('(?<=Cena:)\\s?(.*)\\s?z\\s?[lł]\\s?')
B = re.compile('.*Cena\\s?1(.*):\\s?(.*?)(?=Cena\\s?ł).*', re.DOTALL)
number = re.compile('\d')


def cena(line):
    try:
        if G.search(line):
            res6 = G.search(line)
            result = re.sub(r'[^\d\.]', '', res6.group(1))
            if number.search(result):
                o_cena.append(result)
            else:
                o_cena.append('')
        else:
            o_cena.append('')

        return o_cena
    except:
        return o_cena


def cena_1mkw(line):
    try:
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
    except:
        return p_cena_1mkw
