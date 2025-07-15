capacidade_maxima = int(input("Informe a capacidade máxima do restaurante: "))
soma_clientes = 0

while True:     
    print("\nOpções:")
    print("1. Registrar chegada de clientes")
    print("2. Verificar se o restaurante está lotado")
    print("3. Resgistrar saida de clientes")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        clientes = int(input("Informe o número de clientes que chegaram: "))
        if clientes > capacidade_maxima:
            print("Não há lugares suficiente!!")
        else:
            soma_clientes += clientes
    elif opcao == "2":
        if soma_clientes >= capacidade_maxima:
            print("Restaurante lotado, não há mais mesas disponíveis")
        else:
            print("Ainda há mesas disponíveis.")
    elif opcao == "3":
        clientes = int(input("informe o numero de clientes que sairam: "))
        soma_clientes -= clientes        
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
