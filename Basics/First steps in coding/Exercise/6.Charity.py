dni = int(input())
sladkari = int(input())
torti = int(input())
gofreti = int(input())
palachinki = int(input())
pari_torti = torti * 45
pari_gofreti = gofreti * 5.80
pari_palachinki = palachinki * 3.20
subrana_suma = (pari_gofreti + pari_palachinki + pari_torti) * dni * sladkari
pari_za_pokrivane = 1/8 * subrana_suma
kraina_suma = subrana_suma - pari_za_pokrivane
print(kraina_suma)
