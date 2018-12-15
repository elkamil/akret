import re
from lokale.variables_ak import u_powierzchnia_uzytkowa

M = re.compile('.*Pow\\.\\s?użytk\\.\\s?:\\s?\\b(.*)(?=\\s?m\\s?kw\\.).*')


def powierzchnia_uzytkowa(line):

    if M.search(line):
        res6 = M.search(line)
        res6prim = res6.group(1)
        u_powierzchnia_uzytkowa.append(res6prim)
    else:
        u_powierzchnia_uzytkowa.append('')

    if u_powierzchnia_uzytkowa[0]:
        u_powierzchnia_uzytkowa[:] = [s.replace(' ', '') for s in u_powierzchnia_uzytkowa]
        print(u_powierzchnia_uzytkowa)
        u_powierzchnia_uzytkowa_2f = ['%.2f' % elem for elem in [float(i) for i in u_powierzchnia_uzytkowa]]
    else:
        u_powierzchnia_uzytkowa_2f = ['']

    return u_powierzchnia_uzytkowa_2f
