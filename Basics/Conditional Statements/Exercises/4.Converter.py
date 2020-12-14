chislo = float(input())
ot_merna_edinitsa = input()
do_merna_edinitsa = input()
stoinost_cm = 0
stoinost_m = 0
stoinost_mm = 0
if ot_merna_edinitsa == 'mm':
    stoinost_cm = chislo / 10
    stoinost_m = chislo / 1000
    stoinost_mm = chislo
elif ot_merna_edinitsa == 'cm':
    stoinost_cm = chislo
    stoinost_m = chislo / 100
    stoinost_mm = chislo * 10
elif ot_merna_edinitsa == 'm':
    stoinost_cm = chislo * 100
    stoinost_m = chislo
    stoinost_mm = chislo * 1000
if do_merna_edinitsa == 'mm':
    print(f'{stoinost_mm:.3f}')
elif do_merna_edinitsa == 'cm':
    print(f'{stoinost_cm:.3f}')
elif do_merna_edinitsa == 'm':
    print(f'{stoinost_m:.3f}')


