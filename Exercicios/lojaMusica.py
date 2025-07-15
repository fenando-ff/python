class Intrumento:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco
        
    def tocar(self):
        pass
    
    def get_preco(self):
        return self.__preco
    
    def set_preco(self,valor):
        try:
            if valor > 0:
                self.__preco = valor
                print("Feito")
        except ValueError:
            print("Digite um valor maior que zero")
    
class Violao(Intrumento):
    def tocar(self):
        print(f"{self.nome} está tocando... 🎸🎼🔊")
        
    def set_preco(self, valor):
        return super().set_preco(valor)
    
class Bateria(Intrumento):
    def tocar(self):
        print(f"{self.nome} está tocando... 🥁🎼🔊")
    
    def set_preco(self, valor):
        return super().set_preco(valor)
    
class Piano(Intrumento):
    def tocar(self):
        print(f"{self.nome} está tocando... 🎹🎼🔊")
        
    def set_preco(self,valor):
        return super().set_preco(valor)
        
lista_intrumentos = []

def main():
    while True:
        opcao = int(input("1 - violão | 2 - bateria | 3 - piano | 4 - tocar | 0 - sair: "))
        match opcao:
            case 1:
                nome = input("Nome do violão: ")
                preco = float(input("Digite o preco: R$"))
                violao = Violao(nome,preco)
                violao.set_preco(preco)
                lista_intrumentos.append(violao)
            case 2:
                nome = input("Nome da bateria: ")
                preco = float(input("Digite o preco: R$"))
                bateria = Bateria(nome,preco)
                bateria.set_preco(preco)
                lista_intrumentos.append(bateria)
            case 3:
                nome = input("Nome do piano: ")
                preco = float(input("Digite o preco: R$"))
                piano = Piano(nome,preco)
                piano.set_preco(preco)
                lista_intrumentos.append(piano)
            case 4:
                for item in lista_intrumentos:
                    item.tocar()
            case 0:
                break
            
main()