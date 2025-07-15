class Produto:
    def __init__(self, nome, quantidade, preco_compra, preco_venda):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda

estoque = []
total_produtos = 0

def venderProduto(estoque, total_produtos):
    nome_venda = input("Nome do produto a ser vendido: ")
    quantidade_venda = int(input("Quantidade a ser vendida: "))
    encontrado = False
    for i in range(total_produtos):
        if estoque[i].nome == nome_venda:
            if estoque[i].quantidade >= quantidade_venda:
                valor_venda = quantidade_venda * estoque[i].preco_venda
                estoque[i].quantidade -= quantidade_venda
                print("Venda realizada. Valor total da venda:", valor_venda)
                encontrado = True
            else:
                print("Erro: quantidade insuficiente em estoque.")
            break
    if not encontrado:
        print("Erro: produto não encontrado.")

while True:
    print("Opções:")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Vender produto")
    print("4. Calcular valor total do estoque")
    print("5. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        if total_produtos < 100:
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade em estoque: "))
            preco_compra = float(input("Preço de compra: "))
            preco_venda = float(input("Preço de venda: "))
            produto = Produto(nome, quantidade, preco_compra, preco_venda)
            estoque.append(produto)
            total_produtos += 1
            print("Produto adicionado ao estoque.")
        else:
            print("Erro: estoque cheio.")
    elif opcao == 2:
        if total_produtos > 0:
            for i in range(total_produtos):
                print(i + 1, ". ", estoque[i].nome, " - Quantidade: ", estoque[i].quantidade, ", Preço de venda: ", estoque[i].preco_venda)
        else:
            print("Estoque vazio.")
    elif opcao == 3:
        if total_produtos > 0:
            venderProduto(estoque, total_produtos)
        else:
            print("Estoque vazio.")
    elif opcao == 4:
        valor_total_estoque = sum(produto.quantidade * produto.preco_compra for produto in estoque)
        print("Valor total do estoque:", valor_total_estoque)
    elif opcao == 5:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
