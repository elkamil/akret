import re
from budynki.variables_ak import z_rep_a, aa_nr_zmiany

AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]{0,4})-?\\s?(\\d+/\\d+)[-/](.*?)(?=,)')
re_wpis = re.compile('.*Nrdok\.:(.*?)(?=,KW).*')
re_nawias = re.compile('\)')
re_nawias_koniec = re.compile('\)$')
re_nawias_koniec_group = re.compile('([a-zA-Z]{0,4})-?(\\d+/\\d+)[-/](.*)')
re_nawias_begin_group = re.compile('([a-zA-Z]{0,4})-?(.*?)(?=\))\)[/-]?(.*)')
re_beznawiasu = re.compile('([a-zA-Z]{0,4})-?(\\d+/\\d+)[-/](.*)')


def nr_dok(line):
    nospace = re.sub(r'\s', '', line)
    nospace1 = re.sub(r'—', '-', nospace)
    correct = re.sub(r'(\||I|l)', '/', nospace1)
    if re_wpis.search(correct):
        res9 = re_wpis.search(correct)
        if re_nawias.search(res9.group(1)):
            if re_nawias_koniec.search(res9.group(1)):
                wynik = re_nawias_koniec_group.search(res9.group(1))
                z_rep_a.append(wynik.group(2))
                aa_nr_zmiany.append(wynik.group(3))
            else:
                wynik = re_nawias_begin_group.search(res9.group(1))
                an = wynik.group(2) + ")"
                z_rep_a.append(an)
                aa_nr_zmiany.append(wynik.group(3))
        else:
            if re_beznawiasu.search(res9.group(1)):
                wynik = re_beznawiasu.search(res9.group(1))
                z_rep_a.append(wynik.group(2))
                aa_nr_zmiany.append(wynik.group(3))
            else:
                z_rep_a.append('')
                aa_nr_zmiany.append('')

    # if AH.search(correct):
       # res9 = AH.search(correct)
        # z_rep_a.append(res9.group(2))
        # aa_nr_zmiany.append(res9.group(3))
    else:
        z_rep_a.append('')
        aa_nr_zmiany.append('')
    return z_rep_a, aa_nr_zmiany
