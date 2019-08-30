import re

from lokale.variables_ak import ab_kw, ag_kw_gruntowa, ah_kw_lokalu

AF = re.compile('.*KW\\s?:\\s?(.*?)(?=[uU]zbrojenie)', re.DOTALL)


def kw(line):
    if AF.search(line):
        res12 = AF.search(line)
        res12prim = res12.group(1)
        res12prim2 = re.sub(r',$', '', res12prim)
        correct = re.sub(r'\.', ',', re.sub(r'(\||I|l)', '/', res12prim2))
        ab_kw.append(re.sub(r'\n', '', correct))
    else:
        ab_kw.append('')
    return ab_kw


def kw_podzial(kw):
    kw_str = ''.join(kw)
    if kw_str == "":
        ag_kw_gruntowa.append('')
        ah_kw_lokalu.append('')
    else:
        if (len(re.findall('(,|;)', kw_str)) == 0):
            ag_kw_gruntowa.append(re.sub(r'\s', '', re.sub(r'l', '/', kw_str)))
            ah_kw_lokalu.append('')
        elif (len(re.findall(',|;', kw_str)) == 1):
            druga_ksiega_search = re.compile('(.*)(;|,)(.*)')
            druga_ksiega = druga_ksiega_search.search(kw_str)
            d_ksiega = re.sub(r'\s', '', druga_ksiega.group(3))
            rem_pipe = re.sub(r'l', '/', d_ksiega)
            ah_grunt = re.sub(r'\s', '', re.sub(r'l', '/', druga_ksiega.group(1)))
            ah_kw_lokalu.append(rem_pipe)
            ag_kw_gruntowa.append(ah_grunt)
        elif (len(re.findall(',|;', kw_str)) > 1):
            d_ksiega_trzecia_search = re.compile('(.*?)(,|;)(.*?)(,|;).*(;|,)?.*')
            d_ksiega_trz = d_ksiega_trzecia_search.search(kw_str)
            d_ksiega_trzecia = d_ksiega_trz.group(1)
            ah_lokal = re.sub(r'\s', '', d_ksiega_trz.group(2))
            ah_kw_lokalu.append(ah_lokal)
            ag_kw_gruntowa.append(re.sub(r'\s', '', d_ksiega_trzecia))
        else:
            ag_kw_gruntowa.append('')
            ah_kw_lokalu.append('')
    return ag_kw_gruntowa, ah_kw_lokalu
