from lokale_mieszkalne.variables import j_ulica, ulica_geo, k_nr_domu, l_nr_lokalu
from db_kody import create_connection as get_kod
import re

J = re.compile('\\d+\\s?\\.\\s?([^,]+)\\s?,\\s?([^\\d]+)\\s?((?!m\\.).*)\\s?m\\.\\s?([^(\\s]+)\\s?.*')
ulica_m = re.compile('\\sm\\..*')
ulica_else = re.compile('\\d+\\s?\\.\\s?([^,]+)\\s?,\\s?([^\\d]+)\\s?((?!m\\.).*)\\s?\\(.*')
find_mist = re.compile('(G[bB]|%|\\G[dD]\\s|\\sG[gG]\\s|\\sG[aA]\\s)')


def ulica(line):
    # if find_mist.search(line.splitlines()[0]) is not None:
     #   print(line.splitlines()[0])
     #   line = re.sub(r'\sG[Aa]\s',' 6a ', re.sub(r'\sG[gG]\s',' 6g ', re.sub(r'\sG[dD]\s',' 6d ', re.sub(r'G[bB]', '6b', re.sub(r'%', '9b', line.splitlines()[0])))))
     #   print(line)

    line = re.sub(r'\sG[Aa]\s',' 6a ', re.sub(r'\sG[gG]\s',' 6g ', re.sub(r'\sG[dD]\s',' 6d ', re.sub(r'G[bB]', '6b', re.sub(r'%', '9b', line.splitlines()[0])))))
    al_plac = re.compile('^\\s?(AL\\.|al\\.|ALEJA|PL\\.|pl\\.|PLAC)')
    if ulica_m.search(line) is not None:
        res4 = J.search(line)
        if res4 is not None:
            if al_plac.search(res4.group(2)) is not None:
                j_ulica.append(res4.group(2))
                ulica_geo.append(res4.group(2))
            elif al_plac.search(res4.group(2)) is None:
                ulica_plac_al = "ul. " + res4.group(2)
                j_ulica.append(ulica_plac_al)
                ulica_geo.append(res4.group(2))
            else:
                ulica_geo.append(res4.group(2))
                j_ulica.append(res4.group(2))

            k_nr_domu.append(res4.group(3))
            l_nr_lokalu.append(res4.group(4))
            ulica_geo.append(res4.group(2))
        else:
            j_ulica.append('')
            k_nr_domu.append('')
            l_nr_lokalu.append('')
            ulica_geo.append('')
    elif ulica_m.search(line) is None:
        res4 = ulica_else.search(line)
        if al_plac.search(res4.group(2)) is not None:
            ulic = res4.group(2)
            ulica_remove_wolny_rynek = re.sub(r'(\s+|\s?)\((wolny|przetargowy).*\n.*', '', ulic)
            j_ulica.append(ulica_remove_wolny_rynek)
            k_nr_domu.append(res4.group(3))
            l_nr_lokalu.append('')
            ulica_geo.append(ulica_remove_wolny_rynek)
        else:
            ulic = res4.group(2)
            # print("1:",ulic)
            ulica_remove_wolny_rynek = re.sub(r'(\s+|\s?)\((przetargowy|wolny).*\n.*', '', ulic)
            # print("2:",ulica_remove_wolny_rynek)
            l_nr_lokalu.append('')
            ulica_geo.append(ulica_remove_wolny_rynek)
            if len(ulica_remove_wolny_rynek) <= 1:
                j_ulica.append('')
                k_nr_domu.append('')
            else:

                j_ulica.append("ul. "+ulica_remove_wolny_rynek)
                k_nr_domu.append(res4.group(3))
    else:
        j_ulica.append('')
        k_nr_domu.append('')
        l_nr_lokalu.append('')
        ulica_geo.append('')
    # print("Ulica_before:", j_ulica)
    # print("Nr before:", k_nr_domu)
    try:
        # find_char_in_nr_domu = re.compile('[,-/|]')
        find_char_in_nr_domu = re.compile('(.*?)(?=(,|-|/))')
        if find_char_in_nr_domu.search(k_nr_domu[0]):
            K = find_char_in_nr_domu.search(k_nr_domu[0])
            nr_domu_code = int(re.sub(r'[aA-zZ]','',re.sub(r'\s+','',K.group(1))))
        else:
            nr_domu_code = int(re.sub(r'[aA-zZ]','',re.sub(r'\s+','',k_nr_domu[0])))
    except:
        pass
        nr_domu_code = ''
    if j_ulica[0] and nr_domu_code:
        ulica_code = re.sub(r'^ul.\s?','',re.sub(r'\s+','',re.sub(r'[Źź]','z',re.sub(r'[Żż]','z',re.sub(r'[Śś]','s',re.sub(r'[óÓ]','o',re.sub(r'[Ńń]','',re.sub(r'[Łł]','l',re.sub(r'[Ćć]','c', re.sub(r'[Ęę]','e',re.sub(r'[ąĄ]','a',j_ulica[0]))))))))))).lower()
        kod = get_kod(ulica_code, nr_domu_code)
        # print("Ulica:", ulica_code)
        # print("Nr domu:", nr_domu_code)
    else:
        kod = ['']
        # print("Line:", line)
        # print("Ulica:", j_ulica)
        # print("Nr domu poprawiony:{0} ||| Nr domu original:{1}".format(nr_domu_code,k_nr_domu))
    return j_ulica, k_nr_domu, l_nr_lokalu, ulica_geo, kod
