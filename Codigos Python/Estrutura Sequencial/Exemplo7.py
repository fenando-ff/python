
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
endereco = input("Digite o seu endereço: ")
estado_civil = input("Digite o seu estado civil: ")
escolaridade = input("Digite a sua escolaridade: ")
salario1 = float(input("Qual o seu salario no primeiro mes? "))
salario2 = float(input("Qual o seu salario no segundo mes? "))
salario3 = float(input("Qual o seu salario no terceiro mes? "))

salario_medio = (salario1 + salario2 + salario3) / 3
dif_salario = salario1 - salario2

print("DADOS DIGITADOS: ")
print(nome)
print(f"Idade: {idade} anos")
print(f"Endereço: {endereco}")
print(f"Estado civil: {estado_civil}")
print(f"Salario1: {salario1:.2f}")
print(f"Salario2: {salario2:.2f}")
print(f"Salario3: {salario3:.2f}\n")
print(f"Salario medio: {salario_medio:.2f}" )
print(f"Diferença de salario 1 e 2: {abs(dif_salario)}")