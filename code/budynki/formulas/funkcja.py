import re

from budynki.variables_ak import o_funkcja_gruntu, q_funkcja_bud

# B = re.compile('.*określono\s?[wW]\s?dniu\s?(.*)')
B = re.compile('.*Funkcja\\s?:\\s?(.*?)(?=Pow).*', re.DOTALL)
C = re.compile('(?<=Funkcja)\\s?:(.*)\\s?Funkcja', re.DOTALL)


def qq_funkcja(line):
    if B.search(line):
        res2 = B.search(line)
        q_funkcja_bud.append(
            re.sub(r'^\s', '', re.sub(r'\s$', '', re.sub(r'I', '/', re.sub(r'\n', '', res2.group(1))))))
    else:
        q_funkcja_bud.append('-')
    return q_funkcja_bud


def oo_funkcja(line):
    if C.search(line):
        res2 = C.search(line)
        o_funkcja_gruntu.append(re.sub(r'^\s', '', re.sub(r',\s$', '', re.sub(r'I', '/', res2.group(1)))))
    else:
        o_funkcja_gruntu.append('-')
    return o_funkcja_gruntu
