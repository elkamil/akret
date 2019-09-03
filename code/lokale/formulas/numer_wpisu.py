import re
re_numer_wpisu = re.compile('(\\d+)\\..*')


def numer_wpisu(line):
    line = re.sub(r'\s+', '', line.splitlines()[0])
    numer_wpisu = []
    if re_numer_wpisu.search(line):
        res9 = re_numer_wpisu.search(line)
        numer_wpisu.append(res9.group(1))
    else:
        numer_wpisu.append('')
    return numer_wpisu
