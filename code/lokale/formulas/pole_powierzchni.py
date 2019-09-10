import re

CB = re.compile('.*Pow\\.\\s?:\\s?(.*)\\sha.*')

def pole_powierzchni(line):
    cb_pole_powierzchni_gruntu = ['']
    try:
        if CB.search(line):
            res8 = CB.search(line)
            res8prim = res8.group(1)
            res8prim2 = re.sub(r'\.', '', res8prim)
            res8prim3 = re.sub(r'^[0]+', '', res8prim2)
            cb_pole_powierzchni_gruntu.append(res8prim3)
        else:
            cb_pole_powierzchni_gruntu.append('')
        return cb_pole_powierzchni_gruntu
    except:
        return cb_pole_powierzchni_gruntu
