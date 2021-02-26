electrons = int(input())
orbital = 0
electrons_orbitals = []
while True:
    orbital += 1
    electrons_per_orbital = 2*(orbital**2)
    if electrons - electrons_per_orbital < 0:
        electrons_orbitals.append(electrons)
        break
    else:
        electrons_orbitals.append(electrons_per_orbital)
        electrons -= electrons_per_orbital
        if electrons == 0:
            break
print(electrons_orbitals)