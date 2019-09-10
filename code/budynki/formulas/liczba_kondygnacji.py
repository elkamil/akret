import re

from budynki.variables_ak import n_liczba_kondygnacji

AK = re.compile('.*Liczba\\s?kondygn\\.\\s?:\\s?(\\d+)')


def liczba_kondygnacji(line):
    try:
        if AK.search(line):
            res5 = AK.search(line)
            n_liczba_kondygnacji.append(res5.group(1))
        else:
            n_liczba_kondygnacji.append('')
        return n_liczba_kondygnacji
    except:
        return n_liczba_kondygnacji
