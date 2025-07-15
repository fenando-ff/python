# Faça um sistema que:
# 1 - Receba um número do usuário
# 2 - Mostre todos números primos até chegar no número informado
# Ex:
# número escolhido: 24
# Número primos: 2,3,5,7,11,13,17,19,23
# 3 - mostre todos os números primos dentro de uma lista
# 4  - some todos itens da lista e multiplique o produto pelo o número informado
# 5 - mostre resumo geral do que o sistema fez, mostrando o número informado, a lista dos números primos, os cálculos feitos e o resultado final
# 6- o sistema deve rodar até o usuário desejar parar


lista_primo= []
def numero_primo(numero):
    if numero > 1:
        lista_numeros = []
        for i in range(1,numero+1):
            if numero % i == 0:
                lista_numeros.append(i) # Adiciona na lista os numeros em que são divisíveis
        if len(lista_numeros) < 3: # Se a quantidade de elementos na lista for 2 ele aramazena na lista de números primos
            lista_primo.append(numero)

def lista_de_primos(numero):          
    for j in range(2,numero):
        numero_primo(j)
       
def somando(lista_primo):
    soma = sum(lista_primo)
    for i in range(len(lista_primo)):
        primo_na_lista = lista_primo[i]
        print(primo_na_lista, end=" + ")
    return soma
   
controle = "s"
while controle == "s":    
    numero = int(input("Digite um número: "))        
    numero_primo(numero)
    lista_de_primos(numero)
    soma = somando(lista_primo)
    print(f"\n{soma} x {numero} = {soma*numero}")
    controle = input("Deseja continuar? (s/n)")