preco_produto1 = float(input("Digite o preço do primeiro produto: R$ "))
preco_produto2 = float(input("Digite o preço do segundo produto: R$ "))
preco_produto3 = float(input("Digite o preço do terceiro produto: R$ "))

if preco_produto1 < preco_produto2 and preco_produto1 < preco_produto3:
        print("Você deve comprar o primeiro produto.")
elif preco_produto2 < preco_produto1 and preco_produto2 < preco_produto3:
        print("Você deve comprar o segundo produto.")
else:
        print("Você deve comprar o terceiro produto.")