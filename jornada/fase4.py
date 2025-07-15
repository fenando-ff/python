def gastos_por_dia(gasto_dia,qtd_dia):
    total = gasto_dia*qtd_dia
    return total

def seguro(total,opcao):
    if opcao == "s":
        total += 150
    else:
        total = total
    return total
    


def main():
    nome_lugar = input("Destino da viagem: ")
    qtd_dias = int(input("Quantidade de dias: "))
    gasto_dia = float(input("Gasto médio por dia: R$"))
    opcao = input("Deseja contratar seguro?(s/n): ").lower()
    total = gastos_por_dia(gasto_dia,qtd_dias)
    gasto_total = seguro(total,opcao)
    if opcao == "s":
        print(f"\nSua viagem para {nome_lugar} por {qtd_dias} dias custará R${gasto_total} com seguro incluso.")
    else:
        print(f"\nSua viagem para {nome_lugar} por {qtd_dias} dias custará R${gasto_total} sem seguro.")
    
main()