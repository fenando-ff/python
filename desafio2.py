def chegada_clientes(qtd_clientes, capacidade):
    if qtd_clientes <= capacidade:
        capacidade -= qtd_clientes
    return capacidade

def saida_clientes(qtd_clientes,capacidade):
    capacidade += qtd_clientes
    return capacidade

def vip():
    nome = input("Digite o nome da pessoa: ")
    lista_vip.append(nome)
    print("Cliente Cadastrado")

lista_vip = []
lista_dia = []
controle = "s"
capacidade = int(input("Digite a capacidade máxima de seu restaurante: "))
capacidade_maxima = capacidade
contador_cliente = 0
while controle.lower() != "n":
    opcao = int(input("\nO que deseja fazer?\nChegada de cliente = 1\nSaída de cliente = 2\nVerificar vagas = 3\nAdicionar VIP = 4\nEncerrar o dia = 5\nVer lista VIP = 6\n\nDigite sua escolha:\n "))
    match opcao:
        case 1:
            qtd_clientes = int(input("Digite a quantidade de pessoas: "))
            if capacidade < qtd_clientes:
                print(f"Vagas insuficientes! há {capacidade} vagas")
            else:
                capacidade = chegada_clientes(qtd_clientes,capacidade)
                contador_cliente += qtd_clientes
                lista_dia.append(qtd_clientes)
        case 2:
            qtd_clientes = int(input("Digite a quantidade de pessoas: "))
            if qtd_clientes <= contador_cliente:
                contador_cliente -= qtd_clientes
                capacidade = saida_clientes(qtd_clientes,capacidade)
            else:
                print("Tá saindo mais gente do que tem lá dentro!")
        case 3:
            print(f"\nQuantidade de vagas: {capacidade}")
        case 4:
            vip()
        case 5:
            if capacidade != capacidade_maxima:
                print("Ainda há clientes no restaurante!")
            else: 
                controle = "n"
        case 6:
            print(lista_vip)
        case opcao if opcao > 5:
            print("\nEscolha inválida!\n")
dia = sum(lista_dia)
if dia >= 200:
    print(f"\nO dia teve {dia} clientes, foi um ótimo dia")
elif dia >= 150 and dia < 200:
    print(f"\nO dia teve {dia} clientes, foi um dia mediano")
else:
    print(f"\nO dia teve {dia} clientes, foi um péssimo dia")