import numpy as np
from lokale.variables_ak import *

from lokale.formulas.numer_wpisu import numer_wpisu
from lokale.formulas.tryb_sprzedazy import tryb_sprzedazy
from lokale.formulas.stan_prawny import stan_prawny
from lokale.formulas.rodzaj_osoby import rodzaj_osoby
from lokale.formulas.rodzaj_budynku import rodzaj_budynku
from lokale.formulas.udzial import udzial
from lokale.formulas.powierzchnia_gruntu import powierzchnia_gruntu
from lokale.formulas.lokalizacja import lokalizacja
from lokale.formulas.uwagi_do_ceny import uwagi_do_ceny
from lokale.formulas.kw import kw
from lokale.formulas.uzbrojenie import uzbrojenie
from lokale.formulas.opis import opis
from lokale.formulas.przeznaczenie_terenu import przeznaczenie_terenu
from lokale.formulas.data import data
from lokale.formulas.ulica import ulica
from lokale.formulas.nr_dok import nr_dok
from lokale.formulas.funkcja import oo_funkcja, qq_funkcja
from lokale.formulas.cena import vv_cena, rr_cena, ww_cena_1mkw, ss_cena_1mkw
from lokale.formulas.cena_laczna import cena_laczna
from lokale.formulas.powierzchnia_uzytkowa import powierzchnia_uzytkowa


def if_statements(line):
    for i in kolumny:
        del i[:]

    dane_adresowe = lokalizacja(line)
    dane_ulica = ulica(line)
    docs = nr_dok(line)

    a_okres = ['']
    b_nr = numer_wpisu(line)
    c_ulica = dane_ulica[0]
    d_nr = dane_ulica[1]
    e_tryb_sprzedazy = tryb_sprzedazy(line)
    f_sprzedal = stan_prawny(line)
    g_typ_wlasciciela = rodzaj_osoby(line)
    h_udzial = udzial(line)
    i_rodzaj_nieruchomosci = "GRUNT LOKAL"
    j_dzielnica = dane_adresowe[4]
    k_obreb = dane_adresowe[0]
    l_arkusz = dane_adresowe[1]
    m_dzialka = dane_adresowe[2]
    n_liczba_izb = dane_adresowe[3]
    o_funkcja = oo_funkcja(line)
    p_pow = powierzchnia_gruntu(line)
    q_funkcja = qq_funkcja(line)
    r_cena = rr_cena(line)
    s_cena_1mkw = ss_cena_1mkw(line)
    t_cena_laczna = cena_laczna(line)
    u_powierzchnia_uzytkowa = powierzchnia_uzytkowa(line)
    v_cena = vv_cena(line)
    w_cena_1mkw = ww_cena_1mkw(line)
    x_data = data(line)
    y_uwagi_do_ceny = uwagi_do_ceny(line)
    z_an = docs[0]
    aa_nr_zmiany = docs[1]
    ab_kw = kw(line)
    ac_uzbrojenie = uzbrojenie(line)
    ad_rodzaj_budynku = rodzaj_budynku(line)
    ae_przeznaczenie_terenu = przeznaczenie_terenu(line)
    af_opis_dodatkowy = opis(line)

    z = np.column_stack((a_okres, b_nr, c_ulica, d_nr, e_tryb_sprzedazy,
                         f_sprzedal, g_typ_wlasciciela, h_udzial,
                         i_rodzaj_nieruchomosci, j_dzielnica,
                         k_obreb, l_arkusz, m_dzialka, n_liczba_izb, o_funkcja,
                         p_pow, q_funkcja, r_cena, s_cena_1mkw, t_cena_laczna,
                         u_powierzchnia_uzytkowa, v_cena, w_cena_1mkw, x_data,
                         y_uwagi_do_ceny, z_an, aa_nr_zmiany, ab_kw,
                         ac_uzbrojenie, ad_rodzaj_budynku,
                         ae_przeznaczenie_terenu, af_opis_dodatkowy))
    return z
