import re
from lokale.variables_ak import o_funkcja, q_funkcja

# B = re.compile('.*określono\s?[wW]\s?dniu\s?(.*)')
B = re.compile('.*Funkcja\\s?:\\s?(.*?)(?=Pow).*', re.DOTALL)
C = re.compile('(?<=Funkcja:)\\s?(.*)\\s?Funkcja', re.DOTALL)


def qq_funkcja(line):
    if B.search(line):
        res2 = B.search(line)
        q_funkcja.append(res2.group(1))
    else:
        q_funkcja.append('-')
    return q_funkcja


def oo_funkcja(line):
    if C.search(line):
        res2 = C.search(line)
        o_funkcja.append(res2.group(1))
    else:
        o_funkcja.append('-')
    return o_funkcja
