def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)
print(f"Média: {media:.2f}")
