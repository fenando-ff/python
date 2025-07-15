media_aluno = float(input("Digite a média do aluno: "))

match media_aluno:
    case media_aluno if media_aluno < 5:
        print("Você foi reprovado")
    case media_aluno if 5 <= media_aluno < 7:
        print("Você fará a recuperação")
    case media_aluno if media_aluno >= 7:
        print("Você foi aprovado")