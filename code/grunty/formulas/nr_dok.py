import re
from grunty.variables_ak import u_rep_a, v_nr_zmiany

AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]+)-?\\s?(\\d+/\\d+)-(.*?)(?=,)')


def nr_dok(line):
    nospace = re.sub(r'\s', '', line)
    nospace1 = re.sub(r'—', '-', nospace)
    correct = re.sub(r'(\||I|l)', '/', nospace1)
    if AH.search(correct):
        res9 = AH.search(correct)
        u_rep_a.append(res9.group(2))
        v_nr_zmiany.append(res9.group(3))
    else:
        u_rep_a.append('-')
        v_nr_zmiany.append('-')
    return u_rep_a, v_nr_zmiany
