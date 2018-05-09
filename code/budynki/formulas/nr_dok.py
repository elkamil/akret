import re
from budynki.variables_ak import z_rep_a, aa_nr_zmiany

AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]+)-?\\s?(\\d+/\\d+)-(.*?)(?=,)')


def nr_dok(line):
    nospace = re.sub(r'\s', '', line)
    correct = re.sub(r'(\||I|l)', '/', nospace)
    if AH.search(correct):
        res9 = AH.search(correct)
        z_rep_a.append(res9.group(2))
        aa_nr_zmiany.append(res9.group(3))
    else:
        z_rep_a.append('')
        aa_nr_zmiany.append('')
    return z_rep_a, aa_nr_zmiany
