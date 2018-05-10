import re
from lokale.variables_ak import y_uwagi_do_ceny

re_uwagi_do_ceny = re.compile('.*Uwagi\\s?do\\s?ceny\\s?:\\s?(.*?)(?=\\s?Nr\\s?dok).*', re.S)


def uwagi_do_ceny(line):

    if re_uwagi_do_ceny.search(line):
        res11 = re_uwagi_do_ceny.search(line)
        y_uwagi_do_ceny.append(re.sub(r'\n', '', res11.group(1)))
    else:
        y_uwagi_do_ceny.append('-')
    return y_uwagi_do_ceny
