import re
from budynki.variables_ak import ab_kw
AF = re.compile('.*KW\\s?:\\s?(.*?)(?=[uU]zbrojenie)', re.DOTALL)


def kw(line):
    if AF.search(line):
        res12 = AF.search(line)
        res12prim = res12.group(1)
        res12prim2 = re.sub(r',$', '', res12prim)
        ab_kw.append(re.sub(r'\n', '', res12prim2))
    else:
        ab_kw.append('')
    return ab_kw
