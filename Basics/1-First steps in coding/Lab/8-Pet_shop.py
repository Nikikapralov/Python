hrana_kucheta = 2.50
hrana_druga = 4.00
broi_kupena_kucheta = int(input())
broi_kupena_druga = int(input())
tsena_kucheta = hrana_kucheta * broi_kupena_kucheta
tsena_drugi = hrana_druga * broi_kupena_druga
obshta_tsena = tsena_drugi + tsena_kucheta
print(f' {obshta_tsena} lv.')