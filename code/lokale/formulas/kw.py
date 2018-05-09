import re
from lokale.variables_ak import ab_kw
AF = re.compile('.*KW\\s?:\\s?(.*?)(?=[uU]zbrojenie)', re.DOTALL)


def kw(line):
    if AF.search(line):
        res12 = AF.search(line)
        res12prim = res12.group(1)
        res12prim2 = re.sub(r',$', '', res12prim)
        correct = re.sub(r'(\||I|l)', '/', res12prim2)
        ab_kw.append(correct)
    else:
        ab_kw.append('')
    return ab_kw
