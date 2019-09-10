import re



def typ_budynku(line):
    V = re.compile('Rodzaj\\s?bud\\.\\s?:\\s?(jednorodzinne|wielorodzinne|wieIorodzinne)')
    z_typ_budynku = ['']
    try:
        if V.search(line):
            res7 = V.search(line)
            if res7.group(1) == 'jednorodzinne':
                typ = ['jednorodzinny']
                z_typ_budynku.append(typ)
            else:
                z_typ_budynku.append(res7.group(1))
        else:
            z_typ_budynku.append('')
        return z_typ_budynku
    except:
        return z_typ_budynku
