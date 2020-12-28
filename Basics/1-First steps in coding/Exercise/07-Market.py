tsena_iagodi = float(input())
banani = float(input())
portokali = float(input())
malini = float(input())
iagodi = float(input())

tsena_malini = 0.5 * tsena_iagodi
tsena_portokali = 0.6 * tsena_malini
tsena_banani = 0.2 * tsena_malini

kupeni_malini = tsena_malini * malini
kupeni_iagodi = tsena_iagodi * iagodi
kupeni_banani = tsena_banani * banani
kupeni_portokali = tsena_portokali * portokali

pari = kupeni_banani + kupeni_iagodi + kupeni_malini + kupeni_portokali
print(pari)
