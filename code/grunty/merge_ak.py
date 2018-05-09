# import re
# from itertools import islice
import numpy as np
from grunty.variables_ak import kolumny
from grunty.formulas.data import data
from grunty.formulas.grunt import lokalizacja
from grunty.formulas.ulica import ulica
from grunty.formulas.rodzaj_osoby import rodzaj_osoby
from grunty.formulas.cena_laczna import cena_laczna
from grunty.formulas.cena import cena, cena_1mkw
from grunty.formulas.uwagi_do_ceny import uwagi_do_ceny
from grunty.formulas.powierzchnia_gruntu import powierzchnia_gruntu
from grunty.formulas.stan_prawny import stan_prawny
from grunty.formulas.udzial import udzial
from grunty.formulas.funkcja import funkcja
from grunty.formulas.typ_budynku import typ_budynku
from grunty.formulas.tryb_sprzedazy import tryb_sprzedazy
from grunty.formulas.numer_wpisu import numer_wpisu
# from grunty.formulas.ceny import ceny
from grunty.formulas.nr_dok import nr_dok
from grunty.formulas.kw import kw
from grunty.formulas.opis import opis
from grunty.formulas.uzbrojenie import uzbrojenie
from grunty.formulas.przeznaczenie_terenu import przeznaczenie_terenu
from grunty.formulas.ulica import ulica


def if_statements(line):
    for i in kolumny:
        del i[:]

# Funkcje
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
    i_rodzaj_nieruchomosci = "GRUNT"
    j_dzielnica = dane_adresowe[2]
    k_obreb = dane_adresowe[0]
    l_arkusz = dane_adresowe[1]
    m_dzialka = dane_adresowe[3]
    n_funkcja = funkcja(line)
    o_cena = cena(line)
    p_cena_1mkw = cena_1mkw(line)
    q_cena_laczna = cena_laczna(line)
    r_pow = powierzchnia_gruntu(line)
    s_data = data(line)
    t_uwagi_do_ceny = uwagi_do_ceny(line)
    u_rep_a = docs[0]
    v_nr_zmiany = docs[1]
    w_kw = kw(line)
    x_uzbrojenie = uzbrojenie(line)
    y_przeznaczenie_terenu = przeznaczenie_terenu(line)
    z_rodzaj_bud = typ_budynku(line)
    aa_opis = opis(line)

    z = np.column_stack((a_okres, b_nr, c_ulica, d_nr, e_tryb_sprzedazy,
                         f_sprzedal, g_typ_wlasciciela, h_udzial,
                         i_rodzaj_nieruchomosci, j_dzielnica,
                         k_obreb, l_arkusz, m_dzialka, n_funkcja,
                         o_cena, p_cena_1mkw,
                         q_cena_laczna, r_pow, s_data,
                         t_uwagi_do_ceny, u_rep_a,
                         v_nr_zmiany, w_kw, x_uzbrojenie,
                         y_przeznaczenie_terenu,
                         z_rodzaj_bud, aa_opis))

    return z
