#Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos 
#Em seguida mostre quantos destes valores X estão dentro do intervalo [10,20] e 
#quantos estão fora do intervalo

n = int(input("Digite quantos números deseja incluir: "))

fora_intervalo=0
dentro_intervalo=0

for i in range(n):
    num = int(input(f"Digite o {i + 1}º número: "))

    if num >= 10 and num <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

print(f"Número dentro do intervalo {dentro_intervalo}")
print(f"Número fora do intervalo {fora_intervalo}")