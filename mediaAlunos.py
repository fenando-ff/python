def turma(qtd_turma):    
    lista = []
    for i in range(1,qtd_turma+1):
        qtd_alunos = int(input(f"Digite a quantidade de alunos na turma {i}: "))
        if qtd_alunos > 40:
            while qtd_alunos > 40:
                print(f"\nNúmero máximo de alunos é 40 alunos por turma")
                qtd_alunos = int(input(f"Digite a quantidade de alunos na turma {i}: "))
                if qtd_alunos <= 40:
                    lista.append(qtd_alunos)
        else:
            lista.append(qtd_alunos)
    return lista

def main():
    qtd_turma = int(input("Digite a quantidade de turmas: "))
    lista = turma(qtd_turma)
    media = sum(lista) / qtd_turma
    # print(f"\n\n{sum(lista)} / {qtd_turma} = {media}\n{lista}")
    print(f"\n\nA média dos alunos é {media:.2f}")
main()