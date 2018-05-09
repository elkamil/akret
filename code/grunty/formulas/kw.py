import re
from grunty.variables_ak import w_kw
AF = re.compile('.*KW\\s?:\\s?(.*?)(?=[uU]zbrojenie)', re.DOTALL)


def kw(line):
    if AF.search(line):
        res12 = AF.search(line)
        res12prim = res12.group(1)
        res12prim2 = re.sub(r',$', '', res12prim)
        res12prim3 = re.sub(r'\n', '', res12prim2)
        w_kw.append(res12prim3)
    else:
        w_kw.append('')
    return w_kw
