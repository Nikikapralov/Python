depozirana_suma = float(input())
srok_depozit = int(input())
lihven_prozent = float(input())
smetka_1 = srok_depozit * ((depozirana_suma * lihven_prozent / 100) / 12)
suma = depozirana_suma + smetka_1
print(suma)