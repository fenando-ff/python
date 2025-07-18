# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Responda às perguntas com 'sim' ou 'não'.")

pergunta1 = input("Telefonou para a vítima? ").lower()
pergunta2 = input("Esteve no local do crime? ").lower()
pergunta3 = input("Mora perto da vítima? ").lower()
pergunta4 = input("Devia para a vítima? ").lower()
pergunta5 = input("Já trabalhou com a vítima? ").lower()

respostas_positivas = 0

if pergunta1 == 'sim':
    respostas_positivas += 1
if pergunta2 == 'sim':
    respostas_positivas += 1
if pergunta3 == 'sim':
    respostas_positivas += 1
if pergunta4 == 'sim':
    respostas_positivas += 1
if pergunta5 == 'sim':
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Você é classificado como 'Suspeita'.")
elif respostas_positivas <= 4:
    print("Você é classificado como 'Cúmplice'.")
elif respostas_positivas == 5:
    print("Você é classificado como 'Assassino'.")
else:
    print("Você é classificado como 'Inocente'.")
