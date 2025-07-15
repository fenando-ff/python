lista_vogais = ["a", "e", "i", "o", "u"]
palavra = input("Digite uma palavra aleatória: ").lower()

qtd_letras = len(palavra)
contador_vogal = 0
contador_consoante = 0
for i in range(len(palavra)):
    verifica = palavra[i]
    if verifica in lista_vogais:
        contador_vogal += 1
    else:
        contador_consoante += 1
print(f"\nHá {contador_vogal} vogais no total\nHá {contador_consoante} consoantes no total")
print(f"\nHá {qtd_letras} letras no total")