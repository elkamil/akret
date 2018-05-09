import re
from budynki.variables_ak import r_cena, v_cena, w_cena_1mkw, s_cena_1mkw

# B = re.compile('.*określono\s?[wW]\s?dniu\s?(.*)')
B = re.compile('.*Cena\\s?:\\s?(.*?)(?=Cena\\s?1).*', re.DOTALL)
C = re.compile('(?<=Cena:)\\s?(.*)\\s?Cena\\s?:', re.DOTALL)

B1 = re.compile('.*Cena\\s?1\\s?.*:(.*?)(?=Cena\\s?[^:]).*', re.DOTALL)
C1 = re.compile('(?<=Cena\\s1)(.*):(.*)\\s?Cena\\s?1', re.DOTALL)


def vv_cena(line):
    if B.search(line):
        res2 = B.search(line)
        v_cena.append(res2.group(1))
    else:
        v_cena.append('-')
    return v_cena


def rr_cena(line):
    if C.search(line):
        res2 = C.search(line)
        r_cena.append(res2.group(1))
    else:
        r_cena.append('-')
    return r_cena


def ww_cena_1mkw(line):
    if B1.search(line):
        res2 = B1.search(line)
        w_cena_1mkw.append(res2.group(1))
    else:
        w_cena_1mkw.append('-')
    return w_cena_1mkw


def ss_cena_1mkw(line):
    if C1.search(line):
        res2 = C1.search(line)
        s_cena_1mkw.append(res2.group(2))
    else:
        s_cena_1mkw.append('-')
    return s_cena_1mkw
