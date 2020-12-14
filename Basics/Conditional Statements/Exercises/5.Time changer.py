chas = int(input())
minuti = int(input())
chas_sled_15_minuti = 0
minuti_sled_15_minuti = 0

if minuti + 15 >= 60:
    chas_sled_15_minuti= chas + 1
    minuti_sled_15_minuti = minuti - 45
    if chas == 23:
        chas_sled_15_minuti = 0

if minuti + 15 < 60:
    chas_sled_15_minuti = chas
    minuti_sled_15_minuti = minuti + 15



print(f'{chas_sled_15_minuti}:{minuti_sled_15_minuti:02d}')



chas = int(input())
minuti = int(input())
chas_sled_15_minuti = 0
minuti_sled_15_minuti = 0

if minuti + 15 >= 60:
    chas_sled_15_minuti = chas + 1
    minuti_sled_15_minuti = minuti + 15 - 60


if minuti + 15 < 60:
    chas_sled_15_minuti = chas
    minuti_sled_15_minuti = minuti + 15

if chas_sled_15_minuti > 23:
    chas_sled_15_minuti = 0

print(f'{chas_sled_15_minuti}:{minuti_sled_15_minuti:02d}')