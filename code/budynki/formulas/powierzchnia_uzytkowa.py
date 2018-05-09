import re
from budynki.variables_ak import u_pow_uzytkowa

M = re.compile('.*Pow\\.\\s?użytk\\.\\s?:\\s?\\b(.*)(?=\\s?m\\s?kw\\.).*')


def powierzchnia_uzytkowa(line):
    if M.search(line):
        res5 = M.search(line)
        u_pow_uzytkowa.append(round(float(res5.group(1)), 2))
    else:
        u_pow_uzytkowa.append('')
    return u_pow_uzytkowa
