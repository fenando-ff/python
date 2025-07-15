def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

n = int(input("Digite um número inteiro: "))
resultado = verificar_par_ou_impar(n)
print("O número é:", resultado)
