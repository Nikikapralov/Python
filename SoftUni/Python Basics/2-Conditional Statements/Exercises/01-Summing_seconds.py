vreme_1 = int(input())
vreme_2 = int(input())
vreme_3 = int(input())
obshto_vreme = vreme_1 + vreme_2 + vreme_3
obshto_vreme_minuti = obshto_vreme // 60
obshto_vreme_sekundi = obshto_vreme % 60
if obshto_vreme_sekundi < 10:
    print(f'{obshto_vreme_minuti:.0f}:0{obshto_vreme_sekundi}')
else:
    print(f'{obshto_vreme_minuti}:{obshto_vreme_sekundi}')
