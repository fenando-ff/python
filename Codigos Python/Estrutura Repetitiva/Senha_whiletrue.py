senha_correta = 2002

while True:
    senha = int(input("Digite a senha com 4 digitos: "))
    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
