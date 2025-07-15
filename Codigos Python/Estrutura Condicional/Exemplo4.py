# Ler três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Inicializar a variável para armazenar o menor número
menor_numero = numero1

# Verificar se o segundo número é menor que o atual menor número
if numero2 < menor_numero:
    menor_numero = numero2
# Verificar se o terceiro número é menor que o atual menor número
elif numero3 < menor_numero:
    menor_numero = numero3
else:
    menor_numero = numero1 

print(f"O menor número entre os três é: {menor_numero}")
