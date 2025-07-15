nome = input("Digite o nome do atleta: ")
idade = int(input("Digite a idade do atleta: "))
sexo = input("Digite o sexo do atleta (M/F): ")

print(f"\nAtleta: {nome}")
print(f"Idade: {idade} anos")
print(f"Sexo: {sexo}")

if sexo == "M":
    if idade <= 12:
        categoria = "Infantil"
    elif idade <= 17:
        categoria = "Juvenil"
    elif idade <= 35:
        categoria = "Adulto"
    else:
        categoria = "Sênior"
    print(f"Categoria: {categoria}")

elif sexo == "F":
    if idade <= 10:
        categoria = "Infantil"
    elif idade <= 16:
        categoria = "Juvenil"
    elif idade <= 30:
        categoria = "Adulto"
    else:
        categoria = "Sênior"
    print(f"Categoria: {categoria}")

else:
    print("Sexo inválido. Informe apenas 'M' ou 'F'.")
