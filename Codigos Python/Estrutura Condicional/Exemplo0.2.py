# Solicita a nota do usuário
nota = float(input("Digite a nota do aluno: "))

# Verifica se a nota está acima de 7
if nota >= 7:
    print("Aluno aprovado!")
elif nota >= 5:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")