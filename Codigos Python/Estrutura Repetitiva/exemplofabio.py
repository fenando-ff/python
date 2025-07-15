opcoes: int; num_clientes: int

num_clientes = 0
opcoes = 0
total_clientes = 0
cap_maxima=int(input("Informe a capacidade máxima do restaurante: "))

while (opcoes != 3):
    print("Opções:")
    print("1. Registrar chegada de clientes")
    print("2. Verificar se o restaurante está lotado")
    print("3. Sair")
    opcoes=int(input("Escolha uma opção: "))
    
    if opcoes == 1:
        num_clientes=int(input("Informe o número de clientes que chegaram: "))
        total_clientes = total_clientes + num_clientes
        if total_clientes >= cap_maxima:
            print("RESTAURANTE LOTADO, NÃO HÁ MAIS MESAS DISPONÍVEIS!") 
    elif opcoes == 2:
        if total_clientes >= cap_maxima:
            print("RESTAURANTE LOTADO, NÃO HÁ MAIS MESAS DISPONÍVEIS!")
        else:
            print("AINDA HÁ VAGAS!") 
    elif opcoes == 3:
        print("SAINDO DO PROGRAMA...")

    else: 
        print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")


