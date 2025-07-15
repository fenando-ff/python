##################################### LISTAS #####################################

# # 🧪 Criar e imprimir uma lista
frutas = ["maçã", "banana", "laranja"]
print(frutas)

# # 🧪 Acessar um elemento da lista
nomes = ["Ana", "Carlos", "João"]
print(nomes[1])  

# 🧪 Adicionar item à lista
animais = ["cachorro", "gato"]
animais.append("coelho")
print(animais)

# # 🧪 Remover item da lista
animais.remove("gato")
print(animais)

# 🧪 Tamanho da lista
numeros = [10, 20, 30, 40]
print(len(numeros))  

################################### TUPLAS ###################################

# 🧪 Criar e imprimir uma tupla
cores = ("vermelho", "verde", "azul")   
print(cores)

# 🧪 Acessar um elemento da tupla
meses = ("janeiro", "fevereiro", "março")   
print(meses[2])

# 🧪 Tamanho da tupla
dias_da_semana = ("domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado") 
print(len(dias_da_semana))

# 🧪 Verificar se um elemento está na tupla
frutas = ("maçã", "banana", "laranja")
print("maçã" in frutas) # Retorna True
print("uva" in frutas)  # Retorna False

minha_tupla = (10, 20, 30, 40)
print(f"O tamanho da tupla é: {len(minha_tupla)}")

############################### DICIONÁRIOS ####################    

# 🧪 Criar e imprimir um dicionário
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "São Paulo"
}
print(pessoa)

# 🧪 Acessar um valor no dicionário
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "São Paulo"
}
print(pessoa["idade"])  # Acessa o valor da chave "idade"

# 🧪 Adicionar um novo par chave-valor
cidade = {"nome": "São Paulo"}
cidade["populacao"] = 12000000
print(cidade)

# 🧪 Remover um par chave-valor
cidade = {"nome": "São Paulo", 
          "populacao": 12000000}
del cidade["populacao"]
print(cidade)
