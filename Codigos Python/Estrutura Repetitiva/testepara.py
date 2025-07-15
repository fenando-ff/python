N = int(input("Quantos números serão digitados? "))
soma = 0

for i in range(1, N + 1):
    x = int(input("Digite um número: "))
    soma += x


print("SOMA =", soma)
