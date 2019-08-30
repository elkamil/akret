import re

from lokale.variables_ak import r_cena, v_cena, w_cena_1mkw, s_cena_1mkw

# B = re.compile('.*określono\s?[wW]\s?dniu\s?(.*)')
B = re.compile('.*Cena\\s?:\\s?(.*?)(?=Cena\\s?1).*', re.DOTALL)
C = re.compile('(?<=Cena:)\\s?(.*)\\s?Cena\\s?:', re.DOTALL)

B1 = re.compile('.*Cena\\s?1\\s?.*:(.*?)(?=Cena\\s?[^:]).*', re.DOTALL)
C1 = re.compile('(?<=Cena\\s1)(.*):(.*)\\s?Cena\\s?1', re.DOTALL)
number = re.compile('\d')


def vv_cena(line):
    if B.search(line):
        res2 = B.search(line)
        # v_cena.append(res2.group(1))
        result = re.sub(r'[^\d\.]', '', res2.group(1))
        if number.search(result):
            v_cena.append(result)
        else:
            v_cena.append('')
    else:
        v_cena.append('')
    return v_cena


def rr_cena(line):
    if C.search(line):
        res2 = C.search(line)
        # r_cena.append(res2.group(1))
        result = re.sub(r'[^\d\.]', '', res2.group(1))
        if number.search(result):
            r_cena.append(result)
        else:
            r_cena.append('')
    else:
        r_cena.append('')
    return r_cena


def ww_cena_1mkw(line):
    if B1.search(line):
        res2 = B1.search(line)
        result = re.sub(r'[^\d\.]', '', res2.group(1))
        if number.search(result):
            w_cena_1mkw.append(result)
        else:
            w_cena_1mkw.append('')
        # print(re.sub(r'[^\d\.]', '', res2.group(1)))
    else:
        w_cena_1mkw.append('')
    return w_cena_1mkw


def ss_cena_1mkw(line):
    if C1.search(line):
        res2 = C1.search(line)
        result = re.sub(r'[^\d\.]', '', res2.group(2))
        if number.search(result):
            s_cena_1mkw.append(result)
        else:
            s_cena_1mkw.append('')
        # s_cena_1mkw.append(re.sub(r'.', ',', re.sub(r'\n', '', res2.group(2))))
    else:
        s_cena_1mkw.append('')
    return s_cena_1mkw
