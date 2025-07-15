# Faça um sistema de ata batismal
# O sistema deve perguntar quem está presidindo, dirigindo, 1º hino, 1ª oração, quem deixa a mensagem e qual o tema, regente, as pessoas que vão ser batizadas e as pessoas que batizaram,
# as testemunhas e último hino e oração
# Exibir em formato de ata
import datetime as D

lista_batizados = []
lista_batizadores = []
lista_testemunhas = []
lista_hinos = []
lista_oracao = []

def adicionando_oracao():
    for i in range(1,3):
        oracao = input(f"Quem vai fazer a {i}ª oração? : ")
        lista_oracao.append(oracao)
        
def adicionando_hino():
    for i in range(1,3):
        hino = input(f"Qual o {i}º hino? : ")
        lista_hinos.append(hino)

def adicionando_batizados():
    qtd_batizados = int(input("Quantas pessoas irão ser batizadas?: "))
    for i in range(1,qtd_batizados+1):
        batizado = input(f"Qual o nome da {i}ª pessoa?: ")
        lista_batizados.append(batizado)
    return qtd_batizados

def adicionando_batizadores(qtd_batizados):
    controlador = 0
    while controlador == 0:
        qtd_batizadores = int(input("Quantas pessoas irão ser batizadores? : "))
        if qtd_batizadores < 1:
            print("Quantidade de batizadores não pode ser zero! Tente novamente.")
        elif qtd_batizadores > qtd_batizados:
            print("Quantidade de batizadores não pode ser maior que a de batizados! Tente novamente.")
        else: 
            for i in range(1,qtd_batizadores+1):
                batizadores = input(f"Qual o nome do {i}º batizador? : ")
                lista_batizadores.append(batizadores)
            controlador = 1
        
def adicionando_testemunhas():
    for i in range(1,3):
        testemunha = input(f"Quem é a {i}ª testemunha? : ")
        lista_testemunhas.append(testemunha)
        
def exibir_ata(presidi,dirigi,dia,hora,orador,tema,regente):
    print("\n\n--------- ATA ---------\n        BATISMO        ")
    print(f"Dia: {dia}   Hora: {hora}\nPresidida: {presidi}\nDirigida: {dirigi}")
    print(f"Regente: {regente}\n1º hino: {lista_hinos[0]}\n1ª oração: {lista_oracao[0]}")
    print(f"Mensagem: {orador}   Tema: {tema}\n\nBatismo de:")
    for i in range(len(lista_batizados)):
        print(f"  {lista_batizados[i]}")
    print("\nBatizadores:")
    for j in range(len(lista_batizadores)):
        print(f"  {lista_batizadores[j]}")
    print(f"\n2º hino: {lista_hinos[1]}\n2ª oração: {lista_oracao[1]}")    
        
def main():
    recebe_hora = D.datetime.now()
    hora = recebe_hora.strftime("%H:%M")
    dia = recebe_hora.strftime("%d-%m-%Y")
    print("Bem vindo a Reunião batismal")
    while True:
        try:
            opcao = int(input("\n1 - Adicionar oração\n2 - Adicionar hinos\n3 - Adicionar Testemunhas\n4 - Adicionar quem Presidi e Dirigi\n5 - Adicionar Batizados\n6 - Adicionar batizadores\n7 - Adicionar regente\n8 - Adicionar Discursante\n9 - Ver Ata Batismal\n0 - Sair\nO que deseja fazer?: "))
            match opcao:
                case 1:
                    adicionando_oracao()
                case 2:
                    adicionando_hino()
                case 3:
                    adicionando_testemunhas()
                case 4:
                    presidi = input("Quem está presidindo?: ")
                    dirigi = input("Quem está dirigindo?: ")
                case 5:
                    qtd_batizados = adicionando_batizados()
                case 6:
                    if len(lista_batizados) == 0:
                        print("\nPessoas a serem batizadas ainda não registradas!")
                    else:
                        adicionando_batizadores(qtd_batizados)
                case 7:
                    regente = input("Quem é o regente?: ")
                case 8:
                    orador = input("Quem vai dar a mensagem? : ")
                    tema = input("Qual o tema? : ")
                case 9:
                    exibir_ata(presidi,dirigi,dia,hora,orador,tema,regente)
                case 0:
                    break
        except ValueError:
            print("\nValor inválido! Digite um número")
    
main()