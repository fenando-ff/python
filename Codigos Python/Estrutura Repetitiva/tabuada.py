# Solicita ao usuário o número para a tabuada
numero = int(input("Deseja a tabuada de qual número? "))

# Loop de 1 a 10
for i in range(1, 11):
    # Calcula o produto
    produto = numero * i
    # Imprime a tabuada
    print(f"{numero} x {i} = {produto}")
