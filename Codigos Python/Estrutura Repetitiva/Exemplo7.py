popA=int(input("População do país A: "))
while popA<0:
    popA=int(input("População do país deve ser maior que 0: "))
taxaA=float(input("Taxa de crescimento da cidade A: "))

popB=int(input("População do país B: "))
while popB<0:
    popB=int(input("População do país deve ser maior que 0: "))
taxaB=float(input("Taxa de crescimento da cidade B: "))

ano=0
while popA < popB:
    ano += 1
    popA = int((1 + (taxaA/100) )* popA)
    popB = int((1 + (taxaB/100) )* popB)
    print("Ano %d:" % ano)
    print("Populaçao A: %d" % popA)
    print("População B: %d\n\n" % popB)

print("Ultrapassa no ano:",ano)