numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+ para adição, - para subtração, * para multiplicação, / para divisão): ")

if operacao == '+':
    resultado = numero1 + numero2
    print("O resultado da soma é:", resultado)
elif operacao == '-':
    resultado = numero1 - numero2
    print("O resultado da subtração é:", resultado)
elif operacao == '*':
    resultado = numero1 * numero2
    print("O resultado da multiplicação é:", resultado)
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
        print("O resultado da divisão é:", resultado)
    else:
        print("Não é possível dividir por zero!")
else:
    print("Operação inválida!")

# Verificando se o resultado é par ou ímpar
if resultado % 2 == 0:
    print("O resultado é um número par.")
else:
    print("O resultado é um número ímpar.")

# Verificando se o resultado é positivo ou negativo
if resultado > 0:
    print("O resultado é um número positivo.")
elif resultado < 0:
    print("O resultado é um número negativo.")
else:
    print("O resultado é zero.")
