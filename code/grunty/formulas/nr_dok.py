import re

from grunty.variables_ak import u_rep_a, v_nr_zmiany

AH = re.compile('.*Nr\\s?dok\\.\\s?:\\s?([a-zA-Z]{0,4})-?\\s?(\\d+/\\d+)[-/](.*?)(?=,)')
re_wpis = re.compile('.*Nrdok\.:(.*?)(?=,KW).*')
re_nawias = re.compile('\)')
re_nawias_koniec = re.compile('\)$')
re_nawias_koniec_group = re.compile('([a-zA-Z]{0,4})-?(\\d+/\\d+)[-/](.*)')
re_nawias_begin_group = re.compile('([a-zA-Z]{0,4})-?(.*?)(?=\))\)[/-]?(.*)')
re_beznawiasu = re.compile('([a-zA-Z]{0,4})-?(\\d+[-/]\\d+)[-/](.*)')
re_beznawiasu_p1 = re.compile('([a-zA-Z]{0,4})-?(\\d+[-/]\\d+)(.*)')


def nr_dok(line):
    try:
        nospace = re.sub(r'\s', '', line)
        nospace1 = re.sub(r'—', '-', nospace)
        correct = re.sub(r'(\||I|l)', '/', nospace1)
        if re_wpis.search(correct):
            res9 = re_wpis.search(correct)
            if re_nawias.search(res9.group(1)):
                if re_nawias_koniec.search(res9.group(1)):
                    wynik = re_nawias_koniec_group.search(res9.group(1))
                    u_rep_a.append(wynik.group(2))
                    v_nr_zmiany.append(wynik.group(3))
                else:
                    wynik = re_nawias_begin_group.search(res9.group(1))
                    an = wynik.group(2) + ")"
                    u_rep_a.append(an)
                    v_nr_zmiany.append(wynik.group(3))
            else:
                if re_beznawiasu.search(res9.group(1)):
                    wynik = re_beznawiasu.search(res9.group(1))
                    u_rep_a.append(wynik.group(2))
                    v_nr_zmiany.append(wynik.group(3))
                elif re_beznawiasu_p1.search(res9.group(1)):
                    wynik = re_beznawiasu_p1.search(res9.group(1))
                    u_rep_a.append(wynik.group(2))
                    v_nr_zmiany.append('')
                else:
                    u_rep_a.append('')
                    v_nr_zmiany.append('')

        else:
            u_rep_a.append('')
            v_nr_zmiany.append('')
        return u_rep_a, v_nr_zmiany
    except:
        return u_rep_a, v_nr_zmiany
