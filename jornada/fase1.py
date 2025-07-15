import datetime as D
cpf = int(input("Digite seu CPF (apenas números): "))
hora_atual = D.datetime.now()
hora = hora_atual.hour
gerar_senha = cpf * hora % 1000000
print(f"\n{gerar_senha}")

for i in range(1,4):
    print(f"\nTentativa {i} de 3")
    tentativa = int(input("Digite a senha fornecida: "))
    if tentativa == gerar_senha:
        print("Senha válida! Acesso liberado.")
        break
    else:
        print("Senha inválida! Tente novamente!")