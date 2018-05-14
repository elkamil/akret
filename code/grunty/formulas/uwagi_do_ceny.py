import re
from grunty.variables_ak import t_uwagi_do_ceny

re_uwagi_do_ceny = re.compile('.*Uwagi\\s?do\\s?ceny\\s?:\\s?(.*?)(?=\\s?Nr\\s?dok).*', re.S)


def uwagi_do_ceny(line):

    if re_uwagi_do_ceny.search(line):
        res11 = re_uwagi_do_ceny.search(line)
        t_uwagi_do_ceny.append(re.sub(r'2[Łł]', 'zł', re.sub(r'\n', '', res11.group(1))))
    else:
        t_uwagi_do_ceny.append('-')
    return t_uwagi_do_ceny
