from budynki.variables_ak import f_sprzedal
import re

X = re.compile('Sprzedał\\s?:\\s?(.*?)(?=Kupi).*', re.DOTALL)


def stan_prawny(line):
    if X.search(line):
        res1 = X.search(line)
        res2 = re.sub(r'\n', '', res1.group(1))
        f_sprzedal.append(res2)
    else:
        f_sprzedal.append('-')
    return f_sprzedal
