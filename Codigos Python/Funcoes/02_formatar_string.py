def formatar_string(nome, sobrenome, idade):
  return f"{nome.title()} {sobrenome.title()}, {idade} anos"

nome = "joão"
sobrenome = "silva"
idade = 30

resultado = formatar_string(nome, sobrenome, idade)
print(f"String formatada: {resultado}")