# Ler o preço unitário do produto
preco_unitario = float(input("Digite o preço unitário do produto: "))

# Ler a quantidade de unidades compradas
quantidade = int(input("Digite a quantidade de unidades compradas: "))

# Ler o valor em dinheiro dado pelo cliente
valor_pago = float(input("Digite o valor em dinheiro dado pelo cliente: "))

# Calcular o valor total da compra
valor_total = preco_unitario * quantidade

# Calcular o troco
troco = valor_pago - valor_total

# Verificar se o cliente deu dinheiro suficiente
if troco >= 0:
    print(f"Troco a ser devolvido ao cliente: R${troco:.2f}")
else:
    print("O cliente não deu dinheiro suficiente.")