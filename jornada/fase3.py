registro = {} # Aqui é registrado as chaves e valores dos jogadores

def adicionando_jogadores(qtd_de_jogadores): # Adiciona o nome e a pontuação no registro
    for i in range(1,qtd_de_jogadores+1):
        nome = input(f"\nDigite o nome do {i}º jogador: ")
        try:
            pontos = int(input(f"Digite a pontuação de {nome}: "))
            registro[nome] = pontos 
        except ValueError: # Se o usuário digitar algo diferente de números na pontuação gera uma mensagem de erro
            print("Valor incorreto! Digite um número.")
            
def acima_da_media(media): # Exibi os jogadores com pontuação acima da média
    for nome,pontos in registro.items(): # Verifica os pares com '.items()' (retorna uma lista com pares de chave e seu valor)
        if pontos >  media:
            print(f"Jogador: {nome} - {pontos} pontos")
                
def campeao(): # Exibe o 1º lugar
    maior_pontuação = max(registro.values())
    for nome,pontos in registro.items():
        if pontos == maior_pontuação:
            print(f"\nCampeão: {nome} - {pontos} pontos")

def ultimo(): # exibe o último lugar
    menor_pontuação = min(registro.values())
    for nome,pontos in registro.items():
        if pontos == menor_pontuação:
            print(f"Último: {nome} - {pontos} pontos")

def main():
    qtd_de_jogadores = int(input("Digite quantos jogadores participaram: "))
    adicionando_jogadores(qtd_de_jogadores)
    print("\n______ Resultado ______\n")
    campeao()
    ultimo()
    media = sum(registro.values())/len(registro)
    print(f"\nMédia da pontuação: {media:.2f}\n")
    acima_da_media(media)
    
main()
