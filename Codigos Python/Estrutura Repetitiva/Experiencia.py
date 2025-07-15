totalRatos = 0
totalCoelhos = 0
totalSapos = 0

print("############# COBAIAS ###############")

N = int(input("Quantos casos de teste serão digitados? "))

for i in range(N):
    qte = int(input("Quantidade de cobaias: "))
    tipoCobaia = input("Tipo de cobaia: ")

    if tipoCobaia == "R" or tipoCobaia == 'r':
        totalRatos += qte
    elif tipoCobaia == "S" or tipoCobaia == "s":
        totalSapos += qte
    elif tipoCobaia == "C" or tipoCobaia == "c":
        totalCoelhos += qte
    else:
        print("Valor Invalido!! Tente Novamente")
         

totalCobaias = totalRatos + totalSapos + totalCoelhos

pcoelhos = (totalCoelhos / totalCobaias) * 100
pratos = (totalRatos / totalCobaias) * 100
psapos = (totalSapos / totalCobaias) * 100

print()
print("RELATORIO FINAL:")
print(f"Total: {totalCobaias} cobaias")
print(f"Total de coelhos: {totalCoelhos}")
print(f"Total de ratos: {totalRatos}")
print(f"Total de sapos: {totalSapos}")
print(f"Percentual de coelhos: {pcoelhos:.2f}")
print(f"Percentual de ratos: {pratos:.2f}")
print(f"Percentual de sapos: {psapos:.2f}")
