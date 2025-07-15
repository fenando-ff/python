N = int(input("Digite o valor de N: "))
fat = 1

for i in range(1, N + 1):
    fat *= i


print("A fatorial de N é:", fat)