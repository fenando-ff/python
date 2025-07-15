# Ler as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcular a média final
media = (nota1 + nota2 + nota3) / 3

# Verificar a situação do aluno
if media >= 7.0:
    situacao = "APROVADO"
elif media >= 6.0:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "REPROVADO"

# Exibir a média final e a situação do aluno
print(f"Média final: {media:.2f}")
print(f"Situação do aluno: {situacao}")
