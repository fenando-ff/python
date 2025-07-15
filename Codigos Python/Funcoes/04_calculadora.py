def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def exibir_menu():
    print("\n==== Calculadora ====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando a calculadora. Até mais!")
        break

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", somar(n1, n2))
    elif opcao == "2":
        print("Resultado:", subtrair(n1, n2))
    elif opcao == "3":
        print("Resultado:", multiplicar(n1, n2))
    elif opcao == "4":
        print("Resultado:", dividir(n1, n2))
    else:
        print("Opção inválida. Tente novamente.")
