import re

from budynki.variables_ak import p_pow_gr

CB = re.compile('.*Pow\\.\\s?:\\s?(.*)\\sha.*')


def powierzchnia_gruntu(line):
    try:
        if CB.search(line):
            res8 = CB.search(line)
            res8prim = res8.group(1)
            res8prim2 = re.sub(r'\.', '', res8prim)
            res8prim3 = re.sub(r'^[0]+', '', res8prim2)
            p_pow_gr.append(res8prim3)
        else:
            p_pow_gr.append('')
        return p_pow_gr
    except:
        return p_pow_gr
