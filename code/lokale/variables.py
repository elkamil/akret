a_id = ['']
b_data_transakcji = ['']
c_wojewodztwo = ['']
d_powiat = ['']
e_gmina = ['']
f_miejscowosc = ['']
g_dzielnica = ['']
h_obreb_geodezyjny = ['']
i_arkusz = ['']
h_obreb_geodezyjny = ['']
j_ulica = ['']
k_nr_domu = ['']
l_nr_lokalu = ['']
m_powierzchnia_uzytkowa = ['']
n_cena_laczna = ['']
o_cena_mp2 = ['']
p_cena_mp = ['']
q_cena_mp2mp = ['']
r_kondygnacja = ['']
s_liczba_kondygnacji = ['']
t_liczba_izb = ['']
u_rok_budowy = ['']
v_rodzaj_budynku = ['']
w_stan_prawny_lokalu = ['']
x_stan_prawny_gruntu = ['']
y_typ_wlasciciela = ['']
z_opis = ['']
aa_konstrukcja_budynku = ['']
ab_cena_brutto = ['']
ac_cena_brutto_mp2 = ['']
ad_cena_brutto_mp = ['']
ae_cena_brutto_mp2mp = ['']
af_nr_kw = ['']
ag_sad_wieczysty = ['']
ah_nr_aktu = ['']
ai_zrodlo_danych = ['']
aj_sprzedajacy = ['']
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
bc_kod_pocztowy = ['']
bd_osiedle = ['']
be_strefa_miasta = ['']
bf_otoczenie = ['']
bg_dostepnosc_kom = ['']
bh_zrodlo_ceny = ['']
bi_cena_waluta = ['']
bj_waluta = ['']
bk_kurs_waluty = ['']
bl_stan_prawny_budynku = ['']
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
ca_nr_dzialki = ['']
cb_pole_powierzchni_gruntu = ['']
cc_udzial = ['']
xxx_ulica_geo = ['']
yyy_osm = ['']
ulica_geo = ['']


header_csv = ["Id", "Data transakcji / wyceny", "Województwo", "Powiat", "Gmina", "Miejscowość",
              "Dzielnica", "Obręb geodezyjny", "Arkusz mapy", "Ulica", "Nr domu", "Nr lokalu",
              "Powierzchnia użytkowa (m2)", "Cena", "Cena m2 p.u.", "Cena z uwzględnieniem miejsca postojowego",
              "Cena m2 p.u. z uwzględnieniem miejsca postojowego", "Kondygnacja lokalu", "Liczba kondygnacji",
              "Liczba izb", "Rok budowy", "Rodzaj budynku", "Stan prawny lokalu", "Stan prawny gruntu",
              "Źródło informacji", "Opis", "Konstrukcja budynku", "Cena brutto", "Cena brutto m2 p.u.",
              "Cena brutto z uwzględnieniem miejsca postojowego",
              "Cena brutto m2 p.u. z uwzględnieniem miejsca postojowego", "Nr KW", "Sąd wieczystoksięgowy",
              "Nr aktu notarialnego", "Źródło danych do wpisu", "Sprzedający", "Kupujący",
              "Pomieszczenia przynależne - ilość", "Pomieszczenie przynależne - opis",
              "Cena p. przynależnego zawarta w cenie transakcyjnej", "Pomieszczenia przynależne - Cena za sztukę",
              "Liczba miejsc postojowych", "Rodzaj miejsca postojowego",
              "Cena m. postojowego zawarta w cenie transakcyjnej", "M. postojowe - Cena za sztukę",
              "Pomieszczenia inne przynależne", "Pozostałe obiekty", "Funkcjonalność lokalu", "Standard lokalu",
              "Powierzchnia użytkowa budynku", "Standard techniczny budynku", "Modernizowany w ostatnich 5 latach",
              "Ekspozycja lokalu", "Winda", "Kod pocztowy", "Osiedle", "Strefa miasta", "Otoczenie",
              "Dostępność komunikacyjna", "Źródło ceny", "Cena (waluta)", "Waluta", "Kurs waluty z dn. transakcji",
              "Stan prawny budynku", "Dział III KW lokalu", "Dział III KW gruntu", "Wartość rynkowa",
              "Wartość odtworzeniowa", "Stawka VAT", "M. postojowe - Stawka VAT", "Data utworzenia",
              "Data modyfikacji", "Wpisana przez", "Modyfikowana przez", "Świadectwo charakterystyki energetycznej",
              "Nr św. ch. energetycznej", "Wskaźnik zapotrzebowania na energię pierwotną (EP)",
              "Wskaźnik zapotrzebowania na energię pierwotną (EK)", "Numer działki",
              "Pole powierzchni gruntu", "Udział", "Street View", "OpenStreetMap"]

kolumny = [a_id,  b_data_transakcji, c_wojewodztwo, d_powiat, e_gmina, f_miejscowosc, g_dzielnica, h_obreb_geodezyjny,
           i_arkusz, h_obreb_geodezyjny, j_ulica, k_nr_domu, l_nr_lokalu, m_powierzchnia_uzytkowa, n_cena_laczna,
           o_cena_mp2, p_cena_mp, q_cena_mp2mp, r_kondygnacja, s_liczba_kondygnacji, t_liczba_izb, u_rok_budowy,
           v_rodzaj_budynku, w_stan_prawny_lokalu, x_stan_prawny_gruntu, y_typ_wlasciciela, z_opis,
           aa_konstrukcja_budynku, ab_cena_brutto, ac_cena_brutto_mp2, ad_cena_brutto_mp, ae_cena_brutto_mp2mp,
           af_nr_kw, ag_sad_wieczysty, ah_nr_aktu, ai_zrodlo_danych, aj_sprzedajacy, ak_kupujacy,
           al_pom_przynalezne_ilosc, am_pom_przynalezne_opis, an_cena_pom_przyn, ao_cena_pom_przyn_sztuka,
           ap_liczba_miejsc_post, aq_rodzaj_miejsca_post, ar_cena_miejsca_post, as_miejsce_post_cena,
           at_pom_inne_przyn, au_pozostale_obiekty, av_funkcjonalnosc_lokalu, aw_standard_lokalu,
           ax_powierzchnia_uzytkowa_budynky, ay_stand_tech, az_mod_last_5_y, ba_ekspozycja_lokalu, bb_winda,
           bc_kod_pocztowy, bd_osiedle, be_strefa_miasta, bf_otoczenie, bg_dostepnosc_kom, bh_zrodlo_ceny,
           bi_cena_waluta, bj_waluta, bk_kurs_waluty, bl_stan_prawny_budynku, bm_dzial_3, bn_dzial_3_grunt,
           bo_wartosc_rynkowa, bp_wartosc_odtworzeniowa, bq_stawka_vat, br_mp_stawka_vat, bs_data_utworzenia,
           bt_data_modyfikacji, bu_wpisana_przez, bv_modyfikowana_przez, bw_sw_ch_energ, bx_nr_sw_ch_energ,
           by_wsk_zapot, bz_wsk_zapot_EK, ca_nr_dzialki, cb_pole_powierzchni_gruntu,  cc_udzial, xxx_ulica_geo, yyy_osm]
kolumny1 = ["a_id", "b_data_transakcji", "c_wojewodztwo", "d_powiat", "e_gmina", "f_miejscowosc",
            "g_dzielnica", "h_obreb_geodezyjny", "i_arkusz", "h_obreb_geodezyjny", "j_ulica",
            "k_nr_domu", "l_nr_lokalu", "m_powierzchnia_uzytkowa", "n_cena_laczna", "o_cena_mp2",
            "p_cena_mp", "q_cena_mp2mp", "r_kondygnacja", "s_liczba_kondygnacji", "t_liczba_izb",
            "u_rok_budowy", "v_rodzaj_budynku", "w_stan_prawny_lokalu", "x_stan_prawny_gruntu",
            "y_typ_wlasciciela", "z_opis", "aa_konstrukcja_budynku", "ab_cena_brutto", "ac_cena_brutto_mp2",
            "ad_cena_brutto_mp", "ae_cena_brutto_mp2mp", "af_nr_kw", "ag_sad_wieczysty", "ah_nr_aktu",
            "ai_zrodlo_danych", "aj_sprzedajacy", "ak_kupujacy", "al_pom_przynalezne_ilosc",
            "am_pom_przynalezne_opis", "an_cena_pom_przyn", "ao_cena_pom_przyn_sztuka",
            "ap_liczba_miejsc_post", "aq_rodzaj_miejsca_post", "ar_cena_miejsca_post", "as_miejsce_post_cena",
            "at_pom_inne_przyn", "au_pozostale_obiekty", "av_funkcjonalnosc_lokalu", "aw_standard_lokalu",
            "ax_powierzchnia_uzytkowa_budynky", "ay_stand_tech", "az_mod_last_5_y", "ba_ekspozycja_lokalu",
            "bb_winda", "bc_kod_pocztowy", "bd_osiedle", "be_strefa_miasta", "bf_otoczenie",
            "bg_dostepnosc_kom", "bh_zrodlo_ceny", "bi_cena_waluta", "bj_waluta", "bk_kurs_waluty",
            "bl_stan_prawny_budynku", "bm_dzial_3", "bn_dzial_3_grunt", "bo_wartosc_rynkowa",
            "bp_wartosc_odtworzeniowa", "bq_stawka_vat", "br_mp_stawka_vat", "bs_data_utworzenia",
            "bt_data_modyfikacji", "bu_wpisana_przez", "bv_modyfikowana_przez", "bw_sw_ch_energ",
            "bx_nr_sw_ch_energ", "by_wsk_zapot", "bz_wsk_zapot_EK", "ca_nr_dzialki", "cb_pole_powierzchni_gruntu"]
