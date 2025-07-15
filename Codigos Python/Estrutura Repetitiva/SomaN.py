N = int(input("Digite o valor de N: "))
soma = 0
count = 1
while count <= N:
    soma += count
    count += 1
print("A soma dos primeiros", N, "números é", soma)


# N = int(input("Digite o valor de N: "))
# print("Números pares até", N, ":")
# for i in range(2, N+1, 2):
#     print(i, end=" ")