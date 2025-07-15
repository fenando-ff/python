
saldo_disponivel = 1000.00  

valor_saque = float(input("Digite o valor que deseja sacar: R$"))

# Verificar se o valor de saque é menor ou igual ao saldo disponível
if valor_saque < saldo_disponivel:
    # Se o saldo for suficiente, realizar o saque
    saldo_disponivel -= valor_saque
    print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
    print(f"Saldo disponível após o saque: R${saldo_disponivel:.2f}")
else:
    # Se o saldo for insuficiente, mostrar uma mensagem de erro
    print("Saldo insuficiente. Não é possível realizar o saque.")
