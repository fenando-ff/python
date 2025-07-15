
lista_temperatura = []
lista_menor2 = []
lista_semanal = []
qtd_dias = int(input("Digite quantos dias de análise: "))

def percorre_lista(qtd):        
    if len(lista_temperatura) < 7:
        for j in range(qtd):
            item = lista_temperatura[j]
            lista_semanal.append(item)
    else:
        for j in range(7):
            item = lista_temperatura[j]
            lista_semanal.append(item)

for i in range(1,qtd_dias+1):
    temperatura = float(input(f"Digite a temperatura do {i}º dia: "))
    lista_temperatura.append(temperatura)
    if temperatura < 2.0:
        lista_menor2.append(temperatura)
    
percorre_lista(len(lista_temperatura))
media_semanal = sum(lista_semanal)/len(lista_semanal)
print(f"Média semanal: {media_semanal:.2f}")
print(f"Maior temperatura: {max(lista_temperatura)}")
print(f"Menor temperatura: {min(lista_temperatura)}")
print(f"Dias com temperatura menos que 2°C: {len(lista_menor2)}")