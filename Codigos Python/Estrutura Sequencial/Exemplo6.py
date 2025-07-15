# largura: float
# comprimento: float
# metro_quadrado: float
# area: float
# preco: float

largura = float(input("Largura do terreno: "))
comprimento = float(input("Comprimento do terreno: "))
metro_quadrado = float(input("Valor do metro quadrado: "))

area = largura * comprimento
preco = area * metro_quadrado

print(f"Area do terreno = {area:.2f}")
print(f"Preço do terreno = {preco:.2f}")