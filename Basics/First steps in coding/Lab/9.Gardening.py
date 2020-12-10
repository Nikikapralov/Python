kvadratni_metri = float(input())
tsena_bez_otstupka = kvadratni_metri * 7.61
discount = tsena_bez_otstupka * 0.18
tsena_sus_otstupka = tsena_bez_otstupka - discount
print(f'The final price is: {tsena_sus_otstupka} lv.')
print(f'The discount is: {discount} lv.')
