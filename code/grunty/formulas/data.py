import re
from grunty.variables_ak import s_data

B = re.compile('.*określono\\s?[wW]\\s?dniu\\s?(.*)')


def data(line):
    if B.search(line):
        res2 = B.search(line)
        data = res2.group(1)
        data_without_spaces = re.sub(r'\s+', '', data)
        data_conv = re.compile('(\\d{2})\\.(\\d{2})\\.(\\d{4})')
        d_res = data_conv.search(data_without_spaces)
        d_res_final = d_res.group(3)+'-'+d_res.group(2)+'-'+d_res.group(1)
        s_data.append(d_res_final)
    else:
        s_data.append('-')
    return s_data
