import numpy as np
from budynki.variables_ak import *
from budynki.formulas.numer_wpisu import numer_wpisu
from budynki.formulas.udzial import udzial
from budynki.formulas.rodzaj_osoby import rodzaj_osoby
from budynki.formulas.tryb_sprzedazy import tryb_sprzedazy
from budynki.formulas.opis import opis
from budynki.formulas.uzbrojenie import uzbrojenie
from budynki.formulas.przeznaczenie_terenu import przeznaczenie_terenu
from budynki.formulas.rodzaj_budynku import rodzaj_budynku
from budynki.formulas.kw import kw
from budynki.formulas.data import data
from budynki.formulas.uwagi_do_ceny import uwagi_do_ceny
from budynki.formulas.liczba_kondygnacji import liczba_kondygnacji
from budynki.formulas.lokalizacja import lokalizacja
from budynki.formulas.cena_laczna import cena_laczna
from budynki.formulas.stan_prawny import stan_prawny
from budynki.formulas.ulica import ulica
from budynki.formulas.funkcja import oo_funkcja, qq_funkcja
from budynki.formulas.powierzchnia_gruntu import powierzchnia_gruntu
from budynki.formulas.powierzchnia_uzytkowa import powierzchnia_uzytkowa
from budynki.formulas.cena import vv_cena, rr_cena, ww_cena_1mkw, ss_cena_1mkw
from budynki.formulas.nr_dok import nr_dok


def if_statements(line):
    for i in kolumny:
        del i[:]

    dane_adresowe = lokalizacja(line)
    dane_ulica = ulica(line)
    docs = nr_dok(line)
    udz = udzial(line)

    a_okres = ['']
    b_nr = numer_wpisu(line)
    c_ulica = dane_ulica[0]
    d_nr = dane_ulica[1]
    e_tryb_sprzedazy = tryb_sprzedazy(line)
    f_sprzedal = stan_prawny(line)
    g_typ_wlasciciela = rodzaj_osoby(line)
    h_udzial = udz[0]
    h1_udzial_procent = udz[1]
    i_rodzaj_nieruchomosci = "GRUNT BUDYNEK"
    j_dzielnica = dane_adresowe[3]
    k_obreb = dane_adresowe[0]
    l_arkusz = dane_adresowe[1]
    m_dzialka = dane_adresowe[2]
    n_liczba_kondygnacji = liczba_kondygnacji(line)
    o_funkcja_gruntu = oo_funkcja(line)
    p_pow_gr = powierzchnia_gruntu(line)
    q_funkcja_bud = qq_funkcja(line)
    r_cena = rr_cena(line)
    s_cena_1mkw = ss_cena_1mkw(line)
    t_cena_laczna = cena_laczna(line)
    u_pow_uzytkowa = powierzchnia_uzytkowa(line)
    v_cena = vv_cena(line)
    w_cena_1mkw = ww_cena_1mkw(line)
    x_data = data(line)
    y_uwagi_do_ceny = uwagi_do_ceny(line)
    z_rep_a = docs[0]
    aa_nr_zmiany = docs[1]
    ab_kw = kw(line)
    ac_uzbrojenie = uzbrojenie(line)
    ad_przeznaczenie_terenu = przeznaczenie_terenu(line)
    ae_rodzaj_budynku = rodzaj_budynku(line)
    af_opis = opis(line)

    z = np.column_stack((a_okres, b_nr, c_ulica, d_nr, e_tryb_sprzedazy,
                         f_sprzedal, g_typ_wlasciciela, h_udzial, h1_udzial_procent,
                         i_rodzaj_nieruchomosci, j_dzielnica,
                         k_obreb, l_arkusz, m_dzialka, n_liczba_kondygnacji,
                         o_funkcja_gruntu, p_pow_gr, q_funkcja_bud,
                         r_cena, s_cena_1mkw, t_cena_laczna, u_pow_uzytkowa,
                         v_cena, w_cena_1mkw, x_data, y_uwagi_do_ceny,
                         z_rep_a, aa_nr_zmiany, ab_kw, ac_uzbrojenie,
                         ad_przeznaczenie_terenu, ae_rodzaj_budynku, af_opis))
    return z
