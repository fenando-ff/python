# 3 - Crie um sistema que vai receber o saldo do usuário, criar uma lista de compras,  permitir que o usuário adicione itens, remover itens, printar a lista atual, 
# os valores dos itens da lista, somar os valores dos itens da lista e subtrair do saldo do usuário e printar o saldo restante. 
# O programa deve continuar rodando até o usuário decidir sair



def adicionar_item(produto):
    compras.append(produto)
    
def remover_item(produto):
    compras.remove(produto)

saldo = float(input("Digite seu saldo: "))
compras = []
controle = "s"
while controle.lower() == "s":
    print(f"\n{compras}")
    opcao = int(input("1 = adicionar item\n2 = remover item\nO que deseja fazer? : "))
    produto = input("Digite o nome do produto: ").lower()
    if opcao == 1:
        adicionar_item(produto)
    elif opcao == 2:
        if produto not in compras:
            print(f"\n{produto} não encontrado!\n")
        else:
            remover_item(produto)
    else:
        print("\nOpção inválida!")
    controle = input("Deseja continuar? (s/n): ")
    
    
    
    
valor_compras = {
    compras[0]: 10.00,
    compras[1]: 20.00,
}

print(valor_compras.items())