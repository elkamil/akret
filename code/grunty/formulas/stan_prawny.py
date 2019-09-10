import re

from grunty.variables_ak import f_sprzedal

# X = re.compile('Sprzedał\\s?:\\s?(.*?)(?=Kupi).*', re.DOTALL)
X = re.compile('Sprzedał\\s?:(.*)', re.MULTILINE)


def stan_prawny(line):
    try:
        if X.search(line):
            res1 = X.search(line)
            res2 = re.sub(r'I', 'l', re.sub(r'\n', '', res1.group(1)))
            f_sprzedal.append(res2)
        else:
            f_sprzedal.append('-')
        return f_sprzedal
    except:
        return f_sprzedal
