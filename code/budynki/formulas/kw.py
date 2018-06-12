import re
from budynki.variables_ak import ab_kw, ab_kw_gruntu, ab_kw_budynku
AF = re.compile('.*KW\\s?:\\s?(.*?)(?=[uU]zbrojenie)', re.DOTALL)


def kw(line):
    if AF.search(line):
        res12 = AF.search(line)
        res12prim = res12.group(1)
        res12prim2 = re.sub(r',$', '', res12prim)
        res12prim3 = re.sub(r'\n', '', res12prim2)
        correct = re.sub(r'(\||I|l)', '/', res12prim3)
        ab_kw.append(correct)
    else:
        ab_kw.append('')
    return ab_kw


def kw_podzial(kw):
    kw_str=''.join(kw)
    if kw_str == "":
        ab_kw_gruntu.append('')
        ab_kw_budynku.append('')
    else:
        if (len(re.findall('(,|;)', kw_str)) == 0):
            ab_kw_gruntu.append(re.sub(r'\s', '', re.sub(r'l', '/', kw_str)))
            ab_kw_budynku.append('')
        elif (len(re.findall(',|;', kw_str)) == 1):
            druga_ksiega_search = re.compile('(.*)(;|,)(.*)')
            druga_ksiega = druga_ksiega_search.search(kw_str)
            d_ksiega = re.sub(r'\s', '', druga_ksiega.group(3))
            rem_pipe = re.sub(r'l', '/', d_ksiega)
            ah_lokal = re.sub(r'\s', '', re.sub(r'l', '/', druga_ksiega.group(1)))
            ab_kw_budynku.append(rem_pipe)
            ab_kw_gruntu.append(ah_lokal)
        elif (len(re.findall(',|;', kw_str)) > 1):
            d_ksiega_trzecia_search = re.compile('(.*?)(,|;)(.*?)(,|;).*(;|,)?.*')
            d_ksiega_trz = d_ksiega_trzecia_search.search(kw_str)
            d_ksiega_trzecia = d_ksiega_trz.group(1)
            ah_lokal = re.sub(r'\s', '', d_ksiega_trz.group(2))
            ab_kw_budynku.append(ah_lokal)
            ab_kw_gruntu.append(re.sub(r'\s', '', d_ksiega_trzecia))
        else:
            ab_kw_gruntu.append('')
            ab_kw_budynku.append('')
    return ab_kw_gruntu, ab_kw_budynku
