import math

base = float (input("Informe a base do retangulo: "))
altura = float(input("Informe a altura do retangulo: "))

area = base * altura

perimetro = 2 * (base + altura) 
diagonal = math.sqrt(math.pow(base,2) + math.pow(altura,2))

print(f"Area: {area:.4f}")
print(f"Perimetro: {perimetro:.4f}")
print(f"Diagonal: {diagonal:.4f}")

numero = 16
raiz_quadrada = numero ** (1/2)
print(raiz_quadrada) # Saída: 4.0

numero = 9
raiz_quadrada = numero ** 0.5
print(raiz_quadrada) # Saída: 3.05
