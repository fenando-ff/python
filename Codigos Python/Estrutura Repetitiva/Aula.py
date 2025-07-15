# alunos = [10, 20, 40, 80, 30]
# print(alunos)  # Exibe toda a lista de alunos
# print(alunos[2])  # Exibe o valor no índice 2 da lista, que é 40
# print(alunos[1:4])  # Exibe uma sublista com os elementos do índice 1 até (mas não incluindo) o índice 2
# print(len(alunos))  # Exibe o tamanho da lista, ou seja, a quantidade de elementos (5 neste caso)
# print(sum(alunos))  # Calcula e exibe a soma dos valores da lista (180 neste caso)


# media = sum(alunos) / len(alunos)
# print("Média: ", media)


# alunos = ["joao", "pedro", "jose"]
# for x in alunos:
#     print(x)



# nomes = ["joao", "pedro", "jose"]
# notas = [10, 8, 7]
# turma = zip(nomes,notas)
# for x in turma:
#      print(x)


# for nome, nota in zip(nomes, notas):
#     print("Nome: ", nome, " Nota: ", nota)


# # print("Lista com posição e valor:")
# # for i, valor in enumerate(alunos):
# #     print(f"[{i}] -> {valor}")

# # Ordenar e apresentar a lista ordenada
# # lista_ordenada = sorted(alunos)
# # print("Lista ordenada:", lista_ordenada)


# Definindo a lista
lista = [2, 4, 3, 10, 5, 7, 1, 9, 6, 8]

# 1. O elemento na posição 5
print("Elemento na posição 5:", lista[5])  # Saída: 7

# 2. Intervalo da posição 0 até 5 (incluindo a posição 0, excluindo a posição 5)
print("Intervalo da posição 0 até 5:", lista[0:5])  # Saída: [2, 4, 3, 10, 5]

# 3. Intervalo da posição 5 até 9 (incluindo a posição 5, excluindo a posição 9)
print("Intervalo da posição 5 até 9:", lista[5:9])  # Saída: [7, 1, 9, 6]

# 4. A soma de todos os elementos
print("Soma de todos os elementos:", sum(lista))  # Saída: 55

# 5. A média dos elementos da lista
media = sum(lista) / len(lista)
print("Média dos elementos:", media)  # Saída: 5.5

# 6. Apenas os números pares
pares = [x for x in lista if x % 2 == 0]
print("Números pares:", pares)  # Saída: [2, 4, 10, 6, 8]

# 7. Apresentar os elementos da lista, um embaixo do outro
print("Elementos da lista, um por linha:")
for elemento in lista:
    print(elemento)

# 8. Apresentar a lista toda, com a posição e o valor
print("Lista com posição e valor:")
for i, valor in enumerate(lista):
    print(f"[{i}] -> {valor}")

# 9. Ordenar e apresentar a lista ordenada
lista_ordenada = sorted(lista)
print("Lista ordenada:", lista_ordenada)


# # Definindo as listas de cursos e valores
# curso = ["Informática Básica", "Excel", "Programador", "Manutenção de computadores"]
# valor = [150, 200, 500, 400]

# # 1. Apresentar todos os cursos com seu valor ao lado
# print("Cursos com seus valores:")
# for c, v in zip(curso, valor):
#     print(f"{c} -> {v}")

# # 2. Apresentar os nomes dos cursos com valores maiores que 300
# print("Cursos com valores maiores que 300:")
# for c, v in zip(curso, valor):
#     if v > 300:
#         print(c)

# # 3. Apresentar o nome do curso com o maior valor
# max_valor = max(valor)  # Encontrar o maior valor
# curso_max = curso[valor.index(max_valor)]  # Encontrar o curso correspondente
# print(f"Curso com o maior valor: {curso_max} -> {max_valor}")

# # 4. Apresentar o nome do curso com o menor valor
# min_valor = min(valor)  # Encontrar o menor valor
# curso_min = curso[valor.index(min_valor)]  # Encontrar o curso correspondente
# print(f"Curso com o menor valor: {curso_min} -> {min_valor}")

# # 5. Calcular a média dos valores dos cursos e apresentar
# media_valores = sum(valor) / len(valor)
# print(f"Média dos valores dos cursos: {media_valores}")

# # 6. Apresentar os cursos com valores menores que a média
# print("Cursos com valores menores que a média:")
# for c, v in zip(curso, valor):
#     if v < media_valores:
#         print(c)
