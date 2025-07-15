import getpass as G

lista_letras = []
lista_tracos = []
    
def salvar_letras(palavra_secreta): # Guarda as letras da palavra em uma lista
    for i in range(len(palavra_secreta)):
        letra = palavra_secreta[i]
        lista_letras.append(letra)

def tracos():
    for i in range(len(lista_letras)): # Adiciona uma quantidade de traços na lista de traços igual a quantidade de letras
        traco = "_"
        lista_tracos.append(traco)
        
def exibir_jogo(): # exibe cada elemento da lista de traços
    for i in range(len(lista_tracos)):
        print(f"{lista_tracos[i]}",end=" ")
        
def acerto(palpite): # Se acertou uma letra, modifica o traço com a letra de mesmo indice
    for i in range(len(lista_letras)):
         if palpite == lista_letras[i]:
             lista_tracos[i] = palpite

def main():
    palavra_secreta = G.getpass("Digite uma palavra: ").lower() # Não mostra a palavra enquanto é digitada
    salvar_letras(palavra_secreta)
    tracos()
    exibir_jogo()
    for i in range(1,len(lista_letras)+1): # Número de tentativas de acordo com o tamanho da palavra 
        print(f"\n\nTentativa {i} de {len(lista_letras)}")
        palpite = input("Chute uma letra: ").lower()
        acerto(palpite)
        exibir_jogo()
        if lista_tracos == lista_letras: # Se acertar todas as letras antes das tentativas acabarem, encerra o sistema.
            print(f"\nVocê acertou tudo. Parabéns!!")
            break
    print(f"\nA palavra secreta é: {palavra_secreta}")
    
main()