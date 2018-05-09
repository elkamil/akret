import re
from lokale.variables_ak import e_tryb_sprzedazy

# AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]+)-?\\s?(\\d+/\\d+).*')
re_tryb = re.compile('\\d+\\s?\\.\\s?Wroc.*\\((.*)\\)')


def tryb_sprzedazy(line):
    # nospace = re.sub(r'\\s+', '', line)
    if re_tryb.search(line):
        res9 = re_tryb.search(line)
        e_tryb_sprzedazy.append(res9.group(1))
    else:
        e_tryb_sprzedazy.append('')
    return e_tryb_sprzedazy
