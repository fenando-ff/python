x = int(input("Informe o primeiro numero: "))
y = int(input("Informe o segundo numero: "))

while x != y:
    if x < y:
        print("CRESCENTE")
    else:
        print("DECRESCENTE")
    
    x = int(input("Informe o primeiro numero: "))
    y = int(input("Informe o segundo numero: "))

print("Os dois valores são iguais. Programa finalizado!")