# print(matriz)
# print(matriz[0][2])
# print(matriz[1][2])

# linha = 3
# coluna = 3

# matriz = [[0 for _ in range(coluna)] for _ in range(linha)]

# # Preencher a matriz
# for i in range(linha):
#     for j in range(coluna):
#         matriz[i][j] = int(input(f"Digite um valor para a posição [{i}] [{j}]: "))
       
# print(matriz)
# ---------------------------------------------------------------------

# matriz = [[0]*3 for _ in range(3)]

# for i in range(3):
#     for j in range(3):
#         matriz[i][j] = int(input(f"Digite o valor [{i}][{j}]: "))

# for i in range(3):
#     for j in range(3):
#         print(matriz[i][j], end=" ")
#     print()
   
# pares = 0
# for i in range(3):
#         for j in range(3):
#             if matriz[i][j] % 2 == 0:
#                 pares += 1
# print(pares)
   
# n1 = matriz[0][0]
# n2 = matriz[1][1]
# n3 = matriz[2][2]

# print(n1+n2+n3)
# ---------------------------------------------------------------------
qtd_linhas = int(input("Digite a quantidade de linhas da matriz: "))
qtd_colunas = int(input("Digite a quantidade de colunas da matriz: "))
matriz = [[0]*qtd_colunas for _ in range(qtd_linhas)]

for i in range(qtd_linhas):
    for j in range(qtd_colunas):
        matriz[i][j] = int(input(f"Digite o número [{i}] [{j}]: "))
        
for i in range(qtd_linhas):
    print()
    for j in range(qtd_colunas):
        print(matriz[i][j],end=" ")
    

