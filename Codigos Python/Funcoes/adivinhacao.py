import random

def gerar_numero():
    return random.randint(1, 10)

def verificar_tentativa(numero_secreto, tentativa):
    if tentativa == numero_secreto:
        return "Parabéns! Você acertou!"
    elif tentativa < numero_secreto:
        return "O número é maior!"
    else:
        return "O número é menor!"

# Lógica do jogo
numero_secreto = gerar_numero()
tentativas = 3

print("🎯 Jogo de Adivinhação (1 a 10)")

for i in range(tentativas):
    tentativa = int(input(f"Tentativa {i+1}: "))
    mensagem = verificar_tentativa(numero_secreto, tentativa)
    print(mensagem)
    if tentativa == numero_secreto:
        break
else:
    print(f"Que pena! O número era {numero_secreto}.")
