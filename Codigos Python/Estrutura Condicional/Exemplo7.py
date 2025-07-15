# Solicita ao usuário para inserir um número de 1 a 7
numero = int(input("Digite um número de 1 a 7: "))

# Verifica o número e exibe o dia da semana correspondente
if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Valor inválido. Insira um número de 1 a 7.")
