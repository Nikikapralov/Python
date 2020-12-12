puzel = 2.60
kukla = 3
meche = 4.10
minion = 8.20
kamionche = 2
tsena_ekskurzia = float(input())
broi_puzeli = int(input())
broi_kukli = int(input())
broi_mecheta = int(input())
broi_minioni = int(input())
broi_kamioncheta = int(input())
vsichki_igrachki = broi_kamioncheta + broi_kukli + broi_mecheta + broi_minioni + broi_puzeli
pari_ot_puzeli = broi_puzeli * puzel
pari_ot_kukli = broi_kukli * kukla
pari_ot_mecheta = broi_mecheta * meche
pari_ot_minioni = broi_minioni * minion
pari_ot_kamioncheta = broi_kamioncheta * kamionche
vsichki_pari_ot_igrachki = pari_ot_kamioncheta + pari_ot_kukli + pari_ot_mecheta + pari_ot_minioni + pari_ot_puzeli
if vsichki_igrachki >= 50:
    pari_sus_otstupka = vsichki_pari_ot_igrachki * 0.75
    ostanali_pari = pari_sus_otstupka * 0.9
    if ostanali_pari >= tsena_ekskurzia:
        razlika = ostanali_pari - tsena_ekskurzia
        print(f'Yes! {razlika:.2f} lv left.')
    else:
        razlika = tsena_ekskurzia - ostanali_pari
        print(f'Not enough money! {razlika:.2f} lv needed.')
else:
    pari_sled_naem = vsichki_pari_ot_igrachki * 0.9
    if pari_sled_naem > tsena_ekskurzia:
        razlika = pari_sled_naem - tsena_ekskurzia
        print(f'Yes! {razlika:.2f} lv left.')
    else:
        razlika = tsena_ekskurzia - pari_sled_naem
        print(f'Not enough money! {razlika:.2f} lv needed.')