
import re
from budynki.variables_ak import h_udzial

BD = re.compile('.*Udzia[lł]\\s?:\\s?(.*?)(?=Typ).*', re.DOTALL)


def udzial(line):
    if BD.search(line):
        res5 = BD.search(line)
        res6 = re.sub(r'\n', '', res5.group(1))                            
        h_udzial.append("- Udział: "+re.sub(r'(\||I)', '/', res6))
    else:
        h_udzial.append('-')
    return h_udzial
