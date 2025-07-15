def saque(valorSaque, valorSaldo):
    if valorSaque < valorSaldo:
        valorSaldo = valorSaldo - valorSaque
        print(f"Saldo atual: R${valorSaldo}\nValor do saque: R${valorSaque}")
    else:
        print("Saldo insuficiente")
    return valorSaldo

def deposito(valorNaConta,valorDepositado):
    deposito = valorNaConta + valorDepositado
    return deposito

controle = "s"
saldo = 1000.0
while controle != "n":
    print(f"Saldo: R${saldo}")
    opcao = int(input("Digite 1 para ralizar saque\nDigite 2 para realizar depósito\n"))
    if opcao == 1:
        valor = float(input("Digite o valor do saque: R$"))
        saldo = saque(valor,saldo)
    elif opcao == 2:
        valorAdicionar = float(input("Digite o valor que quer depositar: R$"))
        saldo = deposito(saldo,valorAdicionar)
        print(f"R${saldo}")
    else:
        print("Opção não encontrada!")
    controle = input("Deseja continuar?(s/n)\n")



