# Inicialize as variáveis
codigo_mais_alto = codigo_mais_baixo = codigo_mais_gordo = codigo_mais_magro = None
altura_mais_alto = altura_mais_baixo = peso_mais_gordo = peso_mais_magro = 0
soma_alturas = soma_pesos = total_clientes = 0

while True:
    codigo = input("Digite o código do cliente (ou 0 para sair): ")
    
    if codigo == '0':
        if total_clientes == 0:
            print("Nenhum dado foi inserido. O programa será encerrado.")
            break
        else:
            # Calcula as médias com duas casas decimais
            media_alturas = round(soma_alturas / total_clientes, 2)
            media_pesos = round(soma_pesos / total_clientes, 2)
            
            print("Cliente mais alto - Código:", codigo_mais_alto, "Altura:", round(altura_mais_alto, 2))
            print("Cliente mais baixo - Código:", codigo_mais_baixo, "Altura:", round(altura_mais_baixo, 2))
            print("Cliente mais gordo - Código:", codigo_mais_gordo, "Peso:", round(peso_mais_gordo, 2))
            print("Cliente mais magro - Código:", codigo_mais_magro, "Peso:", round(peso_mais_magro, 2))
            print("Média das alturas dos clientes:", media_alturas)
            print("Média dos pesos dos clientes:", media_pesos)
            break

    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em quilogramas): "))

    soma_alturas += altura
    soma_pesos += peso
    total_clientes += 1

    if altura > altura_mais_alto:
        altura_mais_alto = altura
        codigo_mais_alto = codigo
    if altura < altura_mais_baixo or codigo_mais_baixo is None:
        altura_mais_baixo = altura
        codigo_mais_baixo = codigo
    if peso > peso_mais_gordo:
        peso_mais_gordo = peso
        codigo_mais_gordo = codigo
    if peso < peso_mais_magro or codigo_mais_magro is None:
        peso_mais_magro = peso
        codigo_mais_magro = codigo
