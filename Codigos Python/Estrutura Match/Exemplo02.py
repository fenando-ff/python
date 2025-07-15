opcao = int(input("Escolha uma operação:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nOpção: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match opcao:
    case 1:
        print(f"Resultado da soma: {num1 + num2}")
    case 2:
        print(f"Resultado da subtração: {num1 - num2}")
    case 3:
        print(f"Resultado da multiplicação: {num1 * num2}")
    case 4:
        if num2 != 0:
            print(f"Resultado da divisão: {num1 / num2}")
        else:
            print("Erro: divisão por zero!")
    case _:
        print("Opção inválida!")
