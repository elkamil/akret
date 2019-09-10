import re
B = re.compile('.*określono\\s?[wW]\\s?dniu\\s?(.*)')


def b_data(line):
    b_data_transakcji = ['']
    try:
        if B.search(line):
            res2 = B.search(line)
            data = res2.group(1)
            data_without_spaces = re.sub(r'\s', '', data)
            data_conv = re.compile('(\\d{2})\\.(\\d{2})\\.(\\d{4})')
            d_res = data_conv.search(data_without_spaces)
            d_res_final = d_res.group(3) + '-' + d_res.group(2) + '-' + d_res.group(1)
            b_data_transakcji.append(d_res_final)
        else:
            b_data_transakcji.append('')
        return b_data_transakcji
    except:
        return b_data_transakcji.append('')
