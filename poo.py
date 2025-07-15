import datetime as D
lista_livro = []
class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def detalhes(self):
            print(f"\nTítulo: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}")
           
    def eh_classico(self):
        if self.ano < 1980:
            livro = self.detalhes()
            print(livro)
           
    def media(self):
        ano = D.date.today().year # Recebe o ano atual da máquina
        print(sum(ano - livro.ano for livro in lista_livro) / len(lista_livro))

while True:
    try:
        opcao = int(input("\n1 - Adicionar livro\n2 - Exibir livros\n3 - Clássicos\n4 - Média\n0 - Sair\nDigite uma opção: "))
        match opcao:
            case 1:
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                ano = int(input("Digite o ano do livro: "))
                lista_livro.append(Livro(titulo,autor,ano))
            case 2:
                for livro in lista_livro:
                    livro.detalhes()
            case 3:
                for livro in lista_livro:
                    livro.eh_classico()
            case 4:
                for livro in lista_livro:
                    livro.media()
            case 0:
                break
    except ValueError:
        print("\nValor inválido! Digite um número")
        