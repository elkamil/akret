from grunty.variables_ak import r_pow
import re

CB = re.compile('.*Pow\\.\\s?:\\s?(.*)\\sha.*')


def powierzchnia_gruntu(line):
    if CB.search(line):
        res8 = CB.search(line)
        res8prim = res8.group(1)
        res8prim2 = re.sub(r'\.', '', res8prim)
        res8prim3 = re.sub(r'^[0]+', '', res8prim2)
        r_pow.append(res8prim3)
    else:
        r_pow.append('-')
    return r_pow
