def transferencia():
    transferir = 0
    
def conta():
    saldoDisponivel = 2000.0

    while True:
        opcao = int(input("1 - Saque\n2 - Depósito\n3 - Ver saldo\n4 - Tranferência\n5 - Sair\nEscolha uma opção: "))
        if opcao < 6:
            match opcao:
                case 1:
                    if saldoDisponivel == 0:
                        print(f"\nImpossível fazer saque\nSaldo: R${saldoDisponivel:.2f}\n")
                    else:
                        valorSaque = float(input("Digite o valor do saque: R$"))
                        if valorSaque > saldoDisponivel:
                            print(f"\nSaldo insuficiente\nSaldo: R${saldoDisponivel:.2f}\n")
                        else:
                            saldoDisponivel -= valorSaque
                            print("\nSaque realizado com sucesso!\n")
                case 2:
                    valorDeposito = float(input("Digite o valor que deseja depositar: R$"))
                    saldoDisponivel += valorDeposito
                    print("\nDepósito realizado com sucesso!\n")
                case 3:
                    print(f"\nSaldo: R${saldoDisponivel:.2f}\n")
                case 4:
                    # transferencia()
                    print("\nServiço indisponível, estamos em manutenção\n")
                case 5:
                    break
        else:
            print("\nOpção inválida!\n")

conta()