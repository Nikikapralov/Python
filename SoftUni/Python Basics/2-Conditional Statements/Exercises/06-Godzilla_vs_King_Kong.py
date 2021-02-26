biudjet = float(input())
statisti = int(input())
tsena_za_obleklo_na_1_statist = float(input())
dekor = biudjet * 0.1
neobhodimi_pari = tsena_za_obleklo_na_1_statist * statisti + dekor
nedostigashti_pari = neobhodimi_pari - biudjet
dostigashti_pari = biudjet - neobhodimi_pari

if statisti > 150:
    tsena_za_obleklo_na_1_statist = tsena_za_obleklo_na_1_statist * 0.9
    neobhodimi_pari = tsena_za_obleklo_na_1_statist * statisti + dekor
    nedostigashti_pari = neobhodimi_pari - biudjet
    dostigashti_pari = biudjet - neobhodimi_pari

if neobhodimi_pari > biudjet:
    print('Not enough money!')
    print(f'Wingard needs {nedostigashti_pari:.2f} leva more.')

if neobhodimi_pari <= biudjet:
    print('Action!')
    print(f'Wingard starts filming with {dostigashti_pari:.2f} leva left.')
