import re
from budynki.variables_ak import b_nr

# AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]+)-?\\s?(\\d+/\\d+).*')
re_numer_wpisu = re.compile('(\\d+)\\..*')


def numer_wpisu(line):
    # nospace = re.sub(r'\\s+', '', line)
    line = re.sub(r'\s+', '', line.splitlines()[0])
    if re_numer_wpisu.search(line):
        res9 = re_numer_wpisu.search(line)
        b_nr.append(res9.group(1))
    else:
        b_nr.append('')
    return b_nr
