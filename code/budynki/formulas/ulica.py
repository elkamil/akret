from budynki.variables_ak import c_ulica, d_nr
import re

re_ulica = re.compile('\\d+\\.\\s(.*?)(?=,),\\s?(.*?)(?=\\s?\\()')
re_numer_na_poczatku = re.compile('^\\d')
re_numer_na_poczatku_group = re.compile('(\\d+.*?)(?=\\d)(.*)')
re_bez_numeru = re.compile('\\d', re.DOTALL)
re_normalny = re.compile('(.*?)(?=\\s?\\d)(.*)')


def ulica(line):
    line = re.sub(r'\sG[Aa]\s', ' 6a ', re.sub(r'\sG[gG]\s', ' 6g ', re.sub(r'\sG[dD]\s', ' 6d ', re.sub(r'G[bB]', '6b', re.sub(r'%', '9b', line.splitlines()[0])))))
    if re_ulica.search(line) is not None:
        res4 = re_ulica.search(line)
        res_ulica = res4.group(2)
        if re_numer_na_poczatku.search(res_ulica) is not None:
            res5 = re_numer_na_poczatku_group.search(res_ulica)
            c_ulica.append(res5.group(1))
            d_nr.append(res5.group(2))
        elif re_bez_numeru.search(res_ulica) is None:
            c_ulica.append(res_ulica)
            d_nr.append('')
        else:
            res5 = re_normalny.search(res_ulica)
            c_ulica.append(res5.group(1))
            d_nr.append(res5.group(2))
    else:
        c_ulica.append('')
        d_nr.append('')
    return c_ulica, d_nr
