def recebe_minuto(dia):
    minuto = int(input(f"Minutos estudados no dia {dia}: "))
    return minuto

def main():
    lista_minutos = []
    lista_menos30 = []
    meta = 900
    
    for i in range(1,8):
        minuto = recebe_minuto(i)
        lista_minutos.append(minuto)
        if minuto < 30:
            lista_menos30.append(minuto)
    soma_minuto = sum(lista_minutos)
    print(f"Tempo total de estudo na semana: {soma_minuto} minutos")
    print(f"Dias com menos de 30 minutos: {len(lista_menos30)}")
    
    if soma_minuto < meta:
        print("Continue focado, você chega lá!")
    else:
        print("Você alcançou a meta! Parabéns!!")
        
main()