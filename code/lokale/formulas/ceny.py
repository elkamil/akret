import re

from lokale_mieszkalne.variables import y_typ_wlasciciela, aj_sprzedajacy, n_cena_laczna, ab_cena_brutto, \
    m_powierzchnia_uzytkowa, ac_cena_brutto_mp2, o_cena_mp2

Y = re.compile('Typ\\s?właś.*\\s?:\\s?(osoba fizyczna|\\s?osoba\\s?fizyczna|\\s?osoba\\s?prawna|gmina|\\s?gmina\\s?|\
               \\s?Skarb\\s?Państwa|Skarb Państwa)', re.IGNORECASE)
N = re.compile('.*Cena\\s?łączna\\snieruchomości\\s?:\\s?\\b([^zł]+)(?=\\s?z?ł?\\s?okre).*')
Z_uwagi_do_ceny = re.compile('.*Uwagi\\s?do\\s?ceny\\s?:\\s?(.*?)(?=\\s?Nr\\s?dok).*', re.S)
M = re.compile('.*Pow\\.\\s?użytk\\.\\s?:\\s?\\b(.*)(?=\\s?m\\s?kw\\.).*')


def ceny(line):
    if Y.search(line):
        res = Y.search(line)
        res_y1 = res.group(1)
        aj_sprzedajacy.append(res.group(1))
        if res_y1 in ['osoba fizyczna']:
            res_y = "Umowa ostateczna sprzedaży rynek wtórny"
            y_typ_wlasciciela.append(res_y)
        elif res_y1 in ['osoba prawna']:
            res_y = "Umowa ostateczna sprzedaży rynek pierwotny"
            y_typ_wlasciciela.append(res_y)
        else:
            res_y = "Przetarg (w przypadku transakcji przetargowych)"
            y_typ_wlasciciela.append(res_y)
    else:
        y_typ_wlasciciela.append('')
        aj_sprzedajacy.append('')
        res_y1 = ''

    if Z_uwagi_do_ceny.search(line):
        res11 = Z_uwagi_do_ceny.search(line)
        uwagi_do_ceny = res11.group(1)
    else:
        uwagi_do_ceny = ''

    brutto = re.compile('(brr?utt?o|vat|brut)', re.IGNORECASE)
    netto = re.compile('(netto|nett?o|net)', re.IGNORECASE)
    if N.search(line):
        res6 = N.search(line)
        res6prim = res6.group(1)
        res6prim1 = re.sub(r'\s+', '', res6prim)
        if res_y1 in ['osoba fizyczna', 'Skarb Państwa']:
            n_cena_laczna.append(res6prim1)
            ab_cena_brutto.append(res6prim1)
        elif res_y1 in ['gmina']:
            n_cena_laczna.append('')
            ab_cena_brutto.append(res6prim1)
        elif res_y1 in ['osoba prawna']:
            if brutto.search(uwagi_do_ceny) is None:
                if netto.search(uwagi_do_ceny) is not None:
                    n_cena_laczna.append(round(float(res6prim1), 2))
                    brutto = float(res6prim1) * 1.08
                    ab_cena_brutto.append(round(brutto, 2))
                else:
                    ab_cena_brutto.append(round(float(res6prim1), 2))
                    netto = float(res6prim1) / 1.08
                    n_cena_laczna.append(round(netto, 2))
                    uwagi_do_ceny = "Brak informacji czy cena netto/brutto, ceny unettowiono " + uwagi_do_ceny
            else:
                ab_cena_brutto.append(round(float(res6prim1), 2))
                netto = float(res6prim1) / 1.08
                n_cena_laczna.append(round(netto, 2))
        else:
            n_cena_laczna.append('')
            ab_cena_brutto.append('')
    else:
        n_cena_laczna.append('')
        ab_cena_brutto.append('')

    # ceny per m2
    if M.search(line):
        res5 = M.search(line)
        m_powierzchnia_uzytkowa.append(round(float(res5.group(1)), 2))
    else:
        m_powierzchnia_uzytkowa.append('')

    # cena brutto
    if ab_cena_brutto[0] != '' and m_powierzchnia_uzytkowa[0] != '':
        brutto_za_m2 = float(ab_cena_brutto[0]) / float(m_powierzchnia_uzytkowa[0])
        ac_cena_brutto_mp2.append(round(brutto_za_m2, 2))
    else:
        ac_cena_brutto_mp2.append('')

    # cena netto
    if n_cena_laczna[0] != '' and m_powierzchnia_uzytkowa[0] != '':
        netto_za_m2 = float(n_cena_laczna[0]) / float(m_powierzchnia_uzytkowa[0])
        o_cena_mp2.append(round(netto_za_m2, 2))
    else:
        o_cena_mp2.append('')

    if n_cena_laczna[0]:
        n_cena_laczna_2f = ['%.2f' % elem for elem in [float(i) for i in n_cena_laczna]]
    else:
        n_cena_laczna_2f = ['']
    if ab_cena_brutto[0]:
        ab_cena_brutto_2f = ['%.2f' % elem for elem in [float(i) for i in ab_cena_brutto]]
    else:
        ab_cena_brutto_2f = ['']
    if ac_cena_brutto_mp2[0]:
        ac_cena_brutto_mp2_2f = ['%.2f' % elem for elem in [float(i) for i in ac_cena_brutto_mp2]]
    else:
        ac_cena_brutto_mp2_2f = ['']
    if o_cena_mp2[0]:
        o_cena_mp2_2f = ['%.2f' % elem for elem in [float(i) for i in o_cena_mp2]]
    else:
        o_cena_mp2_2f = ['']
    return y_typ_wlasciciela, aj_sprzedajacy, uwagi_do_ceny, n_cena_laczna_2f, ab_cena_brutto_2f, \
           m_powierzchnia_uzytkowa, ac_cena_brutto_mp2_2f, o_cena_mp2_2f

    # return y_typ_wlasciciela, aj_sprzedajacy, uwagi_do_ceny, format(n_cena_laczna, '.2f'),
    # format(ab_cena_brutto, '.2f'), m_powierzchnia_uzytkowa, format(ac_cena_brutto_mp2, '.2f'),
    # format(o_cena_mp2, '.2f')
