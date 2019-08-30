import re

from grunty.variables_ak import n_funkcja

# B = re.compile('.*określono\s?[wW]\s?dniu\s?(.*)')
B = re.compile('.*Funkcja\\s?:\\s?(.*?)(?=Pow).*', re.DOTALL)


def funkcja(line):
    if B.search(line):
        res2 = B.search(line)
        res3 = re.sub(r'^\s', '', re.sub(r'\s$', '', re.sub(r'I', '/', re.sub(r'\n', '', res2.group(1)))))
        n_funkcja.append(res3)
    else:
        n_funkcja.append('-')
    return n_funkcja
