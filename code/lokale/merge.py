import numpy as np
import re
from lokale_mieszkalne.variables import *
from is_online import is_online
from geo import geo

from lokale_mieszkalne.formulas.b_data_transakcji import b_data
from lokale_mieszkalne.formulas.lokalizacja import lokalizacja
from lokale_mieszkalne.formulas.ulica import ulica
from lokale_mieszkalne.formulas.ceny import ceny
from lokale_mieszkalne.formulas.stan_prawny import stan_prawny
from lokale_mieszkalne.formulas.rodzaj_budynku import rodzaj_budynku
from lokale_mieszkalne.formulas.pole_powierzchni import pole_powierzchni
from lokale_mieszkalne.formulas.nr_dok import nr_dok
from lokale_mieszkalne.formulas.kw import kw
from lokale_mieszkalne.formulas.udzial import udzial
from lokale_mieszkalne.formulas.opis import opis as opis_f

# file = "/home/ee/ee_convert/data/obreby.csv"

# obreby_csv = pd.read_csv(file, sep=';', encoding='utf-8')


def if_statements(line):
    for i in kolumny:
        del i[:]

    dane_adresowe = lokalizacja(line)
    dane_ulica = ulica(line)

    cena = ceny(line)
    kw_all = kw(line)

    a_id = ['']
    b_data_transakcji = b_data(line)
    c_wojewodztwo = ['dolnośląskie']
    d_powiat = ['Wrocław']
    e_gmina = dane_adresowe[4]
    f_miejscowosc = dane_adresowe[5]
    g_dzielnica = dane_adresowe[6]
    h_obreb_geodezyjny = dane_adresowe[0]
    i_arkusz = dane_adresowe[1]
    j_ulica = dane_ulica[0]
    k_nr_domu = dane_ulica[1]
    l_nr_lokalu = dane_ulica[2]
    m_powierzchnia_uzytkowa = cena[5]
    n_cena_laczna = cena[3]
    o_cena_mp2 = cena[7]
    p_cena_mp = ['']
    q_cena_mp2mp = ['']
    r_kondygnacja = ['']
    s_liczba_kondygnacji = ['']
    t_liczba_izb = dane_adresowe[3]
    u_rok_budowy = ['']
    v_rodzaj_budynku = rodzaj_budynku(line)
    w_stan_prawny_lokalu = ['Prawo własności']
    y_typ_wlasciciela = cena[0]
    x_stan_prawny_gruntu = stan_prawny(line)
    aa_konstrukcja_budynku = ['']
    ab_cena_brutto = cena[4]
    ac_cena_brutto_mp2 = cena[6]
    ad_cena_brutto_mp = ['']
    ae_cena_brutto_mp2mp = ['']
    af_nr_kw = kw_all[0]
    ag_sad_wieczysty = ['Sąd Rejonowy dla Wrocławia - Krzyków']
    ah_nr_aktu = nr_dok(line)
    ai_zrodlo_danych = ['RCiWN']
    aj_sprzedajacy = cena[1]
    ak_kupujacy = ['']
    al_pom_przynalezne_ilosc = ['']
    am_pom_przynalezne_opis = ['']
    an_cena_pom_przyn = ['']
    ao_cena_pom_przyn_sztuka = ['']
    ap_liczba_miejsc_post = ['']
    aq_rodzaj_miejsca_post = ['']
    ar_cena_miejsca_post = ['']
    as_miejsce_post_cena = ['']
    at_pom_inne_przyn = ['']
    au_pozostale_obiekty = ['']
    av_funkcjonalnosc_lokalu = ['']
    aw_standard_lokalu = ['']
    ax_powierzchnia_uzytkowa_budynky = ['']
    ay_stand_tech = ['']
    az_mod_last_5_y = ['']
    ba_ekspozycja_lokalu = ['']
    bb_winda = ['']
    bc_kod_pocztowy = dane_ulica[4]
    bd_osiedle = ['']
    be_strefa_miasta = ['']
    bf_otoczenie = ['']
    bg_dostepnosc_kom = ['']
    bh_zrodlo_ceny = ['Transakcja']
    bi_cena_waluta = ['']
    bj_waluta = ['PLN']
    bk_kurs_waluty = ['']
    bl_stan_prawny_budynku = ['Prawo własności']
    bm_dzial_3 = ['']
    bn_dzial_3_grunt = ['']
    bo_wartosc_rynkowa = ['']
    bp_wartosc_odtworzeniowa = ['']
    bq_stawka_vat = ['']
    br_mp_stawka_vat = ['']
    bs_data_utworzenia = ['']
    bt_data_modyfikacji = ['']
    bu_wpisana_przez = ['']
    bv_modyfikowana_przez = ['']
    bw_sw_ch_energ = ['']
    bx_nr_sw_ch_energ = ['']
    by_wsk_zapot = ['']
    bz_wsk_zapot_EK = ['']
    ca_nr_dzialki = dane_adresowe[2]
    cb_pole_powierzchni_gruntu = pole_powierzchni(line)
    cc_udzial = udzial(line)
    # xxx_ulica_geo = geo(j_ulica[0], nr_domu_code)
    if is_online():
        geo_data = geo(dane_ulica[5], dane_ulica[6])
        xxx_ulica_geo = geo_data[0]
        yyy_osm = geo_data[1]
    else:
        xxx_ulica_geo = ['']
    # ulica_geo = ['']

    if cena[2]:
        cena_opis = cena[2]
    else:
        cena_opis = ''

    if opis_f(line):
        opis_opis = opis_f(line)
    else:
        opis_opis = ''

    if dane_adresowe[7]:
        adres_opis = dane_adresowe[7]
    else:
        adres_opis = ''

    if kw_all[1]:
        kw_opis = 'księga gruntowa: {0}'.format(kw_all[1])
    else:
        kw_opis = ''

    tt = ''
    for i in [cena_opis, opis_opis, adres_opis, kw_opis]:
        if i:
            tt += str(i) + ';'
    tt = re.sub(r';$', '', re.sub(r'\n', '', tt))
    z_opis = tt
    z = np.column_stack((a_id, b_data_transakcji, c_wojewodztwo, d_powiat, e_gmina, f_miejscowosc,
                         g_dzielnica, h_obreb_geodezyjny, i_arkusz, j_ulica, k_nr_domu, l_nr_lokalu,
                         m_powierzchnia_uzytkowa, n_cena_laczna, o_cena_mp2, p_cena_mp, q_cena_mp2mp,
                         r_kondygnacja, s_liczba_kondygnacji, t_liczba_izb, u_rok_budowy, v_rodzaj_budynku,
                         w_stan_prawny_lokalu,  x_stan_prawny_gruntu, y_typ_wlasciciela, z_opis,
                         aa_konstrukcja_budynku, ab_cena_brutto, ac_cena_brutto_mp2, ad_cena_brutto_mp,
                         ae_cena_brutto_mp2mp, af_nr_kw, ag_sad_wieczysty, ah_nr_aktu, ai_zrodlo_danych,
                         aj_sprzedajacy, ak_kupujacy, al_pom_przynalezne_ilosc, am_pom_przynalezne_opis,
                         an_cena_pom_przyn, ao_cena_pom_przyn_sztuka, ap_liczba_miejsc_post, aq_rodzaj_miejsca_post,
                         ar_cena_miejsca_post, as_miejsce_post_cena, at_pom_inne_przyn, au_pozostale_obiekty,
                         av_funkcjonalnosc_lokalu, aw_standard_lokalu, ax_powierzchnia_uzytkowa_budynky,
                         ay_stand_tech, az_mod_last_5_y, ba_ekspozycja_lokalu, bb_winda, bc_kod_pocztowy,
                         bd_osiedle, be_strefa_miasta, bf_otoczenie, bg_dostepnosc_kom, bh_zrodlo_ceny,
                         bi_cena_waluta, bj_waluta, bk_kurs_waluty, bl_stan_prawny_budynku, bm_dzial_3,
                         bn_dzial_3_grunt, bo_wartosc_rynkowa, bp_wartosc_odtworzeniowa, bq_stawka_vat,
                         br_mp_stawka_vat, bs_data_utworzenia, bt_data_modyfikacji, bu_wpisana_przez,
                         bv_modyfikowana_przez, bw_sw_ch_energ, bx_nr_sw_ch_energ, by_wsk_zapot, bz_wsk_zapot_EK,
                         ca_nr_dzialki, cb_pole_powierzchni_gruntu,  cc_udzial, xxx_ulica_geo, yyy_osm))
    return z
