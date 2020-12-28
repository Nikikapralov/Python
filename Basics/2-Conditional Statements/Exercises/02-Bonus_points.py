chislo = int(input())
bonus_tochki_chislo_do_100 = 5
bonus_tochki_chislo_poveche_ot_100 = 0.20 * chislo
bonus_tochki_chislo_poveche_ot_1000 = 0.10 * chislo
ostatuk = chislo / 5
if_ostatuk_necheten = ostatuk % 2 == 1
if chislo <= 100:
    bonus_tochki = bonus_tochki_chislo_do_100
    if chislo % 2 == 0:
        kraini_bonus_tochki = bonus_tochki_chislo_do_100 + 1
        print(kraini_bonus_tochki)
        print(kraini_bonus_tochki + chislo)
    elif if_ostatuk_necheten:
        kraini_bonus_tochki = bonus_tochki_chislo_do_100 + 2
        print(kraini_bonus_tochki)
        print(kraini_bonus_tochki + chislo)
    else:
        kraini_bonus_tochki = bonus_tochki_chislo_do_100
        print(kraini_bonus_tochki)
        print(kraini_bonus_tochki + chislo)
if chislo > 1000:
    bonus_tochki = bonus_tochki_chislo_poveche_ot_1000
    if chislo % 2 == 0:
        kraini_bonus_tochki = bonus_tochki_chislo_poveche_ot_1000 + 1
        print(kraini_bonus_tochki)
        print(kraini_bonus_tochki + chislo)
    elif if_ostatuk_necheten:
        kraini_bonus_tochki = bonus_tochki_chislo_poveche_ot_1000 + 2
        print(kraini_bonus_tochki)
        print(kraini_bonus_tochki + chislo)
    else:
        kraini_bonus_tochki = bonus_tochki_chislo_poveche_ot_1000
        print(kraini_bonus_tochki)
        print(kraini_bonus_tochki + chislo)
elif chislo > 100:
    bonus_tochki = bonus_tochki_chislo_poveche_ot_100
    if chislo % 2 == 0:
        kraini_bonus_tochki = bonus_tochki_chislo_poveche_ot_100 + 1
        print(kraini_bonus_tochki)
        print(kraini_bonus_tochki + chislo)
    elif if_ostatuk_necheten:
        kraini_bonus_tochki = bonus_tochki_chislo_poveche_ot_100 + 2
        print(kraini_bonus_tochki)
        print(kraini_bonus_tochki + chislo)
    else:
        kraini_bonus_tochki = bonus_tochki_chislo_poveche_ot_100
        print(kraini_bonus_tochki)
        print(kraini_bonus_tochki + chislo)